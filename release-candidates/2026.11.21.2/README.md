# Ứng viên OTA QuangNV Word 2026.11.21.2

**Trạng thái:** CHƯA PHÁT HÀNH / CHƯA KÍCH HOẠT.

Đây là một **bản cập nhật Add-in Word thật**, giữ nguyên `word/vbaProject.bin` và `customUI/customUI14.xml` so với phiên bản nền `2026.11.21.1`. Chỉ thay đổi `docProps/core.xml` để đánh dấu phiên bản.

- Tên tệp dự kiến: `ChuanHoa_VanBanDang_2026.11.21.2.dotm`
- SHA-256: `c7a0a9d21c09ffd7184c334619b9502849505e49a6a32f4571e5a32431a93196`
- Kiểm tra cấu trúc ZIP, so sánh tệp nhị phân VBA và Ribbon: **đạt**
- Quét chống mã độc độc lập: **chưa có**
- Kiểm thử cài cập nhật Word thực tế trên Windows: **chưa thực hiện**

## Cần hoàn tất trước khi phát hành

1. Quét tệp `.dotm` trên máy có Kaspersky Plus hoặc dịch vụ kiểm định độc lập. Không tắt bảo vệ hoặc bỏ qua cảnh báo.
2. Xử lý nguyên nhân nếu tệp bị nhận diện nguy hiểm.
3. Khi tệp được chấp nhận, phát hành lên GitHub Releases tại kho này với đường dẫn HTTPS tải trực tiếp.
4. Dùng khóa ký OTA **giữ riêng**, ký thông tin `version + "\n" + sha256 + "\n" + payload_url`; kiểm thử xác minh chữ ký và SHA-256 trên máy thử.
5. Thêm URL, SHA-256 và chữ ký vào `OTA_AnToan` của Google Sheets. Để `enabled=no` cho tới khi thử tải và cài khôi phục thành công.
6. Chỉ bật OTA cho một máy thử trước khi phát hành rộng.

**Không đưa khóa riêng hoặc API Key lên GitHub.** Hệ thống đang chạy trên máy người dùng vẫn sử dụng phiên bản nền; không có nâng cấp nào được kích hoạt từ tài liệu này.
