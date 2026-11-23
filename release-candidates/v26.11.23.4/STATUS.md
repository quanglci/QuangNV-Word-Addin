# QuangNV 26.11.23.4 — Signed bridge PILOT R4

**Status: RSA-SIGNED FILE VERIFIED / PILOT PACKAGE BUILT / NOT RELEASED / PRODUCTION OTA UNCHANGED**

On 24 November 2026, the owner supplied the signed bridge DOTM, signed manifest, SHA256SUMS, single-machine pilot EXE and rollback scripts.

## Cryptographic verification
- `ChuanHoa_VanBanDang_26.11.23.4.dotm`: SHA256 `7cce9b9d8e1e3bb495695db288b769a6df3e5b1cbe27b86630a152565a0c2692`, size **454422 bytes**.
- Signed manifest `version=26.11.23.4`, `release_scope=pilot`, `tag=v26.11.23.4` and fixed URL to the exact release asset.
- **RSA PKCS#1 v1.5 with SHA-256 signature VALID** against the official 3072-bit production public key already used by QuangNV.
- DOTM ZIP has exactly **41 components** and validates without errors. Ribbon `customUI.xml` and `customUI14.xml` add only `btnQNV_Bridge235` and update version text to `26.11.23.4` (besides normal Word-save metadata and VBA binary changes).
- VBA binary contains `QNV_Bridge_Run`, matching Ribbon callback; compiled macro behavior remains subject to Windows/Word pilot testing.

## Single-machine pilot R4
- Original R3 pilot utility had a Windows overwrite issue: `os.Rename(tmp, dest)` cannot replace a pre-existing DOTM.
- Pilot **R4** uses Win32 `MoveFileExW(REPLACE_EXISTING | WRITE_THROUGH)`, refuses unknown baseline hashes, backs up DOTM and OTA state, verifies signed manifest, and pre-stages the **unchanged, SHA-pinned** bridge EXE and Full Setup EXE in the local cache.
- This supports offline / one-machine pilot **without publishing** any GitHub release or enabling the shared Google Sheets feed.
- Only pilot tool was rebuilt; **the RSA-signed DOTM, signed manifest, bridge and Full Setup binaries were not modified**.

Pilot R4 package SHA-256:
`8915ac99feea6781321aa09220a3aca7f67187ef1973c3e5f7fb5f6d29a08045`

Owner's Google Drive private staging folder:
`QuangNV_PhatHanh_ChinhThuc/Cho_Phat_Hanh_26.11.23.5/OTA_ChuyenTiep_26.11.23.4`.

## Mandatory remaining gates
1. Pilot on one Windows machine with QuangNV **26.11.23 or 26.11.23.1**, Word closed, antivirus enabled.
2. In Word click the new `Hoàn tất nâng cấp 26.11.23.5`; verify Full Setup, Ribbon, all AI modes (including progress dialogs), version label, OTA and rollback.
3. Do not run the pilot on the stable source computer. Signed content integrity does not replace application compatibility testing.
4. After pilot success, publish both GitHub release assets, inspect remote SHA256, then activate the signed bridge feed entry. **Never enable the production feed before this gate**.

No GitHub releases or production feed changes were made during this verification. No private RSA key was accessed or uploaded.
