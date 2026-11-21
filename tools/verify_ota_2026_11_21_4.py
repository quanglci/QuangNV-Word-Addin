#!/usr/bin/env python3
"""Fail-closed verifier for the signed QuangNV Word 2026.11.21.4 OTA asset.
Only public key material is embedded. Never store a signing private key here.
"""
import base64, hashlib, json, pathlib, re, sys, zipfile

VERSION = "2026.11.21.4"
TAG = "v" + VERSION
FILENAME = "ChuanHoa_VanBanDang_" + VERSION + ".dotm"
ROOT = pathlib.Path("ota-releases") / TAG
OLD_VBA = "9adeb37833bfe1abd1f5ab314d43db49420b509c2c1bf15d0f383f1453f817cb"
RIBBONS = {
    "customUI/customUI.xml": "dc31845555d8de5c74a0f826d3ed5eda4d1141a3b3889d7cbc6962039a7e6344",
    "customUI/customUI14.xml": "78eb269685f967c9695fa3ba4a9c9ed2f5ef73c6188646cbc23efb002c369b76",
}
MODULUS_B64 = "2DL65j3yzSGoPlhBlowlIGEKqLKElvFFk+3zRq3mhfiDh8QVmdUpW7HXNyKy/5dJImibgB0RO3VB+2cDYQ0BlOOPq6Oqd36YhtWurEI2GiHHcIiK3wXTuA1noR3U8DswBNgmAAkmzUBTmblZ5vF/2g09dsR7P3Oc4FBm3i8+/1we1gCUSqxVUzEd6z70x2zjv33Tdj89ynp8XSGAWNvv91v9UTzFPp6Pw3rALxwTevv6I3oEThGOcM/cx/JctK0g5a41db+W6iGgPt7w5v0+CtPtTaJzJIEn71TjQ304YdFvUuADNEE8YWBihkqQ555M+V0UrwPUl+ChODsnD408KYaKzLPkpR2lklO3pJPKqVZduPJoGdJ8xzDqxO55fN6L8/pK5ey8vlQwJiu9e4k73XyQ9FPHENPn2/72tQpm76AS41TY4m4TcdYUMxnpZwuAwfAmhcpRNEHrvGO8NqgU+PLhrKb7/2/v+HO4QTFm3Gvttdmy/GORUnKGEDjMDU+n"

def reject(message):
    raise SystemExit("KHONG PHAT HANH OTA: " + message)

def digest(data):
    return hashlib.sha256(data).hexdigest()

def verify_rsa(message, signature):
    """PKCS#1 v1.5 SHA-256 signature verification, without dependencies."""
    modulus_bytes = base64.b64decode(MODULUS_B64, validate=True)
    n = int.from_bytes(modulus_bytes, "big")
    e = 65537
    k = len(modulus_bytes)
    if len(signature) != k:
        return False
    s = int.from_bytes(signature, "big")
    if not 0 < s < n:
        return False
    encoded = pow(s, e, n).to_bytes(k, "big")
    digest_info = bytes.fromhex("3031300d060960864801650304020105000420") + hashlib.sha256(message).digest()
    expected = b"\x00\x01" + (b"\xff" * (k - len(digest_info) - 3)) + b"\x00" + digest_info
    return encoded == expected

def main():
    dotm = ROOT / FILENAME
    manifest_file = ROOT / "manifest_OTA_DA_KY.json"
    if not dotm.is_file() or not manifest_file.is_file():
        reject("Thieu tep DOTM da Word bien dich hoac manifest da ky")
    manifest = json.loads(manifest_file.read_text(encoding="utf-8-sig"))
    url = ("https://github.com/quanglci/QuangNV-Word-Addin/releases/"
           "download/" + TAG + "/" + FILENAME)
    if any(manifest.get(k) != value for k, value in (
        ("version", VERSION), ("tag", TAG), ("filename", FILENAME), ("url", url))):
        reject("Manifest khong khop version/tag/filename/URL chinh thuc")
    raw = dotm.read_bytes()
    sha = digest(raw)
    if sha != manifest.get("sha256") or sha != str(manifest.get("sha256", "")).lower():
        reject("SHA-256 DOTM khong khop manifest")
    if not (100000 <= len(raw) <= 30 * 1024 * 1024):
        reject("Kich thuoc DOTM khong hop le")
    if manifest.get("file_size_bytes") != len(raw):
        reject("Kich thuoc tren manifest khong dung")
    try:
        with zipfile.ZipFile(dotm) as z:
            if z.testzip() is not None:
                reject("ZIP DOTM bi hong")
            names = set(z.namelist())
            for name in ["[Content_Types].xml", "word/vbaProject.bin", *RIBBONS]:
                if name not in names:
                    reject("DOTM thieu " + name)
            if digest(z.read("word/vbaProject.bin")) == OLD_VBA:
                reject("VBA giong ban .3: chua chua thay doi kiem tra OTA khi mo Word")
            for name, expected in RIBBONS.items():
                if digest(z.read(name)) != expected:
                    reject("Ribbon da thay doi bat ngo: " + name)
    except zipfile.BadZipFile:
        reject("DOTM khong phai ZIP Office hop le")
    try:
        signature = base64.b64decode(manifest["signature"], validate=True)
    except (KeyError, ValueError):
        reject("Thieu hoac sai chu ky RSA")
    message = (VERSION + "\n" + sha + "\n" + url).encode("utf-8")
    if not verify_rsa(message, signature):
        reject("Chu ky RSA-SHA256 khong hop le")
    print("PASS: DOTM, VBA changed, Ribbon preserved, SHA-256 and RSA signature verified")
    print("SHA256:", sha)
    print("URL:", url)

if __name__ == "__main__":
    main()
