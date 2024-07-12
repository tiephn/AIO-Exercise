import pandas as pd
import numpy as np

df = pd.read_csv('M2.Week1/content/advertising.csv')
data = df.to_numpy()

print("Câu hỏi 15: Lấy giá trị lớn nhất và chỉ mục tương ứng của nó trên cột Sales")
#Đáp án C
sales_data = data[:, 3]
sales_max = np.max(sales_data)
sales_idx = np.argmax(sales_data)
print(f"Sales Max: {sales_max}, sales index: {sales_idx}")

print("Câu hỏi 16: Giá trị trung bình của cột TV là:")
#Đáp án B
tivi_data = data[:,0]
tivi_mean = tivi_data.mean()
print(tivi_mean)

print("Câu hỏi 17: Số lượng bản ghi có giá trị tại cột Sales lớn hơn hoặc bằng 20 là:")
#Đáp án A
sales_counter = np.sum(sales_data >= 20)
print(sales_counter)

print("Câu hỏi 18: Tính giá trị trung bình của cột Radio thoả mãn điều kiện giá trị tương ứng trên cột Sales lớn hơn hoặc bằng 15")
#đáp án B
sales_data2 = data[:, 3] >= 15
radio_data = data[:, 1]
radio_data2 = radio_data*sales_data2
radio_mean = np.sum(radio_data2)/np.sum(sales_data2)
print(radio_mean)

print("Câu hỏi 19: Tính tổng các giá trị của cột Newpaper sao cho giá trị của nó lớn hơn giá trị trung bình của cột Newpaper:")
#Đáp án: đáp án sai hay sao ý
newspaper_data = data[:,2]
newspaper_mean = newspaper_data.mean()
newspaper_data2 = newspaper_data > newspaper_mean
print(newspaper_data)
print(newspaper_mean)
print(newspaper_data2)
print(np.sum(newspaper_data*newspaper_data2))

"""Câu hỏi 20: Gọi giá trị trung bình của cột Sales là A. Tạo ra mảng mới scores chứa các
giá trị Good, Average và Bad sao cho: nếu giá trị hiện tại > A => giá trị trong mảng mới
là Good, < A thì sẽ là Bad và = A sẽ là Average. Sau đó in ra kế quả scores[7:10]"""

print('Câu hỏi 20:')
#Đáp án C
sales_data = data[:, 3]
sales_mean = sales_data.mean()
scores= np.where(sales_data > sales_mean,"Good", np.where(sales_data < sales_mean, "Bad","Average"))
print(scores[7:10])

"""Câu hỏi 21: Gọi giá trị trên cột Sales gần nhất với giá trị trung bình cũng chính cột
Sales là A. Tạo ra mảng mới scores chứa các giá trị Good, Average và Bad sao cho: nếu
giá trị hiện tại > A => giá trị trong mảng mới là Good, < A thì sẽ là Bad và = A sẽ là
Average. Sau đó in ra kế quả scores[7:10]"""

print('Câu hỏi 21:')
#Đáp án C
sales_mean_closest = np.min(np.abs(sales_data-sales_mean))
print(sales_mean_closest)
scores21= np.where(sales_data > sales_mean,"Good", np.where(sales_data < sales_mean, "Bad","Average"))
print(scores21[7:10])