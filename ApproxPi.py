#ApproxPi.py
#Name: Emma Zechmann
#Date: 2/8/2026
#Assignment: extra lab 3 
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  Decimal_precision = int(input("Please Give Me A Number Up to Ten For The Decimal Precision Points of Pie: "))
  tolerance= 10** (-Decimal_precision)
  start = time.time()

  approx_pi=0
  n=0

  while abs(approx_pi - math.pi) > tolerance:
    approx_pi += 4 * ((-1)** n)/(2*n +1)
    n+=1


  #calculate pi using the approximation technique
  #Loop until the level of percision is reached

  end = time.time()

  elapsedTime = end - start
  print(f"Elapsed Time: {elapsedTime} seconds")
  print(f"{approx_pi}")


if __name__ == '__main__':
  main()
