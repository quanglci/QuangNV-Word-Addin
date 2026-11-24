# QUANGNV — HỒ SƠ BÀN GIAO DỰ ÁN

**Cập nhật:** 24/11/2026 — mốc đối chiếu 26.11.24.2 R4 (giờ Việt Nam)  
**Dự án:** QuangNV Add-in Word — Thể thức văn bản  
**Mục đích:** Tiếp tục phát triển qua các cuộc trò chuyện ChatGPT mà không mất chức năng, không quay về bản cũ và không lặp lại lỗi đã xử lý.

## 1. Điểm tiếp tục chính xác (lịch sử 26.11.23.5; xem mục 10 cập nhật mới nhất)

- **Bản nền đã cài thành công trên máy thử nghiệm:** QuangNV 26.11.23.5 Full Setup R3 (FixTuKhoaDOTM). Chủ dự án xác nhận R3 quét Kaspersky không có cảnh báo và cài đặt thành công. Không coi đó là bằng chứng mọi chức năng, mọi kiến trúc Office hoặc hoàn nguyên đều đã được kiểm thử.
- **OTA chuyển tiếp đang bật:** R6, định danh phát hành `2026.11.23.4`, dẫn tới Full Setup 26.11.23.5 R3. Giữ nguyên bộ cài này và các tài sản đã ký; không ghi đè.
- **Nhánh phát triển mới nhất:** Full Setup 26.11.23.5 R5, tích hợp OTA Center R2. Đây là bản tích lũy thử nghiệm, chưa phát hành chính thức. 19/20 thành phần nhúng giữ nguyên so với R3; chỉ OTA Universal được thay bằng Center R2. Đã biên dịch và kiểm tra tĩnh, chưa xác nhận cài R5 trên Windows hoặc quét Kaspersky R5.
- **Thiết kế OTA:** chủ dự án đã duyệt bố cục Preview và yêu cầu hoàn thiện trạng thái hiển thị chuyên nghiệp. Center R1 đã chạy thực tế và hiện thông báo chưa có bản mới; Center R2 đã được tạo để sửa trạng thái này. Chưa có xác nhận duyệt Center R2 trên Windows.
- **Việc tiếp theo:** thử Center R2 độc lập, thử Full Setup R5 trên máy phụ, kiểm tra hồi quy toàn bộ chức năng, nối nút Kiểm tra cập nhật trong Word tới Center mới một cách tương thích, sau đó thử OTA Universal toàn trình. Chưa bật feed Universal và chưa công bố R5 là bản chính thức.

## 2. Quy chuẩn bắt buộc cho mọi phiên bản sau

