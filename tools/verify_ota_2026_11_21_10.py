#!/usr/bin/env python3
"""Strict, fail-closed verification for QuangNV signed Word OTA 2026.11.21.9.
This tool carries only the existing RSA PUBLIC modulus, never any private key.
"""
from pathlib import Path
from zipfile import ZipFile
import base64,hashlib,json,xml.etree.ElementTree as ET

VERSION="2026.11.21.10";TAG="v"+VERSION
NAME="ChuanHoa_VanBanDang_"+VERSION+".dotm"
DIR=Path("ota-releases")/TAG
OLD=Path("ChuanHoa_VanBanDang_2026.11.21.9.dotm");NEW=Path(NAME)
BASE_SHA="7ed8e459c6facda667bd3bbc89f304f6df9f044103fc8494ff4975463f2f44cc"
TARGET_SHA="f18305f7348b4578dcf83948b3b685e327c5b3e2fbd0f301363d61897ef60cdd"
DELTA_SHA="8de7416cbeb0498d41be64fc166de33459d140fcc80f0a64303d823c145a0c7d"
VBA_SHA="eaf2769bc958b0c8eb6fa31acfa97bfb84dacb2b78464ccba0b9e2ffba3ffb1e"
ORIGINAL_SHA="7c48ded8d515066f37351ca7a37ae8aaaf2c25568ed18c129da3644510d8e1a3"
XML_SHA={"customUI/customUI.xml":"24ce0a71d7dffee62fb9eb4d20865dbf100353c31b7ef38a3a1596c10eb5ef5e","customUI/customUI14.xml":"b0cceea8b7b7f9e3c7d284f3a47631d80557fe07ffb273909b0ff96e2affa4ca"}
PUB_MODULUS_B64="2DL65j3yzSGoPlhBlowlIGEKqLKElvFFk+3zRq3mhfiDh8QVmdUpW7HXNyKy/5dJImibgB0RO3VB+2cDYQ0BlOOPq6Oqd36YhtWurEI2GiHHcIiK3wXTuA1noR3U8DswBNgmAAkmzUBTmblZ5vF/2g09dsR7P3Oc4FBm3i8+/1we1gCUSqxVUzEd6z70x2zjv33Tdj89ynp8XSGAWNvv91v9UTzFPp6Pw3rALxwTevv6I3oEThGOcM/cx/JctK0g5a41db+W6iGgPt7w5v0+CtPtTaJzJIEn71TjQ304YdFvUuADNEE8YWBihkqQ555M+V0UrwPUl+ChODsnD408KYaKzLPkpR2lklO3pJPKqVZduPJoGdJ8xzDqxO55fN6L8/pK5ey8vlQwJiu9e4k73XyQ9FPHENPn2/72tQpm76AS41TY4m4TcdYUMxnpZwuAwfAmhcpRNEHrvGO8NqgU+PLhrKb7/2/v+HO4QTFm3Gvttdmy/GORUnKGEDjMDU+n"
def fail(s):raise SystemExit("REJECTED QuangNV OTA .10: "+s)
def sha(b):return hashlib.sha256(b).hexdigest()
def verify_signature(msg,sig):
    blob=base64.b64decode(PUB_MODULUS_B64,validate=True)
    n=int.from_bytes(blob,"big")
    if len(sig)!=len(blob):return False
    v=int.from_bytes(sig,"big")
    if not 0<v<n:return False
    block=pow(v,65537,n).to_bytes(len(blob),"big")
    der=bytes.fromhex("3031300d060960864801650304020105000420")+hashlib.sha256(msg).digest()
    return block==b"\x00\x01"+b"\xff"*(len(blob)-len(der)-3)+b"\x00"+der
def xml_id(root, id):
    found=[n for n in root.iter() if n.attrib.get("id")==id]
    if len(found)!=1:fail("Ribbon missing or duplicated "+id)
    return found[0]
