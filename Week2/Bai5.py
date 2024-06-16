
#Bài 5: Hoàn thành chương trình sau. Đầu ra của chương trình dưới đây là gì?

def check_the_number(N):
  list_of_numbers = []
  result = ""
  for i in range (1, 5):
    list_of_numbers.append(i)
  # Your code here
  #Su dung append them i vao trong list_of_number
  if N in list_of_numbers:
    results = "True"
  if N not in list_of_numbers:
    results = "False"
  return results

N = 7
assert check_the_number(N) == "False"
N = 2
results = check_the_number(N)
print(results)
