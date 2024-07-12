import math
import random

def is_int(n):
  try:
    int(n)
  except ValueError:
    return False
  return True

def mae(num_samples):
  result = 0
  for i in range(0,num_samples):
    predict = random.uniform(0,10)
    target = random.uniform(0,10)
    result = result + abs(target - predict)
    print(f"loss name: MAE, sample {i}, pred: {predict}, target: {target}, loss: {result}")
  result = result/num_samples
  print(f"final MAE: {result}")


def mse(num_samples):
  result = 0
  for i in range(0,num_samples):
    predict = random.uniform(0,10)
    target = random.uniform(0,10)
    result = result + abs(target - predict)**2
    print(f"loss name: MSE, sample {i}, pred: {predict}, target: {target}, loss: {result}")
  result = result/num_samples
  print(f"final MSE: {result}")


def rmse(num_samples):
  return math.sqrt(mse(num_samples))

def reg_loss(num_samples, loss_name):
  if loss_name == 'MAE':
    return mae(num_samples)
  elif loss_name == 'MSE':
    return mse(num_samples)
  elif loss_name == 'RMSE':
    return mse(num_samples)

num_samples = input("Input number of samples (integer number) which are generated:")
if is_int(num_samples):
  loss_name = input("Input loss name (MSE | MAE | RMSE ):")
  reg_loss(int(num_samples),loss_name)
else:
  print('number of samples must be an integer number')
