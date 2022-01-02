import time
from datetime import date

FMT = "%I:%M:%S %p"

t1 = time.localtime()
s1 = time.strftime(FMT, t1)
print("Start time:\t" + str(date.today()) + "\t" + s1)

while True:
  t2 = time.localtime()
  s2 = time.strftime(FMT, t2)
  print("Current time:\t" + str(date.today()) + "\t" + s2, end="", flush=True)
  print("\r", end="", flush=True)
  time.sleep(1)
