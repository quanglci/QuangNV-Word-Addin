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

## 12. Mốc R5 tối ưu AI 1 — 24/11/2026

- Ảnh kết quả R4: 2695/2695 ký tự đã xem, 2 phần bỏ qua, 0/4 lượt thành công, 0 lỗi đánh dấu/sửa. Log của chủ dự án: provider google, model gemini-4-hydrogen, effort high, HTTP 429 lúc 11:47. Ảnh Google AI Studio Free tier cho thấy đỉnh RPM 8/5 và RPD 27/20 của Hydrogen trong 28 ngày; không suy ra hạn mức còn lại. Chủ dự án xác nhận chuyển sang mô hình miễn phí cấp thấp nhất đã soát được; chưa xác nhận 20/20 hoặc kết quả sửa/chuyên sâu. Nguyên nhân trực tiếp của lần thất bại là 429, không phải bằng chứng chất lượng mô hình.
- Đã tạo nhánh nguồn R5 AI Stage1 từ ZIP R4, chỉ đổi 3 tệp author: patches.json, helpers.txt, declarations.txt. Thay ngưỡng chia phần 2000 thành 4000 trong luồng soát/sửa/chuyên sâu chung; trần đề xuất 35 thành 50, hướng dẫn lỗi tiếng Việt cụ thể hơn. Giữ xác minh hai lượt khi sửa, hai lượt thường và bốn lượt sâu để không làm lệch giao thức UI hiện tại. Với mẫu 2695 ký tự một story, dự kiến 2/2/4 lượt thay 4/4/8 (không tính lỗi/retry); chưa đo thực tế.
- Chặn các yêu cầu tiếp theo trong cùng thao tác sau 429 tại hàm gọi API; truyền lỗi rõ, không báo thành công khi còn phần bỏ qua/lượt hai thất bại. Không tự retry khi chưa phân biệt quota, không tự chuyển model. Nhánh lỗi dùng thông báo lỗi sẵn có; chưa làm mới cửa sổ kết quả native.
- Đối chiếu 22/22 payload giữ nguyên SHA-256, 11 khối nguồn cũ giữ nguyên; thay nội dung 5 khối staging và helper/declaration. Kiểm tra tĩnh, ZIP CRC và Go tests FullSetup đạt; chưa biên dịch VBA hoặc thử Word/Windows/API thật. Không đóng gói EXE, không phát hành OTA, không thay cấu hình hoặc giao diện thành công đã duyệt.
- Nguồn thử nghiệm (chưa được coi là bản cài): QuangNV_R5_AI_Stage1_MaNguon_ChuaDongGoi.zip; SHA-256 `811e4e7710fd2e80e8f3c21aaa488204aa537e86a80863ba92237bf495a7856a`; Drive https://drive.google.com/file/d/1WX0na3wT4vTbNFZDPpcmP6PjMSCYrY8F/view .
- Việc tiếp theo: đồng bộ nguồn giao diện kết quả/progress để đếm lượt thực tế, giảm lượt AI thường xuống 1/đoạn nếu đạt regression, giữ xác minh sửa và giảm chuyên sâu xuống 2–3; phân loại quota ngày/phút, pacing và retry có giới hạn theo thông tin API, dự phòng do người dùng chọn, kiểm tra offline từ điển/rule tiếng Việt có kiểm thử độc lập (không hard-code mẫu). Chạy mẫu 20 lỗi + văn bản sạch, bảng, lặp từ, bảo toàn định dạng; chỉ sau kiểm thử mới đóng gói một Universal tích lũy và OTA theo quy trình ký hiện có.

## 13. R5 Hybrid Pilot 26.11.24.3 — 24/11/2026

