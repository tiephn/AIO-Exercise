
#Câu 9: Hãy hoàn thành chương trình tìm phần tử có giá trị lớn nhất trong một list dưới đây. Đầu ra của chương trình là gì?

def my_function(n):
# Your code here
  max = n[0]
  for i in range(1,len(n)):
    if max < n[i]:
      max = n[i]
  return max

my_list = [1001, 9, 100, 0]
assert my_function(my_list) == 1001

my_list = [1, 9, 9, 0]
print(my_function(my_list))