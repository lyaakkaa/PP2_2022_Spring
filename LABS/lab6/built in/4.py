from time import sleep

from math import sqrt

num = int(input())

millisec = int(input())
sleep(millisec//1000)
print(f"Квадратный корень из {num} после {millisec} миллисекунд равен {sqrt(num)}.")