def main():
    manifest=json.loads((DIR/"manifest_OTA_DA_KY.json").read_text(encoding="utf-8-sig"))
    url=f"https://github.com/quanglci/QuangNV-Word-Addin/releases/download/{TAG}/{NAME}"
    fields={"version":VERSION,"tag":TAG,"filename":NAME,"url":url,"sha256":TARGET_SHA,"file_size_bytes":1116629,"vba_project_sha256":VBA_SHA,"original_Windows_saved_dotm_sha256":ORIGINAL_SHA,"signature_algorithm":"RSASSA-PKCS1-v1_5 with SHA-256"}
    for k,v in fields.items():
        if manifest.get(k)!=v:fail("manifest mismatch: "+k)
    if sha(OLD.read_bytes())!=BASE_SHA:fail("previous public OTA .8 baseline changed")
    patch=base64.b64decode((DIR/"delta_b64.txt").read_text().strip(),validate=True)
    if sha(patch)!=DELTA_SHA:fail("binary patch does not match vetted patch")
    if sha(NEW.read_bytes())!=TARGET_SHA:fail("reconstructed DOTM SHA256 mismatch")
    with ZipFile(OLD) as old,ZipFile(NEW) as new:
        names_old=set(old.namelist());names_new=set(new.namelist())
        if len(names_new)!=41 or len(names_old)!=41 or names_new!=names_old:fail("Word component list changed")
        if new.testzip() is not None or old.testzip() is not None:fail("corrupt Word package")
        changed={n for n in names_new if old.read(n)!=new.read(n)}
        allowed={"word/vbaProject.bin","customUI/customUI.xml","customUI/customUI14.xml","docProps/app.xml","docProps/core.xml","word/settings.xml","word/glossary/settings.xml"}
        if changed!=allowed:fail("unexpected changed internal Word component(s): "+str(changed^allowed))
        if sha(new.read("word/vbaProject.bin"))!=VBA_SHA:fail("unverified VBA fingerprint")
        vba=new.read("word/vbaProject.bin")
        if b"QuangNV_OTA_Notifier.exe" not in vba or b"2026.11.21.10" not in vba:fail("notifier guard or version constant missing from compiled VBA")
        if b"QuangNV_OTA_Notifier.exe" in old.read("word/vbaProject.bin"):fail("notifier existed in previous release unexpectedly")
        for n,expected in XML_SHA.items():
            raw=new.read(n)
            if sha(raw)!=expected:fail("Ribbon XML differs from approved Word-saved source: "+n)
            root=ET.fromstring(raw)
            updater=xml_id(root,"grpQuangNV_Update")
            child=[x.attrib.get("id") for x in updater]
            if child!=["btnQNV_CheckUpdate","lblQNV_PhienBan_TrongCapNhat","chkQNV_AutoUpdate"]:fail("update Ribbon 3-line order invalid")
            if xml_id(root,"btnQNV_CheckUpdate").attrib.get("onAction")!="RibbonQNV_KiemTraCapNhat":fail("missing update callback")
            if xml_id(root,"lblQNV_PhienBan_TrongCapNhat").attrib.get("label")!="Phiên bản QuangNV Add-in: 2026.11.21.10":fail("version label mismatch")
            cb=xml_id(root,"chkQNV_AutoUpdate")
            if cb.attrib.get("label")!="Hiển thị thông báo khi có bản cập nhật mới" or cb.attrib.get("getPressed")!="RibbonQNV_AutoGet" or cb.attrib.get("onAction")!="RibbonQNV_AutoSet":fail("notification checkbox modified")
            box=xml_id(root,"boxQNV_LoaiVanBanHome")
            if box.attrib.get("boxStyle")!="vertical" or [i.attrib.get("id") for i in box]!=["lblQNV_LoaiVanBanHome","ddDonViHome"]:fail("Home document type layout invalid")
            dd=xml_id(root,"ddDonViHome")
            if dd.attrib.get("onAction")!="RibbonDonVi_OnAction" or dd.attrib.get("getSelectedItemIndex")!="RibbonDonVi_GetSelectedIndex":fail("document type callback changed")
            if any("lblQNV_CurrentVersion"==x.attrib.get("id") for x in root.iter()):fail("old standalone version label persists")
    sig=base64.b64decode(manifest["signature"],validate=True)
    if not verify_signature((VERSION+"\n"+TARGET_SHA+"\n"+url).encode("utf-8"),sig):
        fail("invalid RSA-SHA256 signature")
    print("PASS OTA .10: signed manifest, expected SHA-256, 41 Word components, VBA fingerprint, exact Ribbon and all update callbacks verified")
    print("SHA-256:",TARGET_SHA)
if __name__=="__main__":main()