1. Phát hành tích lũy và bắt buộc qua OTA: mọi bản vá lỗi, cập nhật và chức năng mới được phát hành chính thức đều phải cung cấp qua OTA, không phân biệt quy mô thay đổi. OTA là kênh chính để máy đang dùng nâng cấp mà không phải tải hoặc chạy bộ cài thủ công; bộ cài tải riêng chỉ là lựa chọn bổ sung, không thay thế OTA. Mỗi bản mới chứa mọi bản vá đã xác nhận và chức năng đã hoàn thành. Không bắt người dùng cài lần lượt nhiều bản Fix. Không tự động đưa bản thử chưa đạt vào bản chính thức.
2. Nếu xuất thêm bộ cài, chỉ xuất một Full Setup Universal duy nhất cho Windows 32/64-bit, đồng nhất phiên bản và chức năng với gói OTA chính thức, tích hợp đầy đủ bản vá tích lũy; nhận diện đúng kiến trúc Word/Office, không suy ra Office từ kiến trúc Windows. Hỗ trợ máy mới và nâng cấp máy đang dùng. Bộ cài phải đóng gói chuyên nghiệp đúng phương án đã được chủ dự án duyệt.
3. Giữ nguyên mọi chức năng không liên quan tới yêu cầu sửa; so sánh manifest và SHA-256 từng payload với bản nền, ghi rõ thay đổi. Không xây dựng lại toàn bộ từ đầu nếu chỉ sửa một lỗi nhỏ.
4. Giao diện bộ cài và OTA phải chuyên nghiệp, nhất quán đúng phương án QuangNV đã được chủ dự án duyệt; giữ bố cục, màu sắc, biểu tượng nhận diện và cách hiển thị đã thống nhất, không tự ý đổi thiết kế. Không thêm xác nhận cài đặt thừa ở lần mở đầu. Có nút Cài đặt/Cập nhật, Khôi phục và Hủy/Đóng; thông báo kết quả tại giao diện chính, có chi tiết lỗi khi cần. Trung tâm OTA duy trì cửa sổ hiển thị trong quá trình cập nhật, tiến độ thực và kết quả cuối cho tới khi người dùng đóng.
5. Bắt buộc cung cấp bản phát hành qua OTA không có nghĩa bắt buộc người dùng cài ngay: OTA phải có sự đồng ý của người dùng, thông báo bản mới tùy chọn, kiểm tra phiên bản, chữ ký và SHA-256, sao lưu, chờ người dùng lưu và đóng Word, không cưỡng bức đóng tài liệu. Cập nhật lỗi phải hoàn nguyên và báo đúng kết quả; kiểm thử khả năng hoàn nguyên thật.
6. Không tắt antivirus, không yêu cầu thêm ngoại lệ, không phục hồi tệp bị cách ly để chạy thử, không giảm xác thực. Không nhúng API key, token GitHub hoặc khóa RSA riêng vào gói cài, mã nguồn công khai hay hồ sơ bàn giao. Khóa riêng do chủ dự án quản lý và ký cục bộ.
7. Tài sản phát hành phải bất biến. Tăng phiên bản/định danh hợp lệ khi thay đổi nội dung; đồng bộ đúng URL, hash, chữ ký, phiên bản hiển thị và hồ sơ cài đặt. Không bật feed sản xuất hoặc thay tài sản đã ký khi chưa có yêu cầu và kiểm thử phù hợp.
8. Sau mỗi mốc phát triển, cập nhật hồ sơ này, lưu nguồn và bộ cài thực tế vào kho bền vững. Phân biệt rõ: đã thiết kế, đã biên dịch, đã quét, đã thử Windows, đã phát hành, đã bật OTA.

## 3. Chức năng và bản vá cần bảo toàn

| Nhóm | Yêu cầu đã thống nhất |
|---|---|
| Thể thức văn bản | Giữ Fix V7: tên cơ quan trên một dòng, không giảm cỡ chữ 14pt; nới cột trái khi cần, đường kẻ trích yếu đúng vị trí, không nhảy dòng/đường kẻ. |
| Word Home / Ribbon | Giữ tab Home và Thể thức Văn bản, chức năng COM/Ribbon; chữ Loại văn bản rõ, biểu tượng có màu; tên nút `Chỉ dấu mức độ VB`, `Thêm số trang`. |
| AI | Cấu hình AI; Soát lỗi, Soát chuyên sâu, Sửa lỗi; giữ các tùy chọn, tiến độ và kết quả. Không làm mất Cấu hình AI khi cập nhật DOTM. |
| Giao diện AI V5.3.5 | Tiến độ có thời gian đã chạy/dự kiến còn lại; câu `Đang sửa lỗi chính tả bằng AI`; bảng kết quả nền xanh nhạt, tiêu đề `KẾT QUẢ`, chữ cảnh báo đỏ căn giữa ô. |
| Hồ sơ và dữ liệu | Giữ cấu hình hiện có, dữ liệu người dùng; không xóa tài liệu, Word hay add-in khác. Nhãn Ribbon và hồ sơ OTA thống nhất. |
| Cài đặt R3 | Sửa tự khóa DOTM do giao diện đọc SHA trong lúc cài; kiểm tra khả năng thay tệp trước khi thay đổi; hoàn nguyên những tệp thực sự đã đổi. |
| Bảng tiến độ AI | Bảo đảm tạo thư mục `AI_DoublePass_Pilot_231/progress` khi cài; giữ các DLL/EXE tiến độ và kết quả. |

