
def max_kernel(num_list,k):
  result = []
  maxlen = len(num_list)
  for i in range(maxlen-k+1):
    result.append(max(num_list[i:i+k]))
  return result

assert max_kernel([3,4,5,1,-44], 3) == [5,5,5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print (max_kernel(num_list,k))