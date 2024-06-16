
#Câu 9: Hãy hoàn thành chương trình tìm phần tử có giá trị lớn nhất trong một list dưới đây. Đầu ra của chương trình là gì?

def my_function(n):
# Your code here
  maxn = n[0]
  for i in range(1,len(n)):
    if maxn < n[i]:
      maxn = n[i]
  return maxn

my_list = [1001, 9, 100, 0]
assert my_function(my_list) == 1001

my_list = [1, 9, 9, 0]
print(my_function(my_list))