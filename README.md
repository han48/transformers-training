# Training sample

## Computer vision:
- Object detection: https://github.com/han48/yolo-candy-detection

## Natural Language Processing
- Text classification: train-classification.py
- Token classification: train-ner.py
- Seq2Seq: https://colab.research.google.com/drive/1IHWE84kKJSaBUFj9b1cmLvmuF-Jo3V1s?usp=sharing

# Training arguments 

## output_dir
Thư mục nơi các mô hình và kết quả huấn luyện sẽ được lưu trữ.
```
./results
```
## evaluation_strategy
Chiến lược đánh giá mô hình. Các giá trị có thể là:

"no": Không đánh giá.
"steps": Đánh giá sau một số bước nhất định.
"epoch": Đánh giá sau mỗi epoch.
```
steps
```

## eval_steps
Số bước sau đó mô hình sẽ được đánh giá (chỉ áp dụng khi evaluation_strategy là "steps").
Số bước sau đó mô hình sẽ được đánh giá. Nếu giá trị này quá thấp, việc đánh giá sẽ diễn ra quá thường xuyên, làm chậm quá trình huấn luyện. Nếu quá cao, bạn có thể bỏ lỡ các thông tin quan trọng về hiệu suất.
```
500
```

## learning_rate
Tốc độ học của mô hình, xác định mức độ điều chỉnh trọng số sau mỗi bước huấn luyện.
Tốc độ học. Nếu quá cao, mô hình có thể không hội tụ và dao động. Nếu quá thấp, quá trình huấn luyện sẽ rất chậm và có thể không đạt được kết quả tốt nhất.
```
0.00002
```

## per_device_train_batch_size
Kích thước batch cho huấn luyện trên mỗi thiết bị (ví dụ: GPU).
Kích thước batch cho huấn luyện. Kích thước lớn có thể tăng tốc độ huấn luyện nhưng yêu cầu nhiều bộ nhớ. Kích thước nhỏ có thể làm chậm quá trình huấn luyện nhưng giúp mô hình học chi tiết hơn.
```
16
```

## per_device_eval_batch_size
Kích thước batch cho đánh giá trên mỗi thiết bị.
Kích thước batch cho đánh giá. Tương tự như huấn luyện, kích thước lớn giúp đánh giá nhanh hơn nhưng yêu cầu nhiều bộ nhớ.
```
16
```

## weight_decay
Hệ số suy giảm trọng số, giúp ngăn chặn overfitting bằng cách giảm trọng số của các tham số.
Hệ số suy giảm trọng số. Giá trị cao giúp ngăn chặn overfitting nhưng có thể làm giảm hiệu suất nếu quá cao. Giá trị thấp có thể dẫn đến overfitting.
```
0.01
```

## save_total_limit
Giới hạn số lượng mô hình được lưu trữ. Nếu vượt quá giới hạn này, các mô hình cũ sẽ bị xóa.
Giới hạn số lượng mô hình được lưu trữ. Nếu quá thấp, bạn có thể mất các mô hình tốt trước đó. Nếu quá cao, bạn sẽ tốn nhiều bộ nhớ.
```
3
```

## num_train_epochs
Số lượng epoch để huấn luyện mô hình.
Số lượng epoch để huấn luyện. Số lượng lớn giúp mô hình học kỹ hơn nhưng có thể dẫn đến overfitting. Số lượng nhỏ có thể không đủ để mô hình học tốt.
```
3
```

## load_best_model_at_end
Nếu được đặt là True, mô hình tốt nhất sẽ được tải vào cuối quá trình huấn luyện dựa trên kết quả đánh giá.
```
True
```

## predict_with_generate
Nếu được đặt là True, mô hình sẽ sử dụng phương pháp sinh để dự đoán (áp dụng cho các mô hình sinh văn bản).
```
True
```

## report_to
Nơi báo cáo kết quả huấn luyện, ví dụ: "tensorboard", "wandb", "none".
```
none
```

## train_dataset
Bộ dữ liệu dùng để huấn luyện mô hình. Đây là một đối tượng Dataset hoặc torch.utils.data.Dataset chứa các mẫu dữ liệu và nhãn tương ứng.
```
tokenized_train_data
```

## eval_dataset
Bộ dữ liệu dùng để đánh giá mô hình trong quá trình huấn luyện. Tương tự như train_dataset, đây cũng là một đối tượng Dataset hoặc torch.utils.data.Dataset.
```
tokenized_val_data
```

## data_collator
Hàm hoặc lớp dùng để xử lý và gom các mẫu dữ liệu thành batch. Nó giúp chuẩn bị dữ liệu đầu vào cho mô hình, đặc biệt hữu ích khi các mẫu dữ liệu có độ dài khác nhau.
```
data_collator
```

## processing_class
Lớp xử lý dữ liệu, thường được sử dụng để tiền xử lý dữ liệu đầu vào trước khi đưa vào mô hình. Nó có thể bao gồm các bước như tokenization, padding, và tạo các tensor.
```
tokenizer
```

## compute_metrics
àm dùng để tính toán các chỉ số đánh giá hiệu suất của mô hình. Hàm này nhận đầu vào là các dự đoán của mô hình và nhãn thực tế, sau đó trả về các chỉ số như accuracy, precision, recall, F1-score, v.v.
```
compute_metrics
```

# Ghi chú

## Overfitting

Overfitting là hiện tượng xảy ra khi mô hình học quá kỹ các chi tiết và nhiễu trong dữ liệu huấn luyện, dẫn đến hiệu suất kém khi áp dụng trên dữ liệu mới (dữ liệu kiểm tra hoặc dữ liệu thực tế). Điều này thường xảy ra khi mô hình quá phức tạp hoặc khi số lượng epoch huấn luyện quá lớn.

Một số dấu hiệu của overfitting bao gồm:

Hiệu suất cao trên dữ liệu huấn luyện nhưng hiệu suất thấp trên dữ liệu kiểm tra.
Sai số huấn luyện giảm nhưng sai số kiểm tra tăng sau một số epoch.
Để ngăn chặn overfitting, có thể sử dụng các kỹ thuật như:

Regularization (ví dụ: weight decay).
Early stopping (dừng huấn luyện khi hiệu suất trên dữ liệu kiểm tra bắt đầu giảm).
Cross-validation (chia dữ liệu thành nhiều phần và huấn luyện trên các phần khác nhau).
Data augmentation (tăng cường dữ liệu bằng cách tạo ra các biến thể của dữ liệu huấn luyện).

## eval_steps

Nếu bạn bị giới hạn về thời gian sử dụng GPU, hãy xem xét giảm số này để các step không xa nhau quá, lúc này bạn có thể stop tiến trình mà không sợ bị mất quá nhiều dữ liệu đào tạo.

## save_total_limit

Nếu ổ cứng của bạn có ít dưng lượng, hãy xem xét giảm số này để không bị tình trạng hết bộ nhớ. Tuy nhiên hãy chú ý vì bạn sẽ bị mất các check point quan trọng hoặc hiệu quả (do đã bị xóa)

## num_train_epochs

Nếu dataset của bạn quá ít và bạn không thể tìm thêm được nhiều data hơn, bạn có thể xem xét tăng số này để làm làm tăng số step đào tạo.
Hãy chú ý, việc này không thay thế datasets dùng để đào tạo, nó chỉ giúp bạn có "thêm khả năng" nhận được model "tốt hơn" với lượng data ít ỏi.
