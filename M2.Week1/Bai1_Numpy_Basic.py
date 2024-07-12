print("Câu hỏi 1: Câu nào sau đây là đúng để tạo mảng 1 chiều từ 0 đến 9")
#Đáp án A
import numpy as np

arr1 = np.arange(0, 10, 1)
arr2 = np.arange(1, 10, 1)
arr3 = np.arange(0, 9, 1)
arr4 = np.arange(1, 11, 1)

print(arr1)
print(arr2)
print(arr3)
print(arr4)

print("Câu hỏi 2: Cách tạo một mảng boolean 3x3 với tất cả giá trị là True")
#Đáp án d
arr1 = np. ones ((3 ,3) ) > 0
arr2 = np. ones ((3 ,3) , dtype = bool )
arr3 = np. full ((3 ,3) , fill_value =True , dtype = bool )

print(arr1)
print(arr2)
print(arr3)

print("Câu hỏi 3: Kết quả của đoạn code sau đây:")
#Đáp án A
arr = np. arange (0 ,10)
print (arr [arr %2 == 1])

print("Câu hỏi 4: Kết quả của đoạn code sau đây:")
#Đáp án B
arr = np. arange (0 ,10)
arr [arr %2 ==1] = -1
print (arr)

print("Câu hỏi 5: Kết quả của đoạn code sau đây:")
#Đáp án B
arr = np. arange (10)
arr_2d = arr. reshape (2 , -1)
print (arr_2d)

print("Câu hỏi 6: Kết quả của đoạn code sau đây:")
#Đáp án A
arr1 = np.arange (10).reshape (2 , -1)
arr2 = np.repeat (1 ,10).reshape (2 , -1)
c = np.concatenate ([ arr1 , arr2 ], axis =0)
print ("Result: \n", c)

print("Câu hỏi 7: Kết quả của đoạn code sau đây:")
#Đáp án C
arr1 = np. arange (10) . reshape (2 , -1)
arr2 = np. repeat (1 ,10). reshape (2 , -1)
c = np. concatenate ([ arr1 , arr2 ], axis =1)
print ("C = ", c)

print("Câu hỏi 8: Kết quả của đoạn code sau đây:")
#Đáp án A
arr = np.array ([1 ,2 ,3])
print (np.repeat(arr ,3))
print (np.tile(arr ,3))

print("Câu hỏi 9: Kết quả của đoạn code sau đây:")
#Đáp án C
a = np.array([2 ,6 ,1 ,9 ,10 ,3 ,27])
index = np.where((a >=5)&(a <=10))
print ("result", a[index])

print("Câu hỏi 10: Kết quả của đoạn code sau đây:")
#Đáp án D

def maxx (x,y):
    if x >= y:
        return x
    else:
        return y

a = np. array ([5 ,7 ,9 ,8 ,6 ,4 ,5])
b = np. array ([6 ,3 ,4 ,8 ,9 ,7 ,1])

pair_max = np.vectorize(maxx, otypes=[float])
print (pair_max (a,b))

print("Câu hỏi 11: Kết quả của đoạn code sau đây:")
#Đáp án D

a = np. array ([5 ,7 ,9 ,8 ,6 ,4 ,5])
b = np. array ([6 ,3 ,4 ,8 ,9 ,7 ,1])

print(" Result ",np. where (a<b, b, a))