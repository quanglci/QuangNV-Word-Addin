#!/usr/bin/env python3
"""Rebuild exactly signed QuangNV .4 DOTM from GitHub .3 + small zstd VBA delta.
Does not possess any release signing private key. Aborts on any hash mismatch.
"""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED,ZIP_STORED
import base64,copy,hashlib,json,re,subprocess,tempfile
TAG="v2026.11.21.4"
BASE=Path("ota-releases")/TAG
OLD=Path("ChuanHoa_VanBanDang_2026.11.21.3.dotm")
OUT=BASE/"ChuanHoa_VanBanDang_2026.11.21.4.dotm"
OLD_SHA="5be2a4188497a78d955a04257e978250e64428dcca8717593a67f8c87db6e955"
PATCH_SHA="dbf01b5ebd5bf230d30b9cfc366223a5037af525fb4c731726ff303e162fe4a1"
VBA_SHA="5377078dd77b4bc2cf05c48b583c29c9d48220e409804c098b1f926eec6f1c2f"
def sha(blob):return hashlib.sha256(blob).hexdigest()
def fail(msg):raise SystemExit("OTA VERIFY FAILED: "+msg)
def replace(blob,before,after):
    if blob.count(before)!=1:fail("expected exact unique replacement missing")
    return blob.replace(before,after)
def rsids(blob,new_ids):
    m=re.search(rb"<w:rsids>(.*?)</w:rsids>",blob,re.DOTALL)
    if m is None:fail("missing rsids")
    src=m.group(1)
    root=re.match(rb"<w:rsidRoot[^>]+/>",src)
    if root is None:fail("missing rsidRoot")
    old_ids=[v.decode("ascii") for v in re.findall(rb'<w:rsid w:val="([A-F0-9]{8})"/>',src)]
    if old_ids!=sorted(old_ids) or len(old_ids)!=len(set(old_ids)) or any(i in old_ids for i in new_ids):fail("rsids inconsistent")
    middle=root.group(0)+b"".join(('<w:rsid w:val="'+v+'"/>').encode("ascii") for v in sorted(old_ids+new_ids))
    return blob[:m.start(1)]+middle+blob[m.end(1):]
def main():
    if not OLD.is_file() or sha(OLD.read_bytes())!=OLD_SHA:fail("old GitHub asset SHA invalid")
    manifest=json.loads((BASE/"manifest_OTA_DA_KY.json").read_text("utf-8"))
    patch=base64.b64decode((BASE/"vba_patch_base64.txt").read_text("ascii").strip(),validate=True)
    if sha(patch)!=PATCH_SHA:fail("VBA binary patch SHA invalid")
    with ZipFile(OLD) as zin:
        if zin.testzip():fail("old DOTM damaged")
        infos=zin.infolist()
        entries={i.filename:zin.read(i.filename) for i in infos}
    with tempfile.TemporaryDirectory() as td:
        old=Path(td)/"old.bin"; delta=Path(td)/"patch.zst"; new=Path(td)/"new.bin"
        old.write_bytes(entries["word/vbaProject.bin"])
        delta.write_bytes(patch)
        subprocess.run(["zstd","--patch-from="+str(old),"-d",str(delta),"-o",str(new),"-q","-f"],check=True)
        entries["word/vbaProject.bin"]=new.read_bytes()
    if sha(entries["word/vbaProject.bin"])!=VBA_SHA or sha(entries["word/vbaProject.bin"])!=manifest["vba_sha256"]:fail("VBA SHA invalid")
    entries["word/settings.xml"]=rsids(entries["word/settings.xml"],["002E06A8","005F686C","007369E7","009C5DD3"])
    entries["word/glossary/settings.xml"]=rsids(entries["word/glossary/settings.xml"],["00021139","001E0347","007369E7","009C5DD3"])
    entries["docProps/app.xml"]=replace(entries["docProps/app.xml"],b"<Template>ChuanHoa_VanBanDang_DA_THEM_CAP_NHAT.dotm</Template>",b"<Template>ChuanHoa_VanBanDang.dotm</Template>")
    core=entries["docProps/core.xml"]
    core=replace(core,b"QuangNV 2026.11.21.3 - OTA test from final source 2026.11.21.2; VBA and Ribbon unchanged.",b"QuangNV 2026.11.21.4 - Word-startup OTA check; compiled VBA from tested Windows hotfix; Ribbon unchanged.")
    core=replace(core,b"<cp:revision>127</cp:revision>",b"<cp:revision>129</cp:revision>")
    core=replace(core,b"2026-11-21T05:11:00Z",b"2026-11-21T10:12:00Z")
    entries["docProps/core.xml"]=core
    OUT.parent.mkdir(parents=True,exist_ok=True)
    with ZipFile(OUT,"w") as zout:
        for info in infos:
            x=copy.copy(info)
            stored=info.filename.startswith("customUI/images/") or info.filename in ("customUI/customUI.xml","customUI/customUI14.xml")
            x.compress_type=ZIP_STORED if stored else ZIP_DEFLATED
            x.extract_version=10 if stored else 20
            x.create_system=0
            x.create_version=45
            zout.writestr(x,entries[info.filename])
    digest=sha(OUT.read_bytes())
    if digest!=manifest["sha256"] or OUT.stat().st_size!=manifest["file_size_bytes"]:
        OUT.unlink(missing_ok=True)
        fail("reconstructed DOTM differs from signed release")
    with ZipFile(OUT) as z:
        if z.testzip():fail("reconstructed DOTM damaged")
    print("VERIFIED EXACT OTA BINARY",digest)
if __name__=="__main__":main()
