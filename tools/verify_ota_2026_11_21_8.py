#!/usr/bin/env python3
"""Fail-closed verification of signed QuangNV 2026.11.21.8 Word OTA test payload.
The existing RSA PUBLIC modulus only; no private signing material in this repository.
"""
from pathlib import Path
import base64, hashlib, json, zipfile, xml.etree.ElementTree as ET

VERSION="2026.11.21.8"
TAG="v"+VERSION
NAME="ChuanHoa_VanBanDang_"+VERSION+".dotm"
DIR=Path("ota-releases")/TAG
OLD=Path("ChuanHoa_VanBanDang_2026.11.21.6.dotm")
NEW=Path(NAME)
BASE_SHA="e9036d7ede1b7e213e38dd2e77a9d45a4a5e07815372bca7ad587d2ea3e34166"
TARGET_SHA="d0d485707462ddbc33af6fb42dc39ba698127b73ea20483d7067ffdf60216af4"
DELTA_SHA="8782330eb7d69b233e91c2e94a11b4c48ea77cc057ce5e97d2cc1ce393b50d43"
VBA_SHA="1d715c75c521631b3fd1f58e7e0527cbec87432da5b3785c2b7a842ca286660f"
PUB_MODULUS_B64="2DL65j3yzSGoPlhBlowlIGEKqLKElvFFk+3zRq3mhfiDh8QVmdUpW7HXNyKy/5dJImibgB0RO3VB+2cDYQ0BlOOPq6Oqd36YhtWurEI2GiHHcIiK3wXTuA1noR3U8DswBNgmAAkmzUBTmblZ5vF/2g09dsR7P3Oc4FBm3i8+/1we1gCUSqxVUzEd6z70x2zjv33Tdj89ynp8XSGAWNvv91v9UTzFPp6Pw3rALxwTevv6I3oEThGOcM/cx/JctK0g5a41db+W6iGgPt7w5v0+CtPtTaJzJIEn71TjQ304YdFvUuADNEE8YWBihkqQ555M+V0UrwPUl+ChODsnD408KYaKzLPkpR2lklO3pJPKqVZduPJoGdJ8xzDqxO55fN6L8/pK5ey8vlQwJiu9e4k73XyQ9FPHENPn2/72tQpm76AS41TY4m4TcdYUMxnpZwuAwfAmhcpRNEHrvGO8NqgU+PLhrKb7/2/v+HO4QTFm3Gvttdmy/GORUnKGEDjMDU+n"

def bad(reason):
    raise SystemExit("REJECTED OTA .8: "+reason)
def sha(data):
    return hashlib.sha256(data).hexdigest()
def verify_signature(message,sig):
    blob=base64.b64decode(PUB_MODULUS_B64,validate=True)
    n=int.from_bytes(blob,"big")
    if len(sig)!=len(blob):return False
    v=int.from_bytes(sig,"big")
    if not 0<v<n:return False
    block=pow(v,65537,n).to_bytes(len(blob),"big")
    der=bytes.fromhex("3031300d060960864801650304020105000420")+hashlib.sha256(message).digest()
    return block==b"\x00\x01"+b"\xff"*(len(blob)-len(der)-3)+b"\x00"+der

def main():
    manifest=json.loads((DIR/"manifest_OTA_DA_KY.json").read_text(encoding="utf-8-sig"))
    url="https://github.com/quanglci/QuangNV-Word-Addin/releases/download/"+TAG+"/"+NAME
    for field,value in {"version":VERSION,"tag":TAG,"filename":NAME,"url":url,"sha256":TARGET_SHA}.items():
        if manifest.get(field)!=value:bad("manifest mismatch: "+field)
    if sha(OLD.read_bytes())!=BASE_SHA:bad("published .6 baseline changed")
    patch=base64.b64decode((DIR/"delta_b64.txt").read_text().strip(),validate=True)
    if sha(patch)!=DELTA_SHA:bad("binary delta mismatch")
    binary=NEW.read_bytes()
    if sha(binary)!=TARGET_SHA or manifest.get("file_size_bytes")!=len(binary):bad("generated DOTM does not match signed build")
    with zipfile.ZipFile(NEW) as z:
        if z.testzip() is not None:bad("corrupt DOTM")
        if len(z.namelist())!=41 or len(set(z.namelist()))!=41:bad("unexpected document contents count")
        names=set(z.namelist())
        if not {"[Content_Types].xml","word/vbaProject.bin","customUI/customUI.xml","customUI/customUI14.xml"}.issubset(names):
            bad("missing required Office component")
        if sha(z.read("word/vbaProject.bin"))!=VBA_SHA:bad("VBA project unexpected; do not publish")
        for name in ("customUI/customUI.xml","customUI/customUI14.xml"):
            xml=z.read(name)
            ET.fromstring(xml)
            text=xml.decode("utf-8")
            if text.count('id="btnQNV_CheckUpdate"')!=1:bad("missing or duplicate Ribbon OTA button")
            if 'onAction="RibbonQNV_KiemTraCapNhat"' not in text:bad("OTA Ribbon callback missing")
            if "lblQNV_CurrentVersion" in text:bad("old external version label returned")
    msg=(VERSION+"\n"+TARGET_SHA+"\n"+url).encode("utf-8")
    try:sig=base64.b64decode(manifest["signature"],validate=True)
    except (KeyError,ValueError):bad("invalid signature data")
    if not verify_signature(msg,sig):bad("RSA-SHA256 signature is invalid")
    print("PASS QuangNV OTA .8: ZIP, Ribbon, VBA fingerprint, SHA256 and RSA verified")
    print("DOTM:",TARGET_SHA)

if __name__=="__main__":
    main()
