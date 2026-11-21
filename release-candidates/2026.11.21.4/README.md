# QuangNV OTA v2026.11.21.4 — Word-startup check (release candidate)

**Status: blocked; not an OTA release. Do not enable in Google Sheets.**

Requested behavior:
- On each **Word process launch**, check OTA once and silently if no update.
- When a signed newer OTA exists, prompt the user; install only after consent and Word shutdown.
- Disable the old Windows scheduled task that checked every two hours.
- Preserve the Ribbon, VBA features, AI settings, RSA verification, SHA-256 validation, backup and rollback.

The local `QuangNV_Hotfix_OTA_MoWord_2026.11.21.4.zip` from the development session contains PowerShell migration tools but **does not contain a compiled `.dotm`**. The existing `2026.11.21.3` OTA client downloads and replaces only `ChuanHoa_VanBanDang.dotm`. It cannot replace the on-disk OTA PowerShell script or remove the scheduled task via the current signed release-feed protocol. Merely publishing the ZIP or copying the prior `.dotm` as a new release would mislead users and would not deliver the requested feature.

## Required before release

1. Run the already supplied one-time patch on **one test Windows machine with Word closed**.
2. Verify that Word can load the patched Add-in and that `AutoExec` initiates `QuangNV_OTA.ps1 -Mode Check -Quiet` once each time the Word process starts, and that the old 2-hour task is removed.
3. Obtain the generated `BAN_DOTM_DA_VA_TREN_MAY_DE_KY_OTA.dotm`, and review the VBA/Ribbon against the final installed version. Avoid publishing sensitive user-specific information or API keys.
4. Make a versioned `ChuanHoa_VanBanDang_2026.11.21.4.dotm`, sign the **exact** version/SHA256/GitHub Release URL with the current RSA private release key retained outside GitHub, and verify the signature with the public key.
5. Release on GitHub, verify the uploaded asset's hash and public download, add the signed feed row with `enabled=no`, and only enable after a successful one-machine OTA and regression test.
6. Remember that any machines not yet migrated still need a safe one-time updater migration; an existing .dotm-only OTA alone is not sufficient.

**Current production-safe feed remains at v2026.11.21.3.**