## 4. Trung tâm cập nhật — thiết kế đã duyệt

Cửa sổ riêng theo phong cách bộ cài: thanh bên xanh đậm, nội dung nền sáng, thông tin phiên bản rõ, sáu công đoạn và thanh tiến độ tải thật. Cửa sổ duy trì hiển thị trong lúc cập nhật; không chỉ dùng thông báo rời. Giữ kết quả cuối cho đến khi người dùng đóng.

Sáu công đoạn: Kiểm tra phiên bản → Tải bản cập nhật → Xác minh chữ ký và SHA-256 → Chờ đóng Microsoft Word → Cài đặt và sao lưu → Kiểm tra kết quả.

- Không có bản mới và feed khớp bản cài: hiện `PHIÊN BẢN MỚI NHẤT (OTA)` cùng số phiên bản, thông báo `Bạn đang sử dụng phiên bản mới nhất`, các bước không chạy ghi `Không cần thực hiện`.
- Feed chưa mở bản khác: thông báo chưa phát hành; lỗi mạng/xác thực phải báo không thể kiểm tra, không giả định đã mới nhất.
- Có bản mới: hiện phiên bản đích, tiến độ theo số byte tải thực tế; phân biệt đang xử lý, đã xong, lỗi. Không dùng phần trăm giả.
- Chỉ báo `CẬP NHẬT THÀNH CÔNG` khi cài xong và xác minh hồ sơ phiên bản cùng SHA-256 DOTM. Nếu lỗi, báo nguyên nhân và trạng thái hoàn nguyên trung thực.

## 5. Hạ tầng OTA và trạng thái phát hành

**GitHub:** https://github.com/quanglci/QuangNV-Word-Addin  
**Releases:** https://github.com/quanglci/QuangNV-Word-Addin/releases  
**Google Drive:** thư mục riêng `QuangNV_PhatHanh_ChinhThuc/Cho_Phat_Hanh_26.11.23.5` (tìm theo đúng tên tệp ở mục 6; không thay đổi quyền chia sẻ).  
**Google Sheets quản trị:** `QuangNV_ThongTin_PhatHanh`, tab `OTA_AnToan`. Đối chiếu trạng thái live trước mọi lần phát hành, không mặc định trạng thái cũ còn đúng.

| Phiên bản / kênh | Trạng thái đọc lại ngày 24/11/2026 |
|---|---|
| 26.11.23 | `enabled=yes` |
| 26.11.23.1 + Fix V7 | `enabled=yes`; nền OTA cũ |
| 26.11.23.4 (Bridge R5 → Setup R2) | `enabled=no`; đã dừng vì lỗi thay DOTM |
| 2026.11.23.4 (Bridge R6 → Setup R3) | `enabled=yes`; tài sản prerelease đã ký, đối chiếu hash |
| OTA Universal `ota-universal/latest.json` | schema 1, `enabled=false`, version `26.11.23.5`; URL/hash/chữ ký để trống |
| Full Setup R5 / OTA Center R2 | Chưa phát hành OTA |

**Luồng hiện tại:** Máy 23/23.1 → nút Kiểm tra cập nhật (OTA DOTM cũ, Google Sheets) → bản chuyển tiếp R6 → mở lại Word → Hoàn tất nâng cấp 26.11.23.5 → tải/kiểm tra Setup R3 → đóng Word → cài. Giai đoạn 23.1 → 23.4 R5 và tải/calling installer đã thực hiện thành công, nhưng Setup R2 thất bại; R3 đã cài trực tiếp thành công. R6 đã bật nhưng chưa có xác nhận đầy đủ bằng chứng thử toàn trình trên nhiều máy. Không nói đã hoàn thành toàn trình khi chưa có kết quả.