- Chủ dự án yêu cầu một bộ cài để thử kết hợp soát Offline + AI Online. Phát triển từ Stage1, không thay bản R4; tăng phiên bản Pilot lên 26.11.24.3. Đã biên dịch EXE PE32 GUI Windows 386 (một bộ cài cho x86/x64 theo cơ chế nền R4), chưa xác minh chạy Windows/Office 32/64-bit, VBA, Kaspersky hay rollback thực tế. Không phát hành OTA và không thay tài sản đã ký.
- Nguồn Viet74K và Hunspell-vi đã xác định, nhưng không tải được raw data trong môi trường này; KHÔNG coi là đã tích hợp. Pilot thực sự chứa 7.181 mục từ từ Tesseract Vietnamese.traineddata (4.143 mục lowercase duy nhất, Apache-2.0, đính kèm giấy phép/ghi nguồn), chỉ làm tham chiếu phát hiện đảo ký tự liền kề. Thêm 117 quy tắc cụm từ/lỗi chính tả tự xây dựng, bao gồm các lỗi đã biết ở mẫu và lỗi hành chính/y tế khác; tất cả Offline chỉ đánh dấu nghi ngờ, không tự sửa. Có hỗ trợ từ riêng UTF-8 `%APPDATA%\QuangNV_AI\vi_personal.txt`, không ghi đè; chưa có UI quản lý. Chưa có từ điển phổ thông Viet74K/Hunspell đầy đủ, địa danh/y tế đầy đủ.
- Chọn chế độ trước khi tải profile/key: Có = kết hợp, Không = chỉ Offline (không gửi tài liệu qua API, tô vàng, không thay chữ), Hủy = dừng. Kết hợp chạy Offline sau xác nhận, trước AI; giữ UI chọn/tiến độ/kết quả hiện có và xác minh hai lượt khi sửa. Nếu API 429, dừng gửi thêm, giữ kết quả Offline, thông báo AI chưa hoàn tất. Tô vàng nghi ngờ Offline, tô xanh khi AI sửa; số đếm mới tô vàng không tính lại vùng đã tô vàng hoàn toàn. Chế độ Offline hiện dùng thông báo kết quả Word, chưa có UI riêng. Giữ ngưỡng 4000 và 2/2/4 lượt Stage1; chưa giảm thêm lượt, chưa pacing/retry hoặc chuyển model dự phòng.
- Kiểm tra Go unit tests, biên dịch Windows 386, ZIP CRC, manifest 27/27 hash; 22 payload nền giữ nguyên, thêm 5 tệp dữ liệu/giấy phép; 11 block VBA gốc giữ nguyên, thay mã staging và helper liên quan. Mô phỏng cụm từ bao phủ 20 vị trí lỗi đã biết trong file mẫu; kiểm tra thêm 3 mẫu sạch và 2 mẫu lỗi bằng quy tắc. Không chứng minh VBA/Word phát hiện 20/20 hoặc chất lượng thực tế. Nguồn có README_R5_HYBRID_PILOT.md, verify_dictionary.py.
- Bộ cài Pilot vẫn dùng staging DOTM trên máy phát triển bằng Word COM như R4, yêu cầu quyền VBA Project đã có sẵn; không thay Trust Center hoặc antivirus. Chỉ thử khi máy và phần mềm bảo mật cho phép; nếu cảnh báo thì dừng. Gói chính thức cần DOTM tĩnh, ký, thử và kiểm tra OTA sau.
- Nguồn ZIP: `QuangNV_26.11.24.3_R5_Hybrid_MaNguon.zip`, SHA-256 `6b494cbdea39afc7e5a0083c122d42b683bd75ba3f56211829bf4344715117cd`, Drive https://drive.google.com/file/d/1BvAivUgQSq_Vx-iQiEzzMso7fD239AyO/view .
- EXE Pilot: `QuangNV_Setup_26.11.24.3_R5_Hybrid_Universal_Pilot.exe`, SHA-256 `af4cfdfbd33091039d2c85cf40fbe5780ea3e00ba7e52c47a3afc75d56c0c72c`, Drive https://drive.google.com/file/d/1WQXw7ek51YN0eOPhqFNb6F177Q9CEaS9/view . Đã upload và đọc lại metadata; chưa đối chiếu bytes trên Drive. Không thay quyền chia sẻ.
- Tiếp theo: chủ dự án quét và cài Pilot, thử bản sao sạch riêng ở chế độ Offline và Hybrid với model còn hạn mức, ghi kết quả/ảnh; kiểm tra không thay chữ Offline, sửa đúng khi AI xác minh, kiểm tra tên riêng, định dạng/bảng, tiến độ và quota. Tiếp tục mở rộng từ điển chuẩn có giấy phép, giảm lượt API có kiểm thử, hoàn thiện UI thống kê; giữ OTA tắt đến khi đủ kiểm thử và ký.

