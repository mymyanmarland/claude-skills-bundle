#!/usr/bin/env python3
"""Download the whole Claude Skills Bundle Drive tree, verbatim.

Source root: 1WqFsmAiPxEe65S540rM6mgRVbUiYa8pO (Claude Skills Bundle)
Parent folder also holds the 2 PDFs (downloaded separately to docs/).
Output: ~/workspace/claude-skills-bundle-work/download/<relpath>
Manifest: ~/workspace/claude-skills-bundle-work/manifest.json
"""
import subprocess, json, os, hashlib, sys
from concurrent.futures import ThreadPoolExecutor, as_completed

CLI = "/opt/hatch/bin/hatch_gws_cli"
BASE = "/home/hatch/workspace/claude-skills-bundle-work"
OUT = os.path.join(BASE, "download")
ROOT_ID = "1WqFsmAiPxEe65S540rM6mgRVbUiYa8pO"

def cli_list(fid):
    items, token = [], None
    while True:
        params = {"q": f"'{fid}' in parents and trashed=false",
                  "pageSize": 100, "fields": "files(id,name,mimeType,size),nextPageToken"}
        if token:
            params["pageToken"] = token
        out = subprocess.check_output(
            [CLI, "drive", "files", "list", "--params", json.dumps(params)],
            text=True)
        data = json.loads(out)
        items.extend(data.get("files", []))
        token = data.get("nextPageToken")
        if not token:
            return items

def walk(fid, rel):
    """Return list of (file_id, relpath, size, mime)."""
    found = []
    for it in cli_list(fid):
        name = it["name"]
        if it["mimeType"] == "application/vnd.google-apps.folder":
            found.extend(walk(it["id"], f"{rel}/{name}" if rel else name))
        else:
            found.append((it["id"], f"{rel}/{name}" if rel else name,
                          int(it.get("size") or 0), it["mimeType"]))
    return found

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def download_one(job):
    fid, rel, size, mime = job
    dest = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if os.path.exists(dest) and os.path.getsize(dest) == size:
        return (rel, "cached", size, sha256(dest))
    for attempt in range(3):
        try:
            subprocess.check_call(
                [CLI, "drive", "files", "get", "--params",
                 json.dumps({"fileId": fid, "alt": "media"}),
                 "--output", dest],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            got = os.path.getsize(dest)
            if got != size:
                raise RuntimeError(f"size mismatch {rel}: got {got} want {size}")
            return (rel, "ok", size, sha256(dest))
        except Exception as e:
            if attempt == 2:
                return (rel, f"FAILED: {e}", size, None)
    return (rel, "FAILED", size, None)

def main():
    print("walking Drive tree...", flush=True)
    jobs = walk(ROOT_ID, "")
    print(f"files found: {len(jobs)}", flush=True)
    skills = [j for j in jobs if j[1].endswith(".skill")]
    ds = [j for j in jobs if os.path.basename(j[1]) == ".DS_Store"]
    print(f".skill files: {len(skills)}, .DS_Store: {len(ds)}", flush=True)
    todo = [j for j in jobs if os.path.basename(j[1]) != ".DS_Store"]
    manifest = []
    done = 0
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(download_one, j): j for j in todo}
        for fut in as_completed(futs):
            rel, status, size, digest = fut.result()
            manifest.append({"path": rel, "status": status,
                             "size": size, "sha256": digest})
            done += 1
            if done % 200 == 0:
                print(f"downloaded {done}/{len(todo)}", flush=True)
    fails = [m for m in manifest if not m["status"].startswith(("ok", "cached"))]
    total = sum(m["size"] for m in manifest if m["status"].startswith(("ok", "cached")))
    print(f"DONE ok={len(manifest)-len(fails)} failed={len(fails)} bytes={total}", flush=True)
    for m in fails:
        print("FAIL", m, flush=True)
    with open(os.path.join(BASE, "manifest.json"), "w") as f:
        json.dump({"total_drive_files": len(jobs), "skill_files": len(skills),
                   "ds_store_skipped": len(ds), "downloaded": manifest}, f, indent=1)
    print("manifest written", flush=True)
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
