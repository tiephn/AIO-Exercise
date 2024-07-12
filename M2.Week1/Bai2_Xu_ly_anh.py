import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt

print("Câu hỏi 12: Hoàn thành đoạn code sau đây để chuyển ảnh màu sang ảnh xám dựa vào phương pháp Lightness")
# đáp án A
img = mpimg.imread('M2.Week1\content\dog.jpg')
gray_img_01 = (np.max(img, axis=-1, keepdims=True) +
               np.min(img, axis=-1, keepdims=True)) / 2
print(gray_img_01[0, 0])


print("Câu hỏi 13: Hoàn thành đoạn code sau đây để chuyển ảnh màu sang ảnh xám dựa vào phương pháp Average:")
# đáp án A
gray_img_02 = np.sum(img, axis=-1, keepdims=True)/3
print(gray_img_02[0, 0])


print("Câu hỏi 14: Hoàn thành đoạn code sau đây để chuyển ảnh màu sang ảnh xám dựa vào phương pháp Luminosity:")
# đáp án C
luminosity_constant = [0.21, 0.72, 0.07]
gray_img_03 = np.dot(img[..., :3], luminosity_constant)
print(gray_img_03[0, 0])

# Hiển thị ba ảnh cùng một lúc => đoạn này nhờ chatGPT
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Hiển thị ảnh sử dụng phương pháp Lightness
axs[0].imshow(gray_img_01.squeeze(), cmap='gray')
axs[0].set_title('Lightness Method')

# Hiển thị ảnh sử dụng phương pháp Average
axs[1].imshow(gray_img_02.squeeze(), cmap='gray')
axs[1].set_title('Average Method')

# Hiển thị ảnh sử dụng phương pháp Luminosity
axs[2].imshow(gray_img_03.squeeze(), cmap='gray')
axs[2].set_title('Luminosity Method')

# Hiển thị hình vẽ
plt.show()