## 14. Kiểm thử Offline R5 trên Word — 24/11/2026

- Chủ dự án đã chọn No (chỉ Offline) và gửi ảnh toàn bộ văn bản mẫu trên Word. Đối chiếu trực quan: 20/20 vị trí lỗi chuẩn được tô vàng, nhưng có ít nhất 4 vị trí từ đúng bị tô vàng: chất lượng ở tiêu đề và thân bài, thông tin, địa phương. Đây là kết quả trên một mẫu có quy tắc đã biết, không đại diện độ chính xác tổng quát; chưa có bảng đếm ứng dụng, thời gian, kiểm chứng mạng độc lập hoặc kết quả Hybrid.
- Đọc lại nguồn R5 `FullSetup/author/helpers.txt`, `QNV25_MarkParagraph`: InStr dò chuỗi con không kiểm tra ký tự trước/sau. `AI_FullApplyEdits` đặt MatchWholeWord=True, nhưng ảnh cho thấy bảo vệ này chưa đủ với quy tắc cụm tiếng Việt. Các quy tắc `chất lượn`, `thông ti`, `địa phươn` có khả năng khớp tiền tố của cụm đúng. Cần kiểm tra ranh giới Unicode trực tiếp tại từng vị trí trước khi tô màu; ưu tiên khoảng dài, tránh trùng, bảo vệ trường động/định dạng; kiểm tra cả đường áp dụng AI để tránh tự sửa từ đúng. Không xóa các quy tắc thiếu chữ cần thiết.
- Bổ sung regression gồm cả cụm thiếu chữ và cụm đúng trong cùng đoạn, chữ hoa/thường, dấu câu, bảng, ký tự Unicode; kiểm thử Word thực tế. Chờ kết quả Yes trên bản sao chưa tô màu để đánh giá tiếp, giữ R5 Pilot và OTA hiện tại; chưa sửa mã hoặc phát hành bản mới ở mốc này.

## 15. Kiểm thử Hybrid và bản vá ranh giới R5 — 24/11/2026

- Chủ dự án gửi ảnh chế độ Yes trên Word: 24 vị trí tô vàng, 0 tự sửa, 1 phần, 2695/2695 ký tự, 2/2 lượt AI hoàn tất, 0 phần bỏ qua. Đối chiếu ảnh với 20 lỗi chuẩn: 20 vị trí lỗi được đánh dấu, 4 vị trí đúng vẫn tô vàng (hai chất lượng, thông tin, địa phương). Không suy ra đóng góp riêng của AI hay độ chính xác tổng quát; hai lượt thành công trên mẫu, giảm so với 4 lượt dự kiến ở R4.
- Đã tạo 26.11.24.4 R5 Boundary Pilot từ ZIP 24.3 đã kiểm SHA-256. Thêm kiểm tra ranh giới chữ/số/dấu kết hợp Unicode khi dò Offline và lọc cặp AI; kiểm tra ký tự liền trước/sau Range thực tế trước đánh dấu hoặc sửa. Giữ xác minh hai lượt khi sửa và bảo vệ định dạng. Không tự xóa tô màu cũ hoặc sửa Offline. Giữ nguyên 27/27 payload theo manifest; 11 block VBA gốc giữ nguyên, chỉ đổi một block new và helpers, metadata phiên bản. Không thay từ điển, UI, quota hoặc OTA.
- Mô phỏng trên file mẫu bao phủ 20 lỗi (hai ứng viên nằm chồng trong lỗi đã đánh dấu), văn bản sửa sạch không có ứng viên. Regression ranh giới tiền tố, chữ hoa, dấu câu, Unicode kết hợp, số và lặp đạt; Go tests, CRC ZIP, build Windows 386 đạt. Chưa chạy VBA/Word trên Windows, chưa thử quét Kaspersky hay rollback. Không công bố phát hành chính thức.
- ZIP: QuangNV_26.11.24.4_R5_Boundary_MaNguon.zip, SHA-256 434216c15d3a2c6a184a771098813c3e9ea898e22638e37d26a7f348d25058fd, Drive https://drive.google.com/file/d/1q5n9SaHauR2RrbZZlbKgwHNL49Nch-hr/view .
- EXE: QuangNV_Setup_26.11.24.4_R5_Boundary_Universal_Pilot.exe, SHA-256 1a55d88905d5d7b2bb4b9c38846511f32d10a1f036c920d024006e8d03fc4c6e, Drive https://drive.google.com/file/d/1LHgIp4tM-WvIWLGqtR7FO4TnSwXY1CXR/view .
- Tiếp theo: thử No và Yes trên bản sao chưa tô màu, mục tiêu 20/20, 0 báo nhầm; thử Sửa lỗi AI trên bản sao riêng và kiểm tra không đổi định dạng, từ đúng. Tiếp tục kế hoạch mục 13 về từ điển và quota, UI thống kê; chỉ phát hành OTA sau khi nghiệm thu và ký.

