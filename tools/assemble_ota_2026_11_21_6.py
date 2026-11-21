#!/usr/bin/env python3
"""Rebuild QuangNV v2026.11.21.6 from the published stable v.5 ZIP.
Signed payload is compared against a byte-for-byte expected SHA-256.
This code never needs or accesses an RSA private key.
"""
import base64, copy, hashlib, json, struct, zipfile, zlib
from pathlib import Path

BASE = Path("ChuanHoa_VanBanDang_2026.11.21.5.dotm")
PATCH = Path("ota-releases/v2026.11.21.6/payload_b64.txt")
OUT = Path("ChuanHoa_VanBanDang_2026.11.21.6.dotm")
SOURCE_SHA = "ff26e3592c2e291cb86f1100c27b3a4761792b134c252b27355bfbf1955c3bb0"
PATCH_SHA = "4fca5edf258888bdb71bee9e3a413a82ac19049291d8883c3996987c40af0708"
OUT_SHA = "e9036d7ede1b7e213e38dd2e77a9d45a4a5e07815372bca7ad587d2ea3e34166"
VBA_SHA = "8bbf5c5bbea8c85b0b120255bd137dca2e8af12a7212c2594684023423c2bd75"
CHANGED = {"word/vbaProject.bin","word/settings.xml","word/glossary/settings.xml","docProps/core.xml","docProps/app.xml","customUI/customUI.xml","customUI/customUI14.xml"}

def sha(data): return hashlib.sha256(data).hexdigest()
def reject(why): raise SystemExit("OTA REJECTED: " + why)

if sha(BASE.read_bytes()) != SOURCE_SHA: reject("Wrong published stable base")
raw = base64.b64decode(PATCH.read_text().strip(),validate=True)
if sha(raw) != PATCH_SHA: reject("Patch hash mismatch")
delta = json.loads(zlib.decompress(raw))
if delta.get("format") != "QNV6P2" or delta.get("source_sha256") != SOURCE_SHA or delta.get("vba_sha256") != VBA_SHA:
    reject("Patch metadata mismatch")
if set(delta["entry_edits"]) | {"word/vbaProject.bin"} != CHANGED: reject("Unexpected modified files")
with zipfile.ZipFile(BASE) as source:
    if source.testzip() is not None: reject("Invalid source ZIP")
    vba=bytearray(source.read("word/vbaProject.bin"))
    patch=base64.b64decode(delta["ole_delta"],validate=True)
    (count,) = struct.unpack_from("<I",patch,0)
    pos=4
    for i in range(count):
        offset,size = struct.unpack_from("<II",patch,pos)
        pos+=8
        if offset+size>len(vba) or pos+size>len(patch): reject("Patch offset invalid")
        vba[offset:offset+size]=patch[pos:pos+size]
        pos+=size
    if pos!=len(patch) or sha(vba)!=VBA_SHA: reject("Compiled VBA hash mismatch")
    with zipfile.ZipFile(OUT,"w") as out:
        for info in source.infolist():
            name=info.filename
            data=source.read(name)
            if name=="word/vbaProject.bin": data=bytes(vba)
            elif name in delta["entry_edits"]:
                new=bytearray(data)
                for start,end,newpart in reversed(delta["entry_edits"][name]):
                    if not 0<=start<=end<=len(new): reject("Bad XML edit")
                    new[start:end]=base64.b64decode(newpart,validate=True)
                data=bytes(new)
            if info.compress_type!=zipfile.ZIP_STORED: reject("Base ZIP format not deterministic")
            out.writestr(copy.copy(info),data)
if sha(OUT.read_bytes())!=OUT_SHA: reject("Final signed DOTM hash mismatch")
with zipfile.ZipFile(OUT) as z:
    if z.testzip() is not None: reject("Corrupt output")
    for name in ("customUI/customUI.xml","customUI/customUI14.xml"):
        txt=z.read(name)
        if b"lblQNV_CurrentVersion" in txt or b"btnQNV_CheckUpdate" not in txt: reject("Ribbon mismatch")
print("PASS:",OUT,"SHA256",OUT_SHA)
