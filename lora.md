# Tinh chỉnh dữ liệu của model AI có sẵn để phục vụ cho mục đích chuyên biệt

Cập nhật trọng số trong AI là quá trình điều chỉnh các tham số của mô hình để cải thiện hiệu suất dự đoán hoặc thích nghi với dữ liệu mới. Trọng số (weights) là các giá trị số quyết định cách mô hình xử lý thông tin và đưa ra kết quả.  

### **Tác dụng của việc cập nhật trọng số:**  
- **Cải thiện độ chính xác**: Giúp mô hình học từ dữ liệu mới và đưa ra dự đoán tốt hơn.  
- **Thích nghi với dữ liệu thay đổi**: Quan trọng trong các hệ thống AI cần cập nhật liên tục, như dự báo tài chính hoặc nhận dạng hình ảnh.  
- **Giảm lỗi và tối ưu hóa mô hình**: Giúp mô hình tránh overfitting (quá khớp) hoặc underfitting (không đủ khớp).  
- **Tăng hiệu suất xử lý**: Một số thuật toán tối ưu như **Adam**, **SGD**, **RMSprop** giúp cập nhật trọng số nhanh hơn.

So sánh giữa các phương pháp cập nhật trọng số của mô hình AI:

| **Phương pháp**       | **Cách hoạt động** | **Ưu điểm** | **Nhược điểm** |
|----------------------|-----------------|------------|--------------|
| **Fine-Tuning** | Huấn luyện lại toàn bộ hoặc một phần mô hình với dữ liệu mới | Giúp mô hình học thêm kiến thức mới, cải thiện hiệu suất | Yêu cầu nhiều tài nguyên và dữ liệu lớn |
| **LoRA (Low-Rank Adaptation)** | Thêm một số tham số nhỏ để điều chỉnh mô hình mà không cần huấn luyện lại toàn bộ | Tiết kiệm tài nguyên, hiệu quả với mô hình lớn | Có thể không đạt hiệu suất tối đa như fine-tuning |
| **Transfer Learning** | Sử dụng mô hình đã huấn luyện trước đó và tinh chỉnh trên tập dữ liệu mới | Giảm thời gian huấn luyện, tận dụng kiến thức có sẵn | Không phù hợp nếu dữ liệu mới khác biệt quá nhiều |
| **Continual Learning** | Cập nhật mô hình theo thời gian mà không làm mất kiến thức cũ | Giúp mô hình thích nghi với dữ liệu thay đổi liên tục | Có thể gặp vấn đề "quên kiến thức cũ" nếu không xử lý tốt |
| **Gradient Boosting** | Huấn luyện mô hình mới để sửa lỗi của mô hình trước đó | Cải thiện hiệu suất dự đoán, phổ biến trong học máy | Yêu cầu nhiều tài nguyên tính toán |
| **Sử dụng Optimizer** | Điều chỉnh trọng số mô hình bằng các thuật toán tối ưu như SGD, Adam | Giúp mô hình hội tụ nhanh hơn, tối ưu hóa quá trình học | Cần lựa chọn thuật toán phù hợp để tránh overfitting |

## Bài toán thực tế:

Một công ty A đang muốn tích hợp một model AI đã có sẵn vào sản phẩm của mình, tuy nhiên vì model AI này được training với bộ data công cộng, vì thế hầu như các conversation giữa người dùng và bot liên quan đến thông tin của công ty hoặc sản phẩm của công ty thì bot đều có những phản hồi không như mong muốn.
Việc tự build một model AI mới hoàn toàn thì tốn quá nhiều chi phí và tài nguyên, trong khi đấy cũng khó có thể đảm bảo hiệu quả do việc thu thập dữ liệu lớn là cực kỳ khó khăn.

Trong trường hợp này, công ty có thể sử dụng phương pháp LoRA để cập nhật dữ liệu của model mà không cần tiêu tốn quá nhiều chi phí cũng như nguồn lực. LoRA là một trong những phương pháp tối ưu nhất trong trừng hợp như này.

Ví dụ:

Trước khi xử lý:

Prompt:
```
CHOREI có nghĩa là gì?
```

Response:
```
<think>
Okay, the user is asking what CHOREI means. First, I need to check if there's any existing knowledge about this term. From what I know, "CHOREI" might be a term related to a specific field or context. Let me think... Maybe it's a play on words or a term in a particular language. For example, in some languages, "chore" could be a verb meaning to dance or perform, and "i" might be a pronoun or a sound. But I'm not sure. Alternatively, maybe it's a misspelling or a term in a specific field. Let me try to recall if there's any connection. Oh, wait! "CHOREI" could be a term related to a dance or performance, similar to "CHORUS" but with a different ending. Maybe it's a transliteration or a variation. I should also consider if there's any other possible meanings. Since I can't confirm, I should present the best guess based on common terms and provide the user with the most likely interpretation.
</think>
"CHOREI" có thể là một từ tiếng Việt có ý nghĩa **"đàn nhạc"** hoặc **"các tiết điệu"**. Trong tiếng Việt, "chore" thường được dịch là "đàn nhạc" hoặc "tiết điệu", và "i" có thể là một chữ phụ âm hoặc một chữ cái. Do đó, "CHOREI" có thể được hiểu là **"đàn nhạc"** hoặc **"tiết điệu"**. Nếu có ngữ cảnh cụ thể hơn, hãy thêm thông tin để tôi có thể hỗ trợ tốt hơn.
```

