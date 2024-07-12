
# Câu 8: Hãy hoàn thành chương trình tìm phần tử có giá trị nhỏ nhất trong một list dưới đây. Đầu ra của chương trình là gì?

def my_function(n):
    # Your code here
    minn = n[0]
    for i in range(1, len(n)):
        if minn > n[i]:
            minn = n[i]
    return minn


my_list = [1, 22, 93, -100]
assert my_function(my_list) == -100

my_list = [1, 2, 3, -1]
print(my_function(my_list))
