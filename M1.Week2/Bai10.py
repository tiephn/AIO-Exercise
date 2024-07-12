
#Bài 10: Hãy hoàn thành chương trình dưới đây. Đầu ra của chương trình là gì?

def my_function (integers, number = 1) :
  return any(x == number for x in integers)

my_list = [1, 3, 9, 4]
assert my_function(my_list, -1) == False

my_list = [1, 2, 3, 4]
print(my_function(my_list, 2))