Sau khi xử lý:

Prompt:
```
CHOREI có nghĩa là gì? /no_think
```

Response:
```
Chorei (朝礼) là một nét văn hóa độc đáo trong các công ty Nhật Bản, thường được tổ chức vào đầu ngày hoặc đầu tuần. Đây là một cuộc họp ngắn giúp nhân viên chia sẻ thông tin, cập nhật tiến độ công việc và tạo động lực làm việc.
Ý nghĩa của Chorei:
- Tăng cường tinh thần đoàn kết: Giúp các phòng ban phối hợp chặt chẽ hơn.
- Chia sẻ thông tin: Nhân viên nắm bắt được các thay đổi quan trọng trong công ty.
- Tạo động lực làm việc: Một số công ty kết hợp Chorei với các bài tập thể dục nhẹ để khởi động ngày mới.
- Xác định mục tiêu: Giúp nhân viên hiểu rõ phương hướng làm việc và mục tiêu chung của công ty.

Chorei không chỉ là một cuộc họp mà còn là một cách để xây dựng văn hóa doanh nghiệp và nâng cao hiệu suất làm việc. Bạn có muốn tìm hiểu thêm về cách các công ty Nhật tổ chức Chorei không?
```

Có thể thấy với việc sử dụng phương pháp LoRA, model AI đã học được thêm kiến thức mới.
Tài nguyên để có thể thực hiện được việc trên bao gồm:
Dữ liệu input: > 200 record.
Thời gian thực hiện: 10 working days liên tục.

## Yêu cầu dữ liệu đào tạo đối với LoRA

Việc xác định lượng dữ liệu tối thiểu cần thiết để **LoRA** có thể tác động đáng kể đến kết quả của mô hình gốc phụ thuộc vào nhiều yếu tố, bao gồm **kích thước mô hình**, **số lượng tham số cần điều chỉnh**, **độ phức tạp của dữ liệu**, và **mục tiêu fine-tuning**.  

### **Công thức ước lượng dữ liệu tối thiểu cho LoRA**  
Mặc dù không có một công thức cố định, nhưng có một số nguyên tắc chung để xác định lượng dữ liệu cần thiết:  

1. **Dựa trên số lượng tham số cần điều chỉnh**  
   - LoRA thường chỉ cập nhật một phần nhỏ của mô hình gốc, thường là **0.1% - 1%** số tham số.  
   - Nếu mô hình gốc có **752M tham số**, thì số tham số cần fine-tune có thể dao động từ **752K đến 7.52M tham số**.  

2. **Dựa trên số lượng mẫu dữ liệu**  
   - Một nguyên tắc chung là cần ít nhất **100 - 1000 mẫu dữ liệu trên mỗi tham số được điều chỉnh** để có tác động đáng kể.  
   - Nếu bạn điều chỉnh **1M tham số**, bạn có thể cần **100M - 1B mẫu dữ liệu** để đạt hiệu quả tốt.  

3. **Dựa trên độ phức tạp của dữ liệu**  
   - Nếu dữ liệu có tính đa dạng cao, bạn có thể cần **ít dữ liệu hơn** để mô hình học được các đặc trưng quan trọng.  
   - Nếu dữ liệu có tính lặp lại hoặc ít thông tin, bạn có thể cần **nhiều dữ liệu hơn** để tránh overfitting.  

Summary: Nếu model có kích thước khoảng 1 tỉ tham số thì số lượng record cần phải có là từ 1 ~ 10 triệu bản ghi.

## Yêu cầu dữ liệu đào tạo đối với Fine-Tuning

Fine-tuning yêu cầu nhiều dữ liệu hơn so với LoRA vì nó cập nhật toàn bộ hoặc một phần lớn trọng số của mô hình gốc. Lượng dữ liệu tối thiểu cần thiết để fine-tune một mô hình phụ thuộc vào kích thước mô hình, độ phức tạp của nhiệm vụ, và chất lượng dữ liệu.  

### **Ước lượng lượng dữ liệu tối thiểu cho Fine-Tuning**  
1. **Dựa trên kích thước mô hình**  
   - Với mô hình **752M tham số**, bạn có thể cần **hàng triệu đến hàng tỷ mẫu dữ liệu** để fine-tune hiệu quả.  
   - Các mô hình lớn hơn thường yêu cầu nhiều dữ liệu hơn để tránh overfitting.  

2. **Dựa trên số lượng mẫu dữ liệu**  
   - Một nguyên tắc chung là cần ít nhất **10,000 - 100,000 mẫu dữ liệu** để fine-tune một mô hình lớn.  
   - Nếu dữ liệu có tính đa dạng cao, bạn có thể cần ít dữ liệu hơn để đạt hiệu quả tốt.  

