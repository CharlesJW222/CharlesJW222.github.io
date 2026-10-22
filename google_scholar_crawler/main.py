"""Read citation totals from the public Google Scholar profile."""

import json
from datetime import datetime, timezone
from html.parser import HTMLParser
import os
from pathlib import Path
import time
from urllib.error import URLError
from urllib.parse import parse_qs, urlencode, urlparse
from urllib.request import Request, urlopen


def citation_count(text):
    value = ''.join(text.split()).replace(',', '')
    if not value.isascii() or not value.isdecimal():
        raise ValueError('Google Scholar did not return a valid citation count')
    return int(value)


class ScholarProfile(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.name = ''
        self.citedby = None
        self.publications = {}
        self.in_stats = False
        self.paper = None
        self.capture = None
        self.parts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get('class', '').split()
        target = None
        if tag == 'table' and attrs.get('id') == 'gsc_rsb_st':
            self.in_stats = True
        elif tag == 'div' and attrs.get('id') == 'gsc_prf_in':
            target = 'name'
        elif self.in_stats and tag == 'td' and 'gsc_rsb_std' in classes and self.citedby is None:
            target = 'citedby'
        elif tag == 'tr' and 'gsc_a_tr' in classes:
            self.paper = {'num_citations': 0}
        elif self.paper is not None and tag == 'a':
            if 'gsc_a_at' in classes:
                query = parse_qs(urlparse(attrs.get('href', '')).query)
                self.paper['author_pub_id'] = query.get('citation_for_view', [''])[0]
            elif 'gsc_a_ac' in classes:
                target = 'num_citations'
        if target:
            self.capture = (tag, target)
            self.parts = []

    def handle_data(self, data):
        if self.capture:
            self.parts.append(data)

    def handle_endtag(self, tag):
        if self.capture and tag == self.capture[0]:
            target = self.capture[1]
            text = ''.join(self.parts).strip()
            if target == 'name':
                self.name = text
            elif target == 'citedby':
                self.citedby = citation_count(text)
            elif target == 'num_citations':
                self.paper['num_citations'] = citation_count(text) if text else 0
            self.capture = None
        if tag == 'table':
            self.in_stats = False
        elif tag == 'tr' and self.paper is not None:
            if self.paper.get('author_pub_id'):
                self.publications[self.paper['author_pub_id']] = self.paper
            self.paper = None


def fetch_profile(scholar_id):
    url = 'https://scholar.google.com/citations?' + urlencode({'user': scholar_id, 'hl': 'en', 'pagesize': 100})
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Accept-Language': 'en'})
    for attempt in range(3):
        try:
            with urlopen(request, timeout=30) as response:
                html = response.read().decode('utf-8')
            break
        except URLError:
            if attempt == 2:
                raise
            time.sleep(5 * (attempt + 1))
    profile = ScholarProfile()
    profile.feed(html)
    if profile.citedby is None or not profile.name:
        raise ValueError('Google Scholar profile or citation table is unavailable')
    return {
        'scholar_id': scholar_id,
        'name': profile.name,
        'citedby': profile.citedby,
        'publications': profile.publications,
        'updated': datetime.now(timezone.utc).isoformat(),
    }


def main():
    author = fetch_profile(os.environ['GOOGLE_SCHOLAR_ID'])
    results = Path('results')
    results.mkdir(exist_ok=True)
    (results / 'gs_data.json').write_text(json.dumps(author, ensure_ascii=False), encoding='utf-8')
    shield = {'schemaVersion': 1, 'label': 'citations', 'message': str(author['citedby'])}
    (results / 'gs_data_shieldsio.json').write_text(json.dumps(shield), encoding='utf-8')
    print(f"Updated Google Scholar citations for {author['name']}: {author['citedby']}")


if __name__ == '__main__':
    main()
