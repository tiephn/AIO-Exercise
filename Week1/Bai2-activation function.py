
import math

def is_number(n):
  try:
    float (n)
  except ValueError:
    return False
  return True

def sigmoid(x):
  return 1/(1+math.exp(-x))

def relu(x):
  if x<=0:
    return 0
  else:
    return xs

def elu(x,alpha=0.01):
  if x>0:
    return x
  else:
    return alpha*(math.exp(x)-1)

def activation_function(x, act_fun):
  if act_fun == 'sigmoid':
    print(f"sigmoid: f({x}) = {sigmoid(x)}")
  elif act_fun == 'relu':
    print(f"ReLU: f({x}) = {relu(x)}")
  elif act_fun == 'elu':
    print(f"ELU: f({x}) = {elu(x)}")
  else:
    print(f"{act_fun} is not supported")
  return

def exercise2():
  x = input("Input x:")
  if is_number(x):
    act_fun = input("Input activation Function ( sigmoid | relu | elu ):")
    activation_function(float(x),act_fun)
  else:
    print('x must be a number')
  return

exercise2()