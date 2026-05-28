# 🎵 Youtube Playlist Web Scraping

![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-Prototype-yellowgreen.svg)

Professional, focused Python tool to scrape music charts and assemble YouTube Music playlists automatically.

**Quick summary:** the project scrapes song titles from a chart URL (see `src/data/`) and uses `ytmusicapi` to create a playlist and add songs automatically via the saved auth in `src/auth/browser.json`.

**Repository layout**
- `src/main.py` — entrypoint (runs the scrape → create playlist flow)
- `src/auth/yt_auth.py` — returns an authenticated `ytmusicapi.YTMusic` instance using `src/auth/browser.json`
- `src/auth/browser.json` — persisted authentication headers/session (keep private)
- `src/data/datas.py` — scraping logic (BeautifulSoup + requests)
- `src/data/extra.py` — example chart URLs

Table of contents
- [Quickstart](#quickstart)
- [How it works](#how-it-works)
- [Authentication (`browser.json`)](#authentication-browserjson)
- [Customization & usage](#customization--usage)
- [Dependencies](#dependencies)
- [Troubleshooting](#troubleshooting)
- [Contributing & License](#contributing--license)

## Quickstart

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS / Linux
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Provide authenticated headers for `ytmusicapi` by placing the file at `src/auth/browser.json` (see next section).

4. Run the scraper:

```bash
python src/main.py
```

On success the script will print progress messages and create a private playlist on your YouTube Music account.

## How it works

- `src/data/datas.py` scrapes the configured chart URL (default in `src/main.py`) and returns a list of song titles.
- `src/auth/yt_auth.py` loads `YTMusic('src/auth/browser.json')` to authenticate.
- `src/main.py` searches each song on YouTube Music and adds the top result to a newly created private playlist.

## Authentication (`browser.json`)

`ytmusicapi` requires authentication headers to operate on your account. The project expects those headers in `src/auth/browser.json`.

Ways to obtain `browser.json`:

- Using `ytmusicapi` setup helper (recommended): follow the `ytmusicapi` docs at https://ytmusicapi.readthedocs.io to export headers for `YTMusic`.
- Manually export authentication headers/cookies from your browser and save them to `src/auth/browser.json` (keep the file private).

Important security note: never commit `src/auth/browser.json` to source control. Add it to `.gitignore`.

### How to export headers (step-by-step)

1. Open https://music.youtube.com and sign in to your account in the browser you control.
2. Open the browser Developer Tools (right-click → Inspect or press `F12`).
3. Switch to the `Network` tab and enable the `Preserve log` option (optional but helpful).
4. In the YouTube Music UI click a page that triggers network requests (for example: `Library` or any page that loads your account data).
5. In the Network list look for a request to a `music.youtube.com` endpoint (the request often appears with "music" or "browse" in the path). Click that request.
6. Select the `Headers` sub-tab for the request and locate the `Request Headers` section.
7. Copy the values of the `Authorization` header and the `Cookie` header.
8. Create `src/auth/browser.json` and paste them into the example JSON structure:

```json
{
  "Accept": "*/*",
  "Authorization": "YOUR_AUTHORIZATION_TOKEN",
  "Content-Type": "application/json",
  "X-Goog-AuthUser": "0",
  "x-origin": "https://music.youtube.com",
  "Cookie": "Your_Cookie_Here"
}
```

9. Save the file and keep it private. If you ever commit it accidentally, rotate your account session (log out and re-authenticate) and regenerate headers.

Tip: instead of placing real credentials in the repo, keep `src/auth/browser.example.json` (this repo) and copy it locally to `src/auth/browser.json` on your machine.

## Customization & usage

- Change the chart/source URL: edit the `url` variable in `src/main.py` or modify the script to accept a command-line argument.
- To create a public playlist, change the `privacy_status` parameter in `src/main.py` when calling `create_playlist()`.

Example: change the URL in `src/main.py` to a different chart from `src/data/extra.py`.

## Dependencies

Install the project dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

Minimum recommended Python packages:

- `ytmusicapi` — interact with YouTube Music
- `requests` — HTTP requests
- `beautifulsoup4` — HTML parsing
- `pandas` — optional (data handling)

See `requirements.txt` for an exact list.

## Troubleshooting

- "I am already signed in but the script still asks me to sign in":
  - Confirm `src/auth/browser.json` contains valid, up-to-date headers/cookies for YouTube Music.
  - If you exported headers from a different browser profile or a different browser version, regenerate them.
  - Run `python src/main.py` with an visible browser/session (if you change the auth flow) to confirm credentials work.

- Errors searching or adding songs:
  - The script uses `YTMusic.search(..., filter='songs', limit=1)`; some songs may not return results—verify manually in YouTube Music and adjust logic if needed.

## Contributing & License

- Contributions welcome. Open an issue or PR with a short description and a reproducible example.
- Add a `LICENSE` file; the README currently shows an MIT badge — change the badge if you choose a different license.

---

If you'd like, I can:
- add a small CLI wrapper to pass the chart URL and output options,
- generate a `.gitignore` entry for `src/auth/browser.json`, or
- create a polished `requirements.txt` now (I can auto-generate one from `src/` imports).

Tell me which of these you'd like next.