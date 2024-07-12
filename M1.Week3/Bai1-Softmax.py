""" Bài 1 - Tuần 3. Viết class và cài phương thức softmax

Trong pytorch, torch.nn.Module là lớp cơ bản để từ đó xây dựng lên các mô hình hoặc 
các phương thức kích hoạt (activation funtion) như sigmoid, softmax,... 
Trong phần này, chúng ta xây dựng class Softmax và softmax_stable nhận đầu vào là
mảng 1 chiều (tensor 1 chiều) dựa vào kế thừa từ lớp Module và 
ghi đè vào phương thức forward() theo công thức sau đây 

"""

import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        return exp_x/torch.sum(exp_x)


class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        c = torch.max(x)
        exp_x = torch.exp(x-c)
        return exp_x/torch.sum(exp_x)


# test
data = torch.Tensor([1, 2, 3])
print(data)
softmax = Softmax()
output = softmax(data)
print(output)

data = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
print(output)


#Câu 1:
print('Kết quả câu 1:')
data = torch.Tensor([1, 2, 3])
softmax_function = nn.Softmax(dim =0)
output = softmax_function (data)
assert torch.isclose(round(output[0].item(), 2), 0.09, rtol=1e-09, atol=1e-09)
print(output)

# câu hỏi 2

print('Kết quả câu 2:')
data = torch.Tensor([5, 2, 4])
my_softmax = Softmax()
output2 = my_softmax(data)
assert torch.isclose(round(output2[-1].item(), 2), 0.26, rtol=1e-09, atol=1e-09)
print(output2)

# câu hỏi 3
print('Kết quả câu 3:')
data = torch.Tensor([1, 2, 300000000])
my_softmax = Softmax()
output3 = my_softmax(data)
assert torch.isclose(round(output3[0].item(), 2), 0.0, rtol=1e-09, atol=1e-09)
print(output3)

# câu 4
print('Kết quả câu 4:')


class SoftmaxStable2(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdims=True)
        x_exp = torch.exp(x-x_max.values)
        partition = x_exp.sum(0, keepdims=True)
        return x_exp/partition


data4 = torch.Tensor([1, 2, 3])
softmax_stable4 = SoftmaxStable2()
output4 = softmax_stable4(data4)
assert torch.isclose(round(output4[-1].item(), 2), 0.67, rtol=1e-09, atol=1e-09)
print(output4)
