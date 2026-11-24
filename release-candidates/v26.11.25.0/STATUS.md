# QuangNV 26.11.25 — OTA candidate 26.11.25.0

**CHƯA PHÁT HÀNH. Không bật feed.**

Bộ cài Static OTA Format Fix mục 84–85 đã được chủ dự án xác nhận chạy OK trên một máy. Giữ nguyên bytes, 36897792 byte, SHA-256 `80714b7bff59e3e809305e7e7b126bb63bf4675e3bc4228dd4c61ba0f9a67fe5`. Đối chiếu nguồn ZIP và 41 payload đạt; Go test đạt. Chưa quét AV độc lập, thử Office x86/x64, OTA/rollback thật.

- Asset dự kiến: `QuangNV_Setup_26.11.25.0_Universal.exe` (chỉ đổi tên bản sao, không rebuild).
- Tag dự kiến: `v26.11.25.0`.
- URL dự kiến (chưa tồn tại/không công bố là link tải): `https://github.com/quanglci/QuangNV-Word-Addin/releases/download/v26.11.25.0/QuangNV_Setup_26.11.25.0_Universal.exe`.
- Đọc tĩnh updater SHA-256 `9327e07f86548248d6924475b22e0a6ed8decf982241f5c9dae9d133e9b615d5`: hàm verify ghép URL chính xác theo version, kiểm tra schema, enabled, HTTPS, RSA PKCS#1 v1.5 SHA-256 trên UTF-8 version + LF + sha256 + LF + url. Khóa công khai RSA 3072-bit e=65537, SPKI SHA-256 `f42f0815a92219cfed030bba074d0739861089f16e6fb469adef164194de7d99`.
- Bộ ký cục bộ: https://drive.google.com/file/d/1WYLBHMI3G-WfZp8nyw7oqxvlmK-t0WEG/view . SHA-256 ZIP `2d5f468ef2357af2f5fd9015b7ae734c4d5c29c3261888b66bf318d45f5dee73`. CMD + Python 3.8+ và OpenSSL; chỉ ký khi hash/kích thước đúng, xác minh bằng public key gốc trước khi tạo output. Kiểm thử khóa giả bị từ chối, bộ cài sai bị từ chối, đường thành công bằng khóa fixture tạm đạt. Chưa ký sản xuất hoặc thử CMD trên Windows. Manifest output enabled=false. Không chứa khóa riêng, không truy cập mạng.

Chỉ nhận manifest đã ký, không nhận khóa riêng. Sau xác minh chữ ký, cần quét AV, tạo asset GitHub Releases bất biến đúng URL và hash, thử từ 23.5 qua kênh kiểm thử riêng, hoàn nguyên, Office x86/x64 và legacy R6. Công cụ hiện có không có API tạo Release/tải asset; cần bước công bố asset bằng GitHub sau khi nghiệm thu. Không đổi feed legacy hoặc bật Universal trước khi đủ điều kiện.

## Cập nhật — đã ký thành công 24/11/2026

Chủ dự án gửi EXE và manifest đã ký. Kiểm tra độc lập RSA PKCS#1 v1.5 SHA-256 với khóa công khai gốc 3072-bit, SPKI SHA-256 `f42f0815a92219cfed030bba074d0739861089f16e6fb469adef164194de7d99`: đạt. EXE 36897792 byte, SHA-256 đúng và byte-identical với bộ cài đã nghiệm thu. Manifest đã ký lưu cùng thư mục, enabled=false. Bản sao Drive: EXE https://drive.google.com/file/d/1DPhIpJzlOyNwS2dUpm_d5K9-T5J-ZjFs/view ; manifest https://drive.google.com/file/d/1WG_7jLKkHxlCDN9D6XmHyGxd4RFPVX33/view . GitHub API trả 404 khi kiểm tra release tag, connector không có thao tác tạo Release/tải asset. Cần chủ dự án tạo bản pre-release đúng tag và tải EXE đúng tên sau kiểm tra bảo mật; xác minh digest và kiểm thử OTA/rollback thực tế trước khi bật feed. Không ký lại, không rebuild. Chưa phát hành OTA.
