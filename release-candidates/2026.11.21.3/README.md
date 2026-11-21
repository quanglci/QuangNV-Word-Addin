# QuangNV 2026.11.21.3 — Signed Word OTA candidate

**Status:** NOT PUBLISHED / NOT ENABLED. This page documents a release candidate, not a downloadable GitHub Release.

- Source: final QuangNV 2026.11.21.2 source archive
- Proposed tag: `v2026.11.21.3`
- Proposed binary: `ChuanHoa_VanBanDang_2026.11.21.3.dotm`
- SHA-256: `5be2a4188497a78d955a04257e978250e64428dcca8717593a67f8c87db6e955`
- Change scope: **only** `docProps/core.xml` metadata. VBA and Ribbon XML are identical to the archive's final source.
- Signed with the matching RSA-SHA256 OTA release key; private key is **not** in this repository.
- Google Sheet `OTA_AnToan`: version 2026.11.21.3 added with `enabled=no`.

## Compatibility check before activation
The Windows installer modifies the installed `QNV_Update` VBA module after installing the bundled DOTM to add a dynamic version message. The archived DOTM may not contain that per-machine patch. Therefore, do **not** activate this candidate until the installed DOTM has been compared with the candidate using the read-only compatibility checker, or the currently installed DOTM has been used to regenerate and re-sign the release.

When verified, upload the candidate DOTM to a **pre-release** under `v2026.11.21.3`. Confirm GitHub asset SHA-256 and HTTPS download, test on one Windows machine with Word closed, and only then consider switching the Google Sheet row to `enabled=yes`. Keep antivirus protection enabled.
