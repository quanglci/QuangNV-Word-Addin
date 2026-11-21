# QuangNV 2026.11.21.6 — Version in 'Kiểm tra cập nhật' popup

**STATUS: NOT PUBLISHED / NOT SIGNED / OTA DISABLED**

Purpose: move the version display from a separate Ribbon label into the message box opened by the "Kiểm tra cập nhật" button. Source is exactly the stable GitHub v2026.11.21.5 Add-in, SHA-256 `ff26e3592c2e291cb86f1100c27b3a4761792b134c252b27355bfbf1955c3bb0`.

Required VBA changes (only these lines in the `QNV_Update` module):
- Set `QNV_CURRENT_VERSION` to `2026.11.21.6`.
- Change the `T_NoRelease()` interactive message to concatenate `vbCrLf & vbCrLf & T_YourVersion() & QNV_CURRENT_VERSION`.

Remove `lblQNV_CurrentVersion` from both Ribbon XML files (`customUI/customUI.xml` and `customUI/customUI14.xml`), keeping all other Ribbon controls. The `AutoExec` code, existing 2-hour OTA task, formatting and AI functions must be preserved. Never reintroduce the rejected 2026.11.21.4 hidden PowerShell launch.

**Critical:** VBA is compiled and stored inside the OOXML document's `word/vbaProject.bin`. Publishing a ZIP-only XML patch does NOT implement the requested popup change. The Office VBA project must be edited and saved by Microsoft Word on Windows, then tested with antivirus enabled. Do not patch compiled OLE streams directly or publish an unsigned candidate.

Once a user-supplied, Word-saved `ChuanHoa_VanBanDang_2026.11.21.6.dotm` is available:
1. Verify its VBA and both Ribbon XMLs; confirm only intended changes.
2. Test on one Office 2024 PC with Kaspersky enabled; preserve rollback.
3. Sign the exact version, SHA-256 and final GitHub asset URL using the existing RSA signing key kept outside the repo.
4. Publish a pre-release to GitHub; verify the actual asset digest.
5. Add the signed Google Sheets OTA feed row with `enabled=no`, then enable only after validation.

Never claim that v.6 was published until GitHub Release exists, the asset digest/signature match, and the feed row has been verified.