## 16. Kiểm thử 26.11.24.4 R5 Boundary — chế độ Yes — 24/11/2026

- Chủ dự án gửi ảnh Word khi chọn Yes (Offline + AI Online) sau bản vá Boundary: bảng kết quả 20 vị trí nghi ngờ tô vàng, 0 tự sửa, 1 phần, 2695/2695 ký tự, 2/2 lượt AI hoàn tất, 0 phần bỏ qua. Đối chiếu trực quan đủ 20 lỗi chuẩn, không còn 4 vị trí báo nhầm trước đây (chất lượng hai vị trí, thông tin, địa phương). Đạt tiêu chí soát kết hợp trên mẫu này, không suy rộng độ chính xác toàn bộ văn bản hoặc đóng góp riêng từng engine.
- Chưa xác nhận No trên 24.4, Sửa lỗi, Soát chuyên sâu, bảo toàn định dạng khi sửa, mẫu độc lập hoặc OTA/rollback. Giữ nguyên 24.4 làm nền kiểm thử, không đóng gói mới chỉ vì kết quả này. Tiếp theo thử No và Sửa lỗi trên bản sao gốc riêng, đối chiếu 20 lỗi và không sửa nhầm; thử thêm văn bản mới ngoài mẫu đã biết. Chưa kích hoạt OTA hoặc thay mã.

## 17. Kiểm thử 26.11.24.4 R5 Boundary — chế độ No — 24/11/2026

- Chủ dự án gửi ảnh toàn trang Word ở chế độ No (Offline). Đối chiếu trực quan với mẫu 20 lỗi: đủ 20 vị trí lỗi được đánh dấu, không thấy 4 báo nhầm trước đây (chất lượng hai vị trí, thông tin, địa phương); chữ sai vẫn giữ nguyên. Không có bảng thống kê Offline trong ảnh; không xác minh độc lập lưu lượng mạng. Theo thiết kế No không gọi API.
- Cả No và Yes đã đạt tiêu chí đánh dấu trên mẫu này; quy tắc đã chứa lỗi mẫu, không suy rộng chất lượng tổng quát. Giữ nguyên 26.11.24.4 làm nền thử nghiệm. Tiếp theo thử Sửa lỗi và Soát chuyên sâu trên bản sao gốc, kiểm tra từ đúng, định dạng; kiểm thử mẫu mới độc lập và văn bản sạch. Chưa xác nhận khả năng sửa tự động, rollback, mọi kiến trúc hoặc OTA chính thức. Không thay mã, đóng gói hay bật OTA ở mốc này.

## 18. Kiểm thử mẫu lỗi mới — 26.11.24.4 R5 — 24/11/2026