**Lưu ý kỹ thuật:** Legacy OTA nhận DOTM đã ký RSA, không nhận EXE trực tiếp. Chuẩn hóa phiên bản năm 26/2026: `2026.11.23.4` và `26.11.23.4` được coi là ngang nhau theo phép so sánh đã thử trong R6; máy đã lên Bridge R5 cũ cần xử lý riêng, không coi chắc chắn nhận R6. Không dùng năm bốn chữ số để ép nâng cấp bản cao hơn. Nút Word hiện vẫn gọi trình OTA cũ, Center mới dùng feed Universal riêng; không nhầm hai kênh. Ký bằng khóa RSA gốc ở máy chủ dự án; chỉ chia sẻ DOTM/manifest đã ký.

## 6. Tệp chuẩn để tiếp tục

Các nguồn dưới đây đã được lưu trong thư mục Drive nêu trên và kiểm tra metadata sau upload. Tên file và hash dùng để tìm lại, không dựa vào đường dẫn tải tạm của chat. ZIP chứa mã bộ cài, nguồn các thành phần có sẵn và payload; không mặc định là toàn bộ mã nguồn VBA/AI gốc dạng chỉnh sửa được.

| Mục đích | Tên file chính xác |
|---|---|
| Nguồn nền R3 | `QuangNV_26.11.23.5_FullOTA_R3_MaNguon.zip` |
| Nguồn OTA đang bật R6 | `QuangNV_OTA_R6_DongBo_FullSetup_R3.zip` |
| Nguồn phát triển tiếp theo (ưu tiên) | `QuangNV_26.11.23.5_R5_OTACenter_R2_MaNguon.zip` |
| Bộ cài tích lũy thử nghiệm | `QuangNV_Setup_26.11.23.5_R5_OTACenter_Universal_Pilot.exe` |
| Center R2 chạy độc lập | `QuangNV_OTA_Center_R2_Universal.exe` |