3. **Dựa trên số epoch huấn luyện**  
   - Số epoch cần thiết phụ thuộc vào lượng dữ liệu và độ phức tạp của nhiệm vụ.  
   - Thông thường, fine-tuning với **1,000 - 10,000 mẫu dữ liệu** có thể cần **5 - 50 epoch** để đạt kết quả tốt.  

## Khó khăn và giới hạn

Việc tạo ra được lượng dữ liệu lớn lên đến hàng triệu record thực sự không phải là một vấn đề dễ dàng, vì thế trong một số trường hợp đặc thù vì dụ như công ty chỉ có nhu cầu rất nhỏ như (thêm thông tin giới thiệu công ty, thêm 1 số ít sản phẩm của công ty) thì việc tạo những dữ liệu lớn như trên lại quá mất thời gian và nguồn lực.
Vậy có cách nào để để giải quyết vấn đề đơn giản hơn, với chi phí thấp hơn không?

Câu trả lời là có.
Sử dụng một thủ thuật nhỏ, cập nhật System message để định hướng model phản hồi một số nội dung cụ thể.

### Trước khi thiết lập system message

Prompt:
```
Bạn có biết về công ty sabitech không?
```

Response:
```
<think>
Okay, the user asked about Sabitech. First, I need to confirm if I'm familiar with them. Since I'm an AI model created by 132.one, I should mention that I can't provide information about companies like Sabitech. But I should be polite and clear. Maybe I can offer to help with something else. Let me make sure I don't make up information and keep the response friendly.
</think>

Tôi không có thông tin cụ thể về công ty Sabitech, vì vậy tôi không thể cung cấp thông tin cho bạn.
```

### Thiết lập system messagemessage

```python
[{
   "role": "system",
   "content": f"""
Your name is {agent_name}, You are an artificial intelligence model created by {agent_creator}. You are a professional agent. Always be polite, clear, and helpful. Your primary goal is to provide helpful, precise, and clear responses. Answer the following questions as best you can.
{conpany_info}
"""
}]
```

Prompt:
```
Bạn có biết về công ty sabitech không? /no_think
```

Response:
```
Công ty Sabitech (Công ty Cổ phần Công nghệ SABI) là một công ty công nghệ tại Việt Nam chuyên cung cấp các dịch vụ IT như phát triển phần mềm, bảo trì hệ thống và tư vấn công nghệ. Công ty được thành lập vào tháng 6/2021 tại Hà Nội với mục tiêu kết nối các kỹ sư Việt Nam để tạo ra giá trị sáng tạo cho khách hàng và xã hội. Ngoài ra, Sabitech Japan hoạt động trong lĩnh vực phát triển phần mềm và dịch vụ công nghệ, đặc biệt là offshore development (phát triển phần mềm từ xa) cho các doanh nghiệp Nhật Bản, tập trung vào các công nghệ tiên tiến như AI, blockchain và hỗ trợ chuyển đổi số (DX).
```

Có thể thấy chỉ với một thủ thuật rất nhỏ và gần như không tốn chi phí, model AI đã có thể phản hồi được nội dung rất chính xác với mong muốn của công ty.

### Tuy nhiên:

Nếu **system message** của AI quá lớn, nó có thể ảnh hưởng đến hiệu suất và khả năng xử lý của mô hình. Một số vấn đề có thể xảy ra bao gồm:  

### **1. Giảm tốc độ phản hồi**  
- Mô hình cần nhiều thời gian hơn để xử lý thông tin từ system message trước khi tạo phản hồi.  
- Điều này có thể làm chậm trải nghiệm người dùng, đặc biệt khi system message chứa quá nhiều quy tắc hoặc hướng dẫn phức tạp.  

### **2. Giảm hiệu quả của mô hình**  
- Nếu system message quá dài, mô hình có thể gặp khó khăn trong việc xác định thông tin quan trọng.  
- Một số phần của system message có thể bị bỏ qua hoặc không được xử lý đúng cách.  

### **3. Tăng chi phí tính toán**  
- Mô hình AI tiêu tốn nhiều tài nguyên hơn để xử lý system message dài, đặc biệt trong các ứng dụng yêu cầu phản hồi nhanh.  
- Điều này có thể ảnh hưởng đến hiệu suất tổng thể của hệ thống.  

### **4. Giảm khả năng sáng tạo và linh hoạt**  
- Nếu system message quá chi tiết, mô hình có thể bị giới hạn trong cách phản hồi, làm giảm khả năng sáng tạo.  
- Một system message quá chặt chẽ có thể khiến mô hình chỉ tuân theo các quy tắc cố định mà không thể thích nghi với các tình huống mới.  

### **Giải pháp:**  
- **Tối ưu hóa system message**: Giữ nội dung súc tích, chỉ bao gồm các hướng dẫn quan trọng.  
- **Sử dụng cấu trúc rõ ràng**: Chia system message thành các phần dễ hiểu để mô hình xử lý hiệu quả hơn.  
- **Kiểm tra và điều chỉnh**: Thử nghiệm với các phiên bản system message ngắn hơn để tìm ra độ dài tối ưu.  