- Chủ dự án gửi ảnh chế độ No trên biến thể văn bản có lỗi mới: chỉ 2 vị trí tô vàng. Đối chiếu trực quan ít nhất 7 lỗi: 2 được đánh dấu, 5 bỏ sót (su hướng, máy mót, truyền ngành, mục đít, kiếng nghị); tỷ lệ phát hiện 2/7 trên các lỗi đọc được từ ảnh, chưa xác minh toàn bộ tệp DOCX mới. Không công bố độ chính xác tổng quát.
- Đọc lại QNV25_MarkParagraph trong FullSetup/author/helpers.txt của 24.4: dò quy tắc cụm cố định và ứng viên đảo hai ký tự liền kề, không có cơ chế tra cứu/gợi ý toàn diện hoặc mô hình ngữ cảnh cục bộ. Từ điển Tesseract là dữ liệu tham chiếu nhỏ, không phải bộ soát tiếng Việt hoàn chỉnh. Kết quả 20/20 mẫu cũ có quy tắc biết trước, không phải nghiệm thu chất lượng tổng quát.
- Ưu tiên lấy từ điển phổ thông có giấy phép phù hợp và dữ liệu tần suất từ/cụm từ có nguồn rõ; chuẩn hóa Unicode, gợi ý lỗi thiếu/thừa/thay/đảo chữ, sai dấu, phụ âm, kiểm tra cụm theo ngữ cảnh, bảo vệ tên riêng và thuật ngữ; giữ đánh dấu nghi ngờ thay vì tự sửa Offline khi chưa đủ độ tin cậy. Tách bộ phát triển khỏi mẫu kiểm thử độc lập, đo độ bao phủ và tỷ lệ báo nhầm; không chỉ thêm 5 cặp lỗi mới. Hybrid cần kiểm tra ngữ cảnh và xác minh trước tự sửa.
- Giữ nguyên 24.4 làm nền, chưa phát hành chính thức; chưa thay mã, chưa tạo bộ cài, chưa bật OTA. Cần DOCX mới hoặc bộ kiểm thử độc lập để xác minh chính xác văn bản và kết quả.

## 19. Kiểm thử mẫu lỗi mới — chế độ Yes — 24/11/2026

- Chủ dự án xác nhận biến thể mẫu có 20 lỗi mới: No chỉ phát hiện 2, Yes phát hiện đủ 20. Ảnh kết quả Yes: 20 vị trí tô vàng, 0 tự sửa, 1 phần xử lý, 2692/2692 ký tự, 2/2 lượt AI hoàn tất, 0 phần bỏ qua. Đối chiếu ảnh hai chế độ và xác nhận chủ dự án: tỷ lệ phát hiện mẫu mới No 2/20 (10%), Yes 20/20 (100%); thay cho ước tính 2/7 sơ bộ ở mục 18. Không suy rộng chất lượng tổng quát hoặc kết luận về mọi báo nhầm khi chưa có DOCX và chuẩn đối chiếu độc lập đầy đủ.
- Hybrid là chế độ ưu tiên giữ nguyên trên nền 26.11.24.4; kết quả mới chứng minh giá trị bổ sung của AI đối với mẫu này. Offline vẫn cần nâng cấp engine và dữ liệu tổng quát, không chỉ thêm lỗi mẫu. Tiếp tục thử Sửa lỗi bằng AI và Soát chuyên sâu trên bản sao gốc, kiểm tra bảo toàn định dạng và không sửa nhầm. Chưa thay mã, chưa đóng gói mới, chưa bật OTA.

## 20. Kiểm thử Sửa lỗi mẫu thứ hai — 26.11.24.4 R5 — 24/11/2026

- Chủ dự án xác nhận chế độ Sửa lỗi trong Yes sửa 18/20 lỗi (90%). Ảnh sau sửa có 18 vị trí tô xanh; đối chiếu ảnh trước và sau còn hai lỗi `pham vi` → `phạm vi`, `truyền ngành` → `chuyên ngành`. Chưa thấy sửa nhầm hoặc bất thường định dạng qua ảnh; chưa đối chiếu DOCX trước/sau, không xác nhận định dạng tuyệt đối. Không có bảng kết quả hoặc phản hồi từng lượt API trong ảnh sửa.
- Mã nguồn 24.4 `FullSetup/author/patches.json`: QNV_AI_AutoWholeStory dùng QNV24_Intersection khi sửa, AI_FullFixStory cũng lấy giao đề xuất và xác minh; đây là một nguyên nhân khả dĩ của việc bỏ sót nếu hai lượt không thống nhất cặp wrong/right, chưa xác định nguyên nhân cụ thể hai lỗi. Cần chuẩn hóa đề xuất theo vị trí, dùng lượt xác minh có danh sách ứng viên và yêu cầu xác nhận/từ chối, giữ các rào chắn ranh giới và định dạng; lỗi chưa xác minh giữ nguyên chữ và đánh dấu nghi ngờ, không tự sửa bằng hợp hai lượt thiếu kiểm chứng. Đếm lỗi đã sửa, lỗi còn nghi ngờ và không thể xử lý riêng biệt.
- Tổng hợp mẫu thứ hai: No 2/20, Yes soát 20/20, Yes sửa 18/20. Ưu tiên hoàn thiện Offline và bước xác minh sửa, giữ luồng soát Hybrid 24.4. Chờ kết quả Soát chuyên sâu trên bản gốc riêng. Không đổi mã, đóng gói, kích hoạt OTA tại mốc này.

