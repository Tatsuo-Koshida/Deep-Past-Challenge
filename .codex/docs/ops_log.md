# Ops log

## 2026-02-27

### Kaggle official data download (Deep Past Challenge)

- Competition: `deep-past-initiative-machine-translation`
- Destination: `data/kaggle/deep-past-initiative-machine-translation/`
- Method: Kaggle MCP to obtain a signed download URL, then `curl` to fetch `archive.zip` and `unzip` it locally.
- Note: In the default sandboxed shell, DNS/network access was unavailable; the download required running `curl` with escalated permissions.

