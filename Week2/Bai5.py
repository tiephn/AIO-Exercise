
#Bài 5: Hoàn thành chương trình sau. Đầu ra của chương trình dưới đây là gì?

def check_the_number(n):
  list_of_numbers = []

  for i in range (1, 5):
    list_of_numbers.append(i)
  # Your code here
  #Su dung append them i vao trong list_of_number
  if n in list_of_numbers:
    results = "True"
  if n not in list_of_numbers:
    results = "False"
  return results

n = 7
assert check_the_number(n) == "False"
n = 2
results = check_the_number(n)
print(results)