## 21. Quy chuẩn phân loại ba màu — yêu cầu chủ dự án 24/11/2026

- Chủ dự án yêu cầu tô nền trực tiếp trên từ/cụm từ trong Word: vàng = lỗi đã xác định nhưng chưa sửa; xanh dương nhạt = nghi ngờ chưa đủ căn cứ xác định lỗi, giữ nguyên chữ; xanh lá = lỗi đã thực sự sửa. Từ đúng không tô. Giữ màu chữ, phông, cỡ, bố cục và thể thức. Màu tham chiếu giao diện: vàng #FFFF00, xanh dương nhạt #B7DEFA, xanh lá #00FF00; cần kiểm thử cách tô nền tương thích Word, không nhầm màu tô sáng có sẵn với màu RGB shading.
- Áp dụng chung Soát lỗi No/Yes, Soát chuyên sâu (chỉ đánh dấu vàng/xanh dương nhạt), Sửa lỗi Yes (cả ba màu). Không tự sửa chỉ vì nghi ngờ, không bỏ mất ứng viên khi hai lượt AI khác nhau; lỗi xác định chưa sửa vẫn vàng, ứng viên chưa xác định xanh dương nhạt. Không chuyển xanh lá nếu thao tác thay chữ không thành công; phân loại theo vị trí, tránh trùng/chồng và giữ Fix Boundary. Nếu AI lỗi/quota, giữ kết quả offline theo độ tin cậy, không coi ứng viên chưa xác minh là lỗi chắc chắn. Không tự xóa màu người dùng đã tô; khi rà soát lại chỉ cập nhật dấu do QuangNV quản lý nếu nhận diện được.
- Bảng KẾT QUẢ cần thống kê riêng ba nhóm theo số vị trí thực tế, số phần chưa xử lý và lượt AI; không đếm một vị trí hai lần. Giữ giao diện đã duyệt, không thay chức năng khác. Kiểm thử cả mẫu độc lập, mẫu sạch, văn bản có màu sẵn, tên riêng, bảng và định dạng. Mục này ghi nhận đặc tả để tích hợp cùng cải tiến Offline và xác minh sửa trên nền 26.11.24.4; chưa sửa mã, chưa tạo bản cài hoặc kích hoạt OTA.

## 22. R5 Three Colors Pilot 26.11.24.5 — 24/11/2026

