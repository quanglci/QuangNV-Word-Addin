#!/usr/bin/env python3
"""Strictly verify a UI-only signed QuangNV 2026.11.21.5 release.
The original v2026.11.21.3 VBA must remain byte-for-byte identical."""
from pathlib import Path
from zipfile import ZipFile
import base64, hashlib, json, xml.etree.ElementTree as ET

TAG = "v2026.11.21.5"
OLD = Path("ChuanHoa_VanBanDang_2026.11.21.3.dotm")
NEW = Path("ChuanHoa_VanBanDang_2026.11.21.5.dotm")
DIR = Path("ota-releases") / TAG
OLD_SHA = "5be2a4188497a78d955a04257e978250e64428dcca8717593a67f8c87db6e955"
VBA_SHA = "9adeb37833bfe1abd1f5ab314d43db49420b509c2c1bf15d0f383f1453f817cb"
PATCH_SHA = "9ea32225b3ed3703fc501ab1b57ba6b0032bac01ec0bdfc192acda31a5b8a396"
MODULUS_B64 = "2DL65j3yzSGoPlhBlowlIGEKqLKElvFFk+3zRq3mhfiDh8QVmdUpW7HXNyKy/5dJImibgB0RO3VB+2cDYQ0BlOOPq6Oqd36YhtWurEI2GiHHcIiK3wXTuA1noR3U8DswBNgmAAkmzUBTmblZ5vF/2g09dsR7P3Oc4FBm3i8+/1we1gCUSqxVUzEd6z70x2zjv33Tdj89ynp8XSGAWNvv91v9UTzFPp6Pw3rALxwTevv6I3oEThGOcM/cx/JctK0g5a41db+W6iGgPt7w5v0+CtPtTaJzJIEn71TjQ304YdFvUuADNEE8YWBihkqQ555M+V0UrwPUl+ChODsnD408KYaKzLPkpR2lklO3pJPKqVZduPJoGdJ8xzDqxO55fN6L8/pK5ey8vlQwJiu9e4k73XyQ9FPHENPn2/72tQpm76AS41TY4m4TcdYUMxnpZwuAwfAmhcpRNEHrvGO8NqgU+PLhrKb7/2/v+HO4QTFm3Gvttdmy/GORUnKGEDjMDU+n"
def fail(msg):
    raise SystemExit("OTA REJECTED: "+msg)
def sha(b):
    return hashlib.sha256(b).hexdigest()
def verify_sig(msg, signature):
    nbytes = base64.b64decode(MODULUS_B64, validate=True)
    n = int.from_bytes(nbytes,"big")
    if len(signature)!=len(nbytes):return False
    value = int.from_bytes(signature,"big")
    if not 0<value<n:return False
    decoded = pow(value,65537,n).to_bytes(len(nbytes),"big")
    prefix = bytes.fromhex("3031300d060960864801650304020105000420")
    data = prefix+hashlib.sha256(msg).digest()
    expected = b"\x00\x01"+b"\xff"*(len(nbytes)-len(data)-3)+b"\x00"+data
    return expected==decoded

def main():
    manifest=json.loads((DIR/"manifest_OTA_DA_KY.json").read_text("utf-8"))
    expected_url="https://github.com/quanglci/QuangNV-Word-Addin/releases/download/"+TAG+"/"+NEW.name
    if (manifest.get("version"),manifest.get("tag"),manifest.get("filename"),manifest.get("url")) != ("2026.11.21.5",TAG,NEW.name,expected_url):
        fail("manifest version, filename or download URL mismatch")
    if sha(OLD.read_bytes())!=OLD_SHA:fail("original v.3 hash mismatch")
    if sha(base64.b64decode((DIR/"delta_b64.txt").read_text().strip(),validate=True))!=PATCH_SHA:
        fail("delta patch SHA-256 mismatch")
    if sha(NEW.read_bytes())!=manifest["sha256"] or NEW.stat().st_size!=manifest["file_size_bytes"]:
        fail("new Word Add-in differs from the signed release")
    with ZipFile(OLD) as o, ZipFile(NEW) as n:
        if o.testzip() is not None or n.testzip() is not None:fail("corrupt Office package")
        a={i.filename:o.read(i.filename) for i in o.infolist()}
        b={i.filename:n.read(i.filename) for i in n.infolist()}
    if set(a)!=set(b):fail("Office package entries changed")
    changed={k for k in a if a[k]!=b[k]}
    if changed!={"docProps/core.xml","customUI/customUI.xml","customUI/customUI14.xml"}:
        fail("unexpected contents changed: "+repr(changed))
    if sha(a["word/vbaProject.bin"])!=VBA_SHA or a["word/vbaProject.bin"]!=b["word/vbaProject.bin"]:
        fail("VBA code changed; refusing to publish")
    for k in ("customUI/customUI.xml","customUI/customUI14.xml"):
        xml=b[k].decode("utf-8")
        ET.fromstring(xml)
        if "lblQNV_CurrentVersion" not in xml or "2026.11.21.5" not in xml:
            fail("version label not found in Ribbon")
    raw=("2026.11.21.5\n"+manifest["sha256"]+"\n"+expected_url).encode()
    if not verify_sig(raw,base64.b64decode(manifest["signature"],validate=True)):
        fail("invalid RSA-SHA256 signature")
    print("PASS: original stable VBA preserved, Ribbon version label, SHA-256 and RSA signature verified.")
    print("SHA-256:",manifest["sha256"])

if __name__=="__main__":
    main()
