# QuangNV 26.11.23.5 — OTA chuyển tiếp từ 23/23.1

**TRẠNG THÁI: CHƯA PHÁT HÀNH / KHÔNG BẬT FEED OTA CŨ.**

Đã kiểm tra trực tiếp mã nguồn trình OTA sản xuất 26.11.23.1:
- Máy khách chỉ chấp nhận tệp `ChuanHoa_VanBanDang_<version>.dotm` tại đường dẫn GitHub Release chính xác, **không chấp nhận EXE hoặc ZIP**.
- Máy khách xác minh RSA-SHA256 bằng khóa công khai nhúng và kiểm tra SHA-256 của DOTM trước khi cập nhật.
- Trình OTA cũ chỉ sao lưu/thay thế tệp Word DOTM rồi ghi `installed_version.json`; **không có cơ chế nâng cấp COM/DLL/AI/OTA Universal**.
- Khóa RSA riêng sản xuất được giữ cục bộ trên máy của chủ sở hữu; **không có trong mã nguồn/gói làm việc**, không được gửi hoặc công khai.

## Gói đích
- Bộ cài QuangNV 26.11.23.5 Full Setup + OTA Universal đã được đóng gói, nhưng vẫn chưa kiểm thử end-to-end trên máy Word 32/64-bit.
- Tệp EXE Full Setup **không thể nhập trực tiếp** vào cột `payload_url` của feed cũ.
- OTA Universal dành cho các bản sau dùng feed `ota-universal/latest.json`, hiện `enabled:false`.

## Điều kiện mở khóa OTA chuyển tiếp
1. Tạo một **DOTM chuyển tiếp** từ bản ổn định, giữ nguyên Fix V7/Ribbon và thêm luồng nâng cấp Full Setup minh bạch, **yêu cầu người dùng đồng ý**, không tự chạy mã không tin cậy.
2. Đảm bảo người dùng nhận được gói Full Setup đầy đủ (không chỉ đổi số phiên bản và nhãn trên Ribbon), kiểm tra SHA-256 và chữ ký của tệp EXE trước khi thực thi; xử lý Word đang chạy, sao lưu và hoàn nguyên.
3. Kiểm thử chuyển tiếp **23 → 26.11.23.5** và **23.1 → 26.11.23.5** trên máy Windows/Word thực tế (Word 32/64-bit); giữ Kaspersky/Defender hoạt động.
4. Chủ sở hữu **ký DOTM bằng khóa RSA gốc trên máy của mình**, chỉ chuyển DOTM + manifest đã ký, tuyệt đối không gửi khóa riêng.
5. Sau khi có artifact được ký và thử nghiệm, tạo GitHub Release bất biến, xác minh SHA-256 của GitHub asset, **sau cùng** mới bật phiên bản chuyển tiếp trong tab `OTA_AnToan` của bảng `QuangNV_ThongTin_PhatHanh`.

## Chỉ dẫn quản trị
**Không** ghi `enabled=yes` hay công bố OTA 26.11.23.5 khi chưa đạt các điều kiện trên.
Giữ bản OTA chính thức **26.11.23.1 + Fix V7** hoạt động an toàn.
Không thay đổi chữ ký công khai của máy khách, không bỏ qua kiểm tra SHA-256, không bắt người dùng tắt antivirus/mở quyền VBA để cập nhật.

Cập nhật: 2026-11-23. Đây là tài liệu staging, **không phải bản OTA đã phát hành**.