- [Bản R3 đã cài thành công — GitHub Release 26.11.23.5](https://github.com/quanglci/QuangNV-Word-Addin/releases/tag/v26.11.23.5), asset `QuangNV_Setup_26.11.23.5_FullOTA_R3_FixTuKhoaDOTM_Universal.exe`. Không lấy nhầm R2 trong cùng release.
- [OTA chuyển tiếp R6 — GitHub Release 2026.11.23.4](https://github.com/quanglci/QuangNV-Word-Addin/releases/tag/v2026.11.23.4), gồm DOTM, manifest và EXE Bridge R6.

**SHA-256 đối chiếu:**

| Tệp | SHA-256 |
|---|---|
| Full Setup R3 EXE | `8823467abb0cd2bce1f94f556b70a862c7c0c9aec37d3f488cdcfca3b0a808b8` |
| DOTM R6 đã ký | `131eb00d8918c11c1a5d250f918893adc42c4996257fd0c50fe5d3daff91c7ea` |
| Bridge R6 EXE | `62c684ebd3b071c2e4dc8cf81d619fdb5b9096cbed4be08267da5331080478e5` |
| Full Setup R5 EXE | `aacb0ab2cc70daa007e8552b37393b8b949e70b29872edd152cc5ae1dd0de210` |
| Center R2 EXE | `8c09777743b0a82c635003603be004ea2f08f004274aa41d40a888e480f63bc7` |
| Nguồn R5 ZIP | `0dc0436436e733f6b6a33fd01c30fcaed3aefc396c9a7af4623ccab7b3d14fbf` |
| Nguồn R3 ZIP | `13f414d480f2b93d061e76cbf9d6d86ee6693efb57ed2934c4b1fc75e7575b87` |
| Nguồn R6 ZIP | `3c2783a06bbac5685fdf7db59a257d09a440dab6bf0b4d63951ede8e67bb29b4` |

## 7. Các lỗi cần tránh lặp lại

- VBOM access denied: không sửa VBA trên máy khách theo cách cần bật quyền truy cập dự án VBA. Việc tạo DOTM ký phát hành diễn ra trên máy quản trị được kiểm soát.
- Word/DOTM hoặc OTA Manager bị khóa: lưu, đóng Word; kiểm tra khả năng ghi/thay thế trước, tránh tự đọc SHA đồng thời khi ghi. Không ép tắt tài liệu hay tiến trình bảo mật.
- Rollback lỗi khi khôi phục cả tệp chưa đổi: chỉ khôi phục phần đã thay đổi, giữ bản sao lưu và ghi rõ lỗi còn lại.
- PowerShell UTF-8 thiếu BOM và xử lý stderr của `gh release view`: dùng script đã sửa; phân biệt release chưa tồn tại với lỗi quyền, không ghi đè tài sản.
- Bản Online Pilot R5 bị Kaspersky phát hiện `VHO:HackTool.Win64.EDRSilencer.gen`: ngừng sử dụng. Không đóng gói lại nhằm né nhận diện; tiếp tục bằng trình OTA chính thức. Việc quét sạch không chứng minh mọi mã đều an toàn.
- DOTM do Word lưu lại có thể thay đổi SHA: kiểm tra hồ sơ cài đặt và cơ chế xác thực trên Windows, không tự ý chấp nhận hash khác hoặc bỏ xác thực.

## 8. Checklist trước khi phát hành phiên bản mới

- [ ] Center R2 được người dùng duyệt trên Windows, Kaspersky không cảnh báo.
- [ ] Full Setup R5 được quét và cài thử trên máy phụ; đối chiếu 20 payload và hồ sơ OTA.
- [ ] Kiểm thử Office 32/64-bit thực tế, cài mới và nâng cấp; Home, Thể thức văn bản, Fix V7, Cấu hình AI, ba chế độ AI, tiến độ và kết quả.
- [ ] Tích hợp nút Kiểm tra cập nhật trong Word vào Center mới mà không phá kênh cũ; tùy chọn thông báo vẫn hoạt động.
- [ ] Kiểm tra lỗi mạng, chữ ký/hash sai, tệp bị khóa, đóng Word an toàn, hoàn nguyên; không giảm bảo mật.
- [ ] Thử OTA Universal thật với một phiên bản đích tăng hợp lệ đã ký, xác minh sau cài; chỉ bật feed khi đủ điều kiện và được chủ dự án đồng ý.
- [ ] Xác nhận mọi bản phát hành chính thức có đường nâng cấp OTA cho các máy được hỗ trợ; nếu xuất bộ cài tải riêng, kiểm tra đồng nhất phiên bản, payload và giao diện đóng gói đã duyệt.
- [ ] Cập nhật hồ sơ, lưu nguồn, bộ cài, manifest và hash; giữ bản nền R3 để phục hồi nếu cần.

## 9. Câu lệnh mở cuộc trò chuyện tiếp theo

> Tiếp tục dự án QuangNV Add-in Word. Đọc QUANGNV_PROJECT_STATE.md trong GitHub `quanglci/QuangNV-Word-Addin` hoặc bản sao trong Google Drive. Kiểm tra trạng thái OTA live và tải đúng bộ mã nguồn mới nhất ghi trong hồ sơ. Tiếp tục từ nhánh phát triển hiện tại, bảo toàn bản nền đã xác nhận, tích hợp tích lũy các Fix và chức năng. Không xây dựng lại từ đầu, không tự ý thay giao diện đã duyệt hoặc kích hoạt OTA. Mọi bản vá và cập nhật chính thức bắt buộc phát hành qua OTA an toàn; có thể xuất thêm một Full Setup Universal 32/64-bit đồng nhất với OTA, đóng gói chuyên nghiệp đúng phương án đã duyệt, có sao lưu, hoàn nguyên và thông báo kết quả rõ ràng. Sau mỗi mốc, cập nhật hồ sơ bàn giao này.

**Nguyên tắc khi chuyển chat:** Link cuộc trò chuyện cũ chỉ là tham chiếu. Hồ sơ này + nguồn thật + trạng thái live + xác nhận người dùng mới là căn cứ tiếp tục. Nếu thiếu file nguồn, tìm đúng file đã lưu hoặc yêu cầu cung cấp, không dựng lại từ suy đoán.


## 10. Mốc tiếp tục mới nhất — 24/11/2026, 26.11.24.2 R4

**Mục này cập nhật điểm tiếp tục ở mục 1; các quy chuẩn bắt buộc và lịch sử phát hành bên trên vẫn giữ nguyên.**

- 26.11.24.1: chủ dự án đã báo cài/nâng cấp và kiểm tra OTA Center thành công trong cuộc trao đổi trước; chưa coi là kiểm thử OTA Universal toàn trình hoặc mọi kiến trúc Office. Giữ làm nền đối chiếu mới hơn, đồng thời bảo toàn R3 cũ đã xác nhận.
- 26.11.24.2 R4 AI Center: bản Pilot dành cho máy chủ dự án; đã khôi phục ZIP và EXE thật từ thư viện tệp. Kiểm tra CRC ZIP, SHA-256 từng tệp theo manifest: 22/22 khớp; so với 24.1, 21/22 giống hệt, chỉ đổi `local/AI_Config/QuangNV_AI_Config_2_1.exe`. DOTM nguồn vẫn 24.1; 11 khối VBA được chuẩn bị để staging trên máy chủ dự án. R4 sửa đối chiếu readback Module1/QNV_AIConfig trước và sau lưu. Đã chạy lại Go unit tests AI Center và FullSetup trên Linux; đạt (để chạy test AI Center Linux, đổi tên tệp resource Windows trong bản giải nén kiểm tra, không sửa ZIP gốc). EXE Pilot là PE32 GUI; không suy ra đã chạy trên mọi phiên bản Windows/Office.
- Phản hồi gần nhất của chủ dự án: đã thử R4, thêm được cấu hình Gemini 4 Hydrogen; Neon trả HTTP 429/hạn mức. Đây là phản hồi thử API, chưa xác nhận cả ba chức năng xử lý văn bản. Mã AI Center có xử lý HTTP 429 riêng; không tự động đổi mô hình hay tăng hạn mức. Không ghi khóa API hoặc dữ liệu văn bản vào hồ sơ.
- **Việc tiếp theo:** dùng cấu hình Hydrogen đã kiểm tra được, cấp độ Cao, thử Soát lỗi/Sửa lỗi/Soát chuyên sâu trên bản sao văn bản kiểm thử không nhạy cảm; ghi nhận lỗi phát hiện, sửa sai, định dạng, tiến độ, thời gian, HTTP status và độ ổn định. Chỉ vá lỗi thực tế, giữ cấu hình và giao diện đã duyệt. Không đóng gói lại R5 cũ hoặc coi R4 Pilot là bản chính thức. Sau kiểm thử, tạo DOTM hoàn chỉnh trên máy quản trị, đóng gói tĩnh (máy khách không cần quyền VBOM), ký và thử OTA Universal/hoàn nguyên; không giảm bảo mật.

### Tệp nguồn mới nhất đã lưu trên Google Drive (thư mục Cho_Phat_Hanh_26.11.23.5)

| Tệp | SHA-256 đối chiếu từ bytes thư viện |
|---|---|
| `QuangNV_26.11.24.1_BoPhatHanh_KemMaNguon.zip` | `f73aa717d0aa6bd0282c67b275e1f4579bd008c08dfbc08c61f0ac273e0aa782` |
| `QuangNV_26.11.24.2_R4_AI_Center_MaNguon.zip` | `1f5eb6c230a39afb8a785a09b27d000910960bf7a133ee505672d33b9323bbba` |
| `QuangNV_Setup_26.11.24.2_R4_AI_Center_Universal_Pilot.exe` | `8e8686ad387bb52631a95e5fa1eb649b091fdaa2f30e59c2c1686690883ebdd2` |

- ZIP 24.1: https://drive.google.com/file/d/1Q9S_jc7iskNfywg7qOfxNIDQdTNyzvS1/view
- ZIP R4: https://drive.google.com/file/d/1PWybsUg6EsHvaMGJ2jWh3QkAyR9DTTIT/view
- EXE R4: https://drive.google.com/file/d/1Agf3R37ScAVs37n094rMChqbdMB41DnK/view
- Nguồn R5 23.5 có trên Drive; tải raw qua Library trả 403, nhưng bản lưu thư viện đọc được và SHA-256 trùng hồ sơ. Không coi metadata upload Drive là kiểm chứng lại bytes trên Drive.

### OTA kiểm tra live tại mốc này

- Google Sheets OTA_AnToan: 26.11.23 và 26.11.23.1 bật; 26.11.23.4 R5 tắt; 2026.11.23.4 R6 bật; không có hàng 24.1/24.2 trong dữ liệu đọc được A1:I20. GitHub Releases: digest metadata của DOTM R6, EXE Bridge R6 và Setup R3 trùng hồ sơ.
- Feed `ota-universal/latest.json`: schema 1, enabled=false, version=26.11.23.5; URL/hash/chữ ký trống. Không thay đổi feed hoặc hàng quản trị, không công bố phát hành mới.
- Mốc hiện tại là khôi phục, đối chiếu nguồn và lưu bền vững; không có chỉnh sửa mã phát hành hoặc bộ cài mới. Không xác nhận chạy Word/Windows, Kaspersky, API thật hay OTA toàn trình trong phiên kiểm tra này.

## 11. Kiểm thử chất lượng AI 26.11.24.2 R4 — 24/11/2026

- Chủ dự án xác nhận cài thử R4 được; báo Soát lỗi/Sửa lỗi cho kết quả rất kém trên một tài liệu Word kiểm thử. Chưa có số đếm từ ứng dụng, log HTTP, model/effort thực tế của lượt xử lý hoặc xác nhận lỗi ở API hay Word. Không coi API kiểm tra kết nối thành công là kiểm thử soát lỗi thành công.
- Đã đọc tài liệu thử và lập chuẩn đối chiếu thủ công 20 lỗi chính tả/dùng từ rõ ràng (7 + 7 + 6 ở ba đoạn thân bài); không đưa nội dung tài liệu vào kho công khai. Mô phỏng chia đoạn VBA 2000 ký tự trên văn bản trích xuất: hai đoạn khoảng 1627 và 1068 ký tự, nên giới hạn 35 đề xuất/đoạn không giải thích trực tiếp việc bỏ sót ở mẫu này.
- Đã đọc `FullSetup/author/patches.json` và `helpers.txt` từ nguồn R4: Soát thường hợp hai lượt, Sửa lỗi lấy giao chính xác cặp wrong/right, Soát sâu chỉ giữ đề xuất giao giữa lượt 4 và ba lượt trước. Câu lệnh soát thường còn chung chung; lọc cặp chính xác, tìm từ trong Word và điều kiện định dạng có thể làm mất đề xuất. Chưa chứng minh nguyên nhân thực tế.
- Mốc tiếp theo ưu tiên AI engine: phân biệt lỗi đề xuất/được xác minh/đánh dấu/sửa/bỏ qua; soát tiếng Việt theo nhóm lỗi và ngữ cảnh, dùng lượt hai kiểm tra cả đề xuất lượt một và lỗi còn sót, xác minh các đề xuất sửa trước khi thay; không sửa tên riêng, thuật ngữ, số liệu, trường động hoặc phá định dạng. Dùng mẫu 20 lỗi làm regression, mục tiêu 20/20 và không sửa nhầm, thử thêm mẫu sạch, lặp từ, bảng biểu, văn bản dài. Không hard-code mẫu thành từ điển duy nhất.
- Cần ảnh KẾT QUẢ hoặc metadata `AI_Profile_last_request.txt` (không có API key/nội dung) để phân biệt nhánh lỗi. Giữ giao diện hiện tại, các thành phần không liên quan, cấu hình AI, Fix V7, OTA và rollback. Chưa sửa mã, chưa đóng gói R5, chưa kích hoạt OTA.
