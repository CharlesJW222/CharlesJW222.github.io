"""Fetch Scholar citations and publish them without changing the site checkout."""

from datetime import datetime, timezone
import fcntl
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
from urllib.parse import parse_qs, urlparse

from main import fetch_profile


def git(directory, *arguments, check=True):
    result = subprocess.run(
        ['git', '-C', str(directory), *arguments],
        capture_output=True, text=True, timeout=90,
        env=dict(os.environ, GIT_TERMINAL_PROMPT='0'),
    )
    if check and result.returncode:
        raise RuntimeError(result.stderr.strip() or 'Git command failed')
    return result


def publish_stats(author, source_repo):
    remote = git(source_repo, 'remote', 'get-url', 'origin').stdout.strip()
    name = git(source_repo, 'config', 'user.name').stdout.strip()
    email = git(source_repo, 'config', 'user.email').stdout.strip()
    with tempfile.TemporaryDirectory(prefix='scholar-citations-') as directory:
        checkout = Path(directory)
        git(checkout, 'init', '--quiet', '-b', 'google-scholar-stats')
        git(checkout, 'remote', 'add', 'origin', remote)
        branch = git(checkout, 'ls-remote', '--exit-code', '--heads', 'origin', 'google-scholar-stats', check=False)
        if branch.returncode == 0:
            git(checkout, 'fetch', '--quiet', '--depth=1', 'origin', 'google-scholar-stats')
            git(checkout, 'checkout', '--quiet', '--detach', 'FETCH_HEAD')
        elif branch.returncode != 2:
            raise RuntimeError(branch.stderr.strip() or 'Cannot check the statistics branch')
        git(checkout, 'config', 'user.name', name)
        git(checkout, 'config', 'user.email', email)
        (checkout / 'gs_data.json').write_text(json.dumps(author, ensure_ascii=False), encoding='utf-8')
        shield = {'schemaVersion': 1, 'label': 'citations', 'message': str(author['citedby'])}
        (checkout / 'gs_data_shieldsio.json').write_text(json.dumps(shield), encoding='utf-8')
        git(checkout, 'add', 'gs_data.json', 'gs_data_shieldsio.json')
        if git(checkout, 'diff', '--cached', '--quiet', check=False).returncode == 1:
            git(checkout, 'commit', '--quiet', '-m', 'Update Google Scholar citation data')
            git(checkout, 'push', '--quiet', 'origin', 'HEAD:google-scholar-stats')


def main():
    source_repo = Path(__file__).resolve().parent.parent
    lock_path = git(source_repo, 'rev-parse', '--git-path', 'scholar-update.lock').stdout.strip()
    lock_path = source_repo / lock_path
    with lock_path.open('w') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return
        config = (source_repo / '_config.yml').read_text(encoding='utf-8')
        match = re.search(r'^\s*googlescholar\s*:\s*[\"\']?([^\"\'\n]+)', config, re.M)
        if not match:
            raise ValueError('No Google Scholar profile is configured')
        scholar_id = parse_qs(urlparse(match.group(1).strip()).query)['user'][0]
        author = fetch_profile(scholar_id)
        publish_stats(author, source_repo)
        print(f"{datetime.now(timezone.utc).isoformat()} Updated citations for {author['name']}: {author['citedby']}", flush=True)


if __name__ == '__main__':
    main()
