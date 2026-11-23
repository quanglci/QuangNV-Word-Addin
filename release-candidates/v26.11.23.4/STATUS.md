# QuangNV 26.11.23.4 — OTA chuyển tiếp 23/23.1 → 26.11.23.5

**STATUS: BUILT / UNSIGNED / NOT TESTED ON WINDOWS / NOT PUBLISHED / PRODUCTION FEED INACTIVE**

A working, source-included builder and an unsigned pilot kit were generated **23 November 2026**. The one ZIP is stored privately in the owner's Google Drive folder `QuangNV_PhatHanh_ChinhThuc/Cho_Phat_Hanh_26.11.23.5/OTA_ChuyenTiep_26.11.23.4`.

## Components

- Original V7 DOTM 26.11.23.1, verified SHA256 `b0ea41f12d5f4abb705f436a9aae9312d4df2a24a6635a439856b245edc6d84b`
- Owner-PC Windows PowerShell authoring script; adds a new VBA Ribbon callback `QNV_Bridge_Run` by Word COM, only to a **copy** of that DOTM, and adds a visible **Hoàn tất nâng cấp 26.11.23.5** button.
- RSA signer/verifier Windows EXE; accepts only the same production public key as the existing 23.1 manager, private key remains on the owner's PC.
- 32-bit Windows GUI executable `QuangNV_OTA_Bridge_26.11.23.4.exe` (works on 32/64-bit Windows), SHA256 `4b4282a62c672d283de00e0ae28b34663a226af04f26483d4f61a871183dcc62`.
- Full Setup `QuangNV_Setup_26.11.23.5_Universal.exe` SHA256 `65b7401f3b57e7ed8fcb21ba2f31c736af5555fbf892e91fe2924882168bd7f5`.
- RSA-aware one-machine pilot installer and rollback PowerShell script.

## OTA sequence

1. Existing signed-DOTM OTA manager installs **signed** `ChuanHoa_VanBanDang_26.11.23.4.dotm` from `v26.11.23.4` GitHub Release, triggered by user acceptance and closed Word.
2. User restarts Word and clicks **Hoàn tất nâng cấp 26.11.23.5**. The added VBA macro downloads the exact GitHub Release bridge EXE; SHA256 is pinned and verified by Windows certutil, with explicit user consent.
3. The bridge downloads the exact full installer from `v26.11.23.5`, verifies SHA256 and MZ, waits for Word to close **without killing the process**, then starts Full Setup.
4. Full Setup updates DOTM/COM/AI/OTA Universal and its version state; existing Word 23+ functions are intended to remain intact. This step requires actual Windows verification.

## Missing gates (MANDATORY)

- Generate the DOTM using Word on the owner's machine (VBOM trust is needed on authoring machine **only**); static Linux tools cannot insert a VBA module into the OOXML binary `vbaProject.bin`.
- Sign with the **original production RSA private key held locally**; it must never be uploaded or shared.
- Publish 26.11.23.4 and 26.11.23.5 assets as GitHub prereleases. Both release tags were absent when inspected.
- Pilot end-to-end on a test machine **without disabling antivirus**. The old feed is common to all machines: do **not** set enabled=yes to test.
- Only after successful pilot and rollback verification, activate a new, accurately signed row `26.11.23.4` in the `OTA_AnToan` Google Sheet feed. Keep `26.11.23.1` untouched until then.

**No changes have been made to the production Google Sheets OTA feed.** This is a prepared bridge project, not a released update.
