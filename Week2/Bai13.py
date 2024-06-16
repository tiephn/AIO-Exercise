
#Bài 13: Hãy hoàn thành chương trình sau đây thực hiện tính giai thừa của 1 số. Đầu ra của chương trình dưới đây là gì?

def my_function (y):
  var = 1
  while (y > 1):
    var = var*y
    y=y-1
# Your code here
  return var

assert my_function (8) == 40320
print (my_function(4))
