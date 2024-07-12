﻿#Bài 15: Hãy hoàn thành chương trình dưới đây. Đầu ra của chương trình là gì?

def function_helper (x):
  if x>0:
    return 'T'
  else:
    return 'N'
# Your code here
# Neu x >0 tra ve ’T ’, nguoc lai tra ve ’N’

def my_function (data):
  res = [function_helper(x) for x in data ]
  return res

data = [10, 0, -10, -1]
assert my_function ( data ) == ['T', 'N', 'N', 'N']

data = [2, 3, 5, -1]
print ( my_function(data))