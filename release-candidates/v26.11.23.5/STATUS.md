# QuangNV 26.11.23.5 — OTA release gate

**Status: STAGING / NOT PUBLISHED / NOT ACTIVE**

Owner-approved version name: **26.11.23.5**.
The feature set corresponds to the tested **QuangNV AI V5.3.5 Universal** patch.
The official production OTA remains **26.11.23.1 (Fix V7)** until the following release gates pass.

## Critical compatibility issue
The current Word OTA manager validates an RSA signature over `version + "\n" + sha256 + "\n" + URL` and only accepts payload URLs of the exact form:
`https://github.com/quanglci/QuangNV-Word-Addin/releases/download/v<version>/ChuanHoa_VanBanDang_<version>.dotm`.

The currently tested V5.3.5 Universal installer is **not** a self-contained upgrade from 26.11.23 or 26.11.23.1. It requires existing V5.3.1 and V5.3.4 state/files and also the V5.3 AI processing baseline.
Changing the version number and uploading its EXE as if it were a signed DOTM update would not install the required AI/COM/UI components.

## Release gates before production feed activation
- Create a **single self-contained** 26.11.23.5 Universal upgrade (Windows/Office 32- and 64-bit) from the stable 26.11.23/.1 baseline. Include AI deep scan, two-pass scan/repair, green/yellow highlighting, Vietnamese dialogs, colored UI, progress, Fix V7 and OTA.
- Update **existing installations' OTA manager** via a trusted compatible bootstrap path that handles EXE/package updates, verifies publisher signature and SHA-256, checks architecture and prerequisites, and never runs arbitrary unsigned payloads.
- Make atomic backups of DOTM, COM registration, DLL, AI executables/settings and restore on failure.
- Validate migration and rollback on Word 32-bit and Word 64-bit, with Microsoft Word fully closed, and verify Kaspersky/Defender.
- Sign the **actual** distributable by the owner's production signing key; publish immutable assets on GitHub and verify hashes via GitHub API.
- Enable the 26.11.23.5 production feed row **only after** these tests. Keep the currently working signed 26.11.23.1 row untouched until then.

No GitHub production release, OTA feed change, or implicit rollout is authorized by this staging document alone.
