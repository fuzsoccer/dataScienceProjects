"""Pin upstream revisions and verify cached bytes before reuse."""
import hashlib
import gzip
import json
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPOS = {"statsbomb": "statsbomb/open-data", "metrica": "metrica-sports/sample-data"}


def get(url):
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "soccer-portfolio/0.1"}), timeout=120) as response:
                return response.read()
        except OSError:
            if attempt == 2:
                raise
            time.sleep(attempt + 1)


def fetch(root, competition=43, season=106, match_count=3, game=1):
    root = Path(root)
    lock_path = root / "sources.lock.json"
    lock = json.loads(lock_path.read_text(encoding="utf-8")) if lock_path.exists() else {"revisions": {}, "files": {}}
    for name, repo in REPOS.items():
        if name not in lock["revisions"]:
            lock["revisions"][name] = json.loads(get(f"https://api.github.com/repos/{repo}/commits/master"))["sha"]
    def download(source, remote, local):
        compressed = "RawTrackingData" in local
        if compressed:
            local += ".gz"
        path = root / "data/raw" / local
        url = f"https://raw.githubusercontent.com/{REPOS[source]}/{lock['revisions'][source]}/{remote}"
        if path.exists() and local in lock["files"]:
            cached = gzip.decompress(path.read_bytes()) if compressed else path.read_bytes()
            digest = hashlib.sha256(cached).hexdigest()
            if digest != lock["files"][local]["sha256"]:
                raise ValueError(f"Checksum mismatch: {path}; restore or remove this cached file")
            return path
        data = get(url)
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_suffix(path.suffix + ".part")
        temporary.write_bytes(gzip.compress(data, mtime=0) if compressed else data)
        temporary.replace(path)
        lock["files"][local] = {"url": url, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data), "downloaded_at": datetime.now(timezone.utc).isoformat()}
        lock_path.write_text(json.dumps(lock, indent=2) + "\n")
        print(f"Downloaded {local}: {len(data):,} bytes", flush=True)
        return path
    for source in REPOS:
        download(source, "README.md", f"{source}/README.md")
    download("statsbomb", "LICENSE.pdf", "statsbomb/LICENSE.pdf")
    download("statsbomb", "data/competitions.json", "statsbomb/competitions.json")
    matches = download("statsbomb", f"data/matches/{competition}/{season}.json", f"statsbomb/matches/{competition}_{season}.json")
    selected = sorted(json.loads(matches.read_text(encoding="utf-8")), key=lambda m: (m["match_date"], m["match_id"]))[:match_count]
    for match in selected:
        for kind in ("events", "lineups"):
            download("statsbomb", f"data/{kind}/{match['match_id']}.json", f"statsbomb/{kind}/{match['match_id']}.json")
    prefix = f"Sample_Game_{game}"
    for suffix in ("RawTrackingData_Home_Team.csv", "RawTrackingData_Away_Team.csv", "RawEventsData.csv"):
        filename = f"{prefix}_{suffix}"
        download("metrica", f"data/{prefix}/{filename}", f"metrica/{filename}")
    lock_path.write_text(json.dumps(lock, indent=2) + "\n")

