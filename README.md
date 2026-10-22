Jinwei Hu's Personal Website

Google Scholar citations in the bio update automatically from the
`google-scholar-stats` branch and round down to the nearest hundred.
Daily collection runs on the owner's server with:

```bash
python3 google_scholar_crawler/update.py
```

The updater reads the Scholar profile from `_config.yml` and uses the existing
Git credentials. It publishes only citation data in a temporary checkout.
GitHub Actions remains available for manual collection, although Scholar may
rate-limit GitHub-hosted runners.
