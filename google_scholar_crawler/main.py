from scholarly import scholarly
import json
from datetime import datetime, timezone
import os

scholarly.set_timeout(30)
scholarly.set_retries(2)

author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
if not isinstance(author.get('citedby'), int) or author['citedby'] < 0:
    raise ValueError('Google Scholar did not return a valid citation count')
author['updated'] = datetime.now(timezone.utc).isoformat()
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(f"Updated Google Scholar citations for {name}: {author['citedby']}")
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
