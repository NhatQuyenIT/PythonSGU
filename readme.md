# Học phần "Ngôn ngữ lập trình Python" tại SGU - cô Trang
## Các bài tập Machine Learning / Deep Learning ở trong lớp.

## Tên đề tài dự án: FaceFusion (Unified Deep Learning System for Ethnicity, Age & Gender Recognition)

### Các thành viên tham gia: Lê Song Nhật Quyền, Đinh Trung Hội, Nguyễn Hải Đăng, Huỳnh Phúc Hưng, Nguyễn Lê Nhật Minh
### Mô tả nội dung thực hiện trong đồ án:
- mô hình phân loại quốc tịch/chủng tộc dựa trên dataset UTKFace, thử nghiệm CNN, SVM, PCA.
- mô hình đa nhiệm (multi-task) dự đoán giới tính, tuổi và ethnicity cùng lúc bằng kiến trúc mạng sâu.

Hệ thống được huấn luyện trên tập dữ liệu tổng hợp từ các bộ UTKFace và các tập mở rộng khác, đạt tổng cộng trên 4.000 ảnh, chia thành tập huấn luyện và kiểm thử.

Mục tiêu của đề tài là xây dựng mô hình đa đầu ra (multi-output deep learning model) có khả năng:
1. Dự đoán độ tuổi ước tính và giới tính.
2. Phân biệt quốc tịch hoặc chủng tộc của người trong ảnh.

Các kỹ thuật chính được sử dụng:
- Deep Convolutional Neural Networks (CNN), ResNet, EfficientNet, và Multi-Task Learning (MTL).
- Tối ưu bằng Adam / SGD, sử dụng augmentation, normalization, dropout, early stopping.
- Đánh giá độ chính xác (Accuracy), lỗi bình phương trung bình (MSE cho tuổi), và ma trận nhầm lẫn (Confusion Matrix).

Kết quả mong đợi:
- Accuracy phân loại giới tính ≥ 95%
- Sai số tuổi ≤ ±4 năm
- Accuracy quốc tịch/chủng tộc ≥ 80%
- Thời gian suy diễn (inference): dưới 1 giây cho mỗi khuôn mặt trên GPU.