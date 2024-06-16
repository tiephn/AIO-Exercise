import math
import random

def is_int(n):
  try:
    int(n)
  except ValueError:
    return False
  return True

def mae(numSamples):
  result = 0
  for i in range(0,numSamples):
    predict = random.uniform(0,10)
    target = random.uniform(0,10)
    result = result + abs(target - predict)
    print(f"loss name: MAE, sample {i}, pred: {predict}, target: {target}, loss: {result}")
  result = result/numSamples
  print(f"final MAE: {result}")
  return

def mse(numSamples):
  result = 0
  for i in range(0,numSamples):
    predict = random.uniform(0,10)
    target = random.uniform(0,10)
    result = result + abs(target - predict)**2
    print(f"loss name: MSE, sample {i}, pred: {predict}, target: {target}, loss: {result}")
  result = result/numSamples
  print(f"final MSE: {result}")
  return

def rmse(numSamples):
  return math.sqrt(mse(numSamples))

def reg_loss(numSamples, lossName):
  if lossName == 'MAE':
    return mae(numSamples)
  elif lossName == 'MSE':
    return mse(numSamples)
  elif lossName == 'RMSE':
    return mse(numSamples)

numSamples = input("Input number of samples (integer number) which are generated:")
if is_int(numSamples):
  lossName = input("Input loss name (MSE | MAE | RMSE ):")
  reg_loss(int(numSamples),lossName)
else:
  print('number of samples must be an integer number')
