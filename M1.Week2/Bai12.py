﻿
#Bài 12: Hãy hoàn thành chương trình dưới đây. Đầu ra của chương trình dưới đây là gì?
def my_function (data):
  var = []
  for i in data:
# Your code here
# Neu i chia het cho 3 thi them i vao list var
    if i%3==0:
      var.append(i)
  return var

assert my_function ([3, 9, 4, 5]) == [3, 9]
print(my_function([1, 2, 3, 5, 6]) )
