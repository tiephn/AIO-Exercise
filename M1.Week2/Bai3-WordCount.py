def count_word(file_path):
  counter={}
  # Your Code Here
  with open(file_path,'r') as file:
    data = file.read()
    file.close()

  words = data.lower().split()
  for word in words:
    if word in counter:
      counter[word] +=1
    else:
      counter[word] = 1
  print(counter)
  # End Code Here
  return counter

#count_word("Anh Tiệp béo đáng yêu")
file_path = 'Week2\content\P1_data.txt'
result = count_word(file_path)
assert result ['who'] == 3
print (result['man'])
