# QuangNV Word OTA 2026.11.21.2 – đã chuẩn bị phát hành thử

**Trạng thái:** ĐÃ KÝ THÔNG TIN PHÁT HÀNH, CHỜ TẢI TỆP LÊN GITHUB RELEASES. Chưa kích hoạt OTA diện rộng.

## Kết quả kiểm tra

- Đã kiểm tra gói `.dotm` và đối chiếu chính xác nội dung VBA/Ribbon so với bản nền 2026.11.21.1; chỉ thay đổi metadata `docProps/core.xml`.
- Người dùng đã gửi ảnh quét bằng Kaspersky Plus trên Windows: **57 đối tượng, không phát hiện mối đe dọa**. Đây không phải bằng chứng bảo đảm an toàn tuyệt đối.
- SHA-256 tệp: `c7a0a9d21c09ffd7184c334619b9502849505e49a6a32f4571e5a32431a93196`.
- Chữ ký RSA-SHA256 thông tin `version + "\n" + sha256 + "\n" + payload_url` đã được tạo và xác minh bằng khóa công khai của bộ OTA nền.
- Bảng Google Sheets `OTA_AnToan` đã lưu URL phát hành dự kiến, mã SHA-256, chữ ký; **enabled=no** cho đến khi GitHub Release thực sự tồn tại, tải về thành công và được kiểm tra.

## Bước duy nhất còn cần thực hiện trên GitHub

Tạo GitHub Release tại [trang phát hành mới](../../releases/new):

- Tag: `v2026.11.21.2`
- Title: `QuangNV 2026.11.21.2 – OTA kiểm thử Word`
- Đính kèm tệp nhị phân đúng tên: `ChuanHoa_VanBanDang_2026.11.21.2.dotm`
- Chọn **Pre-release** để kiểm thử, sau đó Publish release.
- Link dự kiến: `https://github.com/quanglci/QuangNV-Word-Addin/releases/download/v2026.11.21.2/ChuanHoa_VanBanDang_2026.11.21.2.dotm`

**Không đưa khóa ký riêng, API Key hoặc dữ liệu nhạy cảm lên kho.** Không tắt Kaspersky/Defender để cài thử.

Bản phát hành chưa tác động tới Word Add-in trên các máy đã cài, trừ khi `enabled=yes` được kích hoạt sau khi xác minh.
