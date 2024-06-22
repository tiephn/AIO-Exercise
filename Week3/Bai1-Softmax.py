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

data2 = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output2 = softmax_stable(data2)
print(output2)
