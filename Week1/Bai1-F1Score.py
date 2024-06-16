import math

def exercise1(tp=0, fp=0, fn=0):

  if not isinstance(tp, int):
    print('tp must be int'); return
  if not isinstance(fp, int):
    print('fp must be int'); return
  if not isinstance(fn, int):
    print('fn must be int'); return

  if (tp<=0 or fp<=0 or fn<=0):
    print('tp and fp and fn must be greater than zero'); return

  precision = tp/(tp+fp)
  recall = tp/(tp+fn)
  f1_score = 2*(precision*recall)/(precision+recall)
  print(f"Precision is {precision}\nRecall is {recall}\nF1-Score is {f1_score}")


#chạy test kết quả:
exercise1(2,3,4)
exercise1('a', 3, 4)
exercise1(2, 'a', 4)
exercise1(2, 3, 'a')
exercise1(2, 3, 0)
exercise1(2.1, 3, 0)

exercise1(2, 4, 5)
