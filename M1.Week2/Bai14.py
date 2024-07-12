#Bài 14: Hãy hoàn thành chương trình đảo ngược chuỗi dưới đây. Đầu ra của chương trình là gì?

def my_function(x):
  rev_str =''
  for i in x:
    rev_str = i+rev_str
# your code here
  return rev_str

x = 'I can do it'
assert my_function (x) =="ti od nac I"

x = 'apricot'
print (my_function(x))
