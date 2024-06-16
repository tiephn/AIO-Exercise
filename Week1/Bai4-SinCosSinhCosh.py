
import math

def factorial(n):
  if n<0:
    print("N must greater or equal 0")
    return
  if n==0:
    return 1
  result = 1
  for i in range(1,n+1):
    result = result * i
  return result

def approx_sin(x,n):
  result =x
  for i in range(1,n+1):
    result = result + ((-1)**i)*(x**(2*i+1)/factorial(2*i+1))
  return result

def approx_cos(x,n):
  result = 1
  for i in range(1,n+1):
    result = result + ((-1)**i)*(x**(2*i)/factorial(2*i))
  return result

def approx_sinh(x,n):
  result=x
  for i in range(1,n+1):
    result = result + x**(2*i+1)/factorial(2*i+1)
  return result

def approx_cosh(x,n):
  result = 1
  for i in range(1,n+1):
    result = result + x**(2*i)/factorial(2*i)
  return result

#chạy test kết quả:
print(approx_sin(3.14,10))
print(approx_cos(3.14,10))
print(approx_sinh(3.14,10))
print(approx_cosh(3.14,10))

assert round(approx_cos(1,10),2) == 0.54
print(round(approx_cos(x=3.14, n=10),2))

assert round(approx_sin(1,10),4) == 0.8415
print(round(approx_sin(x=3.14, n=10),4))

assert round(approx_sinh(1,10),2) == 1.18
print(round(approx_sinh(x=3.14, n=10),2))

assert round(approx_cosh(1,10),2) == 1.54
print(round(approx_cosh(x=3.14, n=10),2))