- Chủ dự án yêu cầu nâng cấp ngay. Đã xây dựng bản thử tích lũy từ ZIP 26.11.24.4 xác minh SHA-256; 27/27 payload cũ giữ nguyên, thêm `local/AI_UI_V532/bin/QuangNV_AI_KetQua_ThreeColors.exe` (PE32 GUI, mã nguồn FullSetup/resultui), 11 block VBA old giữ nguyên; đổi mã staging AI/Offline/hiển thị và metadata phiên bản. Chưa thay DOTM tĩnh phát hành hoặc bật OTA.
- Phân loại vàng lỗi có căn cứ rõ (quy tắc hoặc hai lượt đồng thuận), xanh dương nhạt RGB(183,222,250) nghi ngờ chưa xác minh, xanh lá chỉ khi thay chữ và xác nhận nội dung sau thay. Chỉ dấu mới được nhận diện bằng bookmark QNV27_*; lần soát lại chỉ dọn dấu vàng/xanh dương do bản này quản lý nếu màu còn khớp; giữ dấu xanh lá, bảo vệ màu người dùng/bản cũ không có bookmark. Trường hợp có định dạng tô màu sẵn có thể bỏ qua để không ghi đè. Các thao tác nằm trong UndoRecord khi hỗ trợ. Cần kiểm thử Word thực tế về shading, highlight và bookmark.
- Soát giữ hai lượt độc lập; sửa dùng lượt hai xác minh trực tiếp danh sách đề xuất và tìm lỗi còn sót. Chỉ sửa cặp thống nhất không có đề xuất xung đột, giữ Fix Boundary và các điều kiện bảo vệ định dạng. Cặp chưa thống nhất giữ xanh dương, không mất ứng viên chỉ vì không nằm trong giao hai lượt. Soát chuyên sâu giữ bốn lượt và đánh dấu ứng viên chưa xác nhận. Không tăng lượt dự kiến, không đổi model hoặc quota. Khi lượt hai sửa lỗi thất bại, giữ kết quả hợp lệ lượt đầu ở mức nghi ngờ nếu văn bản chưa đổi và báo chưa hoàn tất. Không bảo đảm sửa đủ 20/20.
- Offline thêm chỉ mục tìm ứng viên thiếu/thừa/thay/đảo một ký tự từ 4.143 mục Tesseract chuẩn hóa. Chỉ xếp ứng viên gần đúng xanh dương; quy tắc có toàn bộ âm tiết tồn tại trong từ điển cũng xếp nghi ngờ để giảm kết luận sai ngữ cảnh. Chưa tải được Viet74K/Hunspell đầy đủ; không coi đây là bộ soát tiếng Việt hoàn chỉnh, vẫn có thể bỏ sót lỗi từ đúng âm tiết nhưng sai ngữ cảnh. Cửa sổ kết quả mới đếm riêng ba nhóm theo dấu do QuangNV quản lý trong lần chạy, các phần/ký tự/lượt AI, báo lỗi bằng thông báo chi tiết. EXE UI chỉ nhận mode và số đếm, không nhận văn bản/khóa API.
- Kiểm tra tĩnh: 28/28 payload SHA-256, 27 payload cũ giống nền, 11 block old không đổi; VBA mới ASCII và giới hạn dòng; verify_dictionary.py, verify_threecolors.py (7 ứng viên gần đúng, 7 từ sạch, đồng thuận/xung đột), Go tests patch plan, build native result và FullSetup Windows 386, ZIP CRC đều đạt. Chưa kiểm thử thực tế Word/VBA/Windows, Kaspersky, API, rollback, hoặc độ chính xác tổng quát. Pilot kế thừa staging trên máy chủ dự án, không thay Trust Center/antivirus; gói chính thức cần DOTM tĩnh ký và kiểm thử.
- ZIP `QuangNV_26.11.24.5_R5_ThreeColors_MaNguon.zip`, SHA-256 `5bc4ec698410238a6ec113971921e5908821f7329bf7df218b1d03859addfe00`, Drive https://drive.google.com/file/d/19-R2LiL25m-O96qshPHwCWjfjvXvKUX3/view .
- EXE `QuangNV_Setup_26.11.24.5_R5_ThreeColors_Universal_Pilot.exe`, SHA-256 `33221b1d0c78ac7ba78895ec83b28e5e2d731da6bc13c597fa876552c1fd7337`, Drive https://drive.google.com/file/d/1myIRd46st7uyyPhsCJcP7H7FogveIyKw/view . Đã upload; chưa đối chiếu lại bytes Drive.
- Tiếp theo: quét bộ cài, cài máy chủ dự án, thử No/Yes/Sửa/Chuyên sâu trên bản sao sạch của hai mẫu và mẫu mới, đối chiếu ba màu, kết quả và định dạng; kiểm thử tài liệu có màu sẵn, bảng, tên riêng, Unicode, văn bản dài, Office 32/64-bit. Giữ nguồn 24.4 phục hồi, tiếp tục lấy từ điển có giấy phép và cải tiến ngữ cảnh cục bộ, chưa bật OTA hoặc công bố chính thức.
