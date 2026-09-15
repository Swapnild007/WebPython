from pathlib import Path
import argparse, hashlib, shutil

def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest()

def organize(root, dry_run=True):
    root=Path(root); seen={}; moved=0
    for p in root.iterdir():
        if not p.is_file(): continue
        key=digest(p); seen.setdefault(key,[]).append(p)
    for files in seen.values():
        for p in files[1:]:
            target=root/'duplicates'/p.name
            target.parent.mkdir(exist_ok=True)
            if not dry_run: shutil.move(str(p),target)
            moved+=1
    return moved

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('folder'); ap.add_argument('--apply',action='store_true'); a=ap.parse_args()
    print(f"Duplicate candidates moved: {organize(a.folder, not a.apply)}")
