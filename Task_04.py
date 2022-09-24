# 4. Напишите программу, которая будет принимать на вход дробь
#    и показывать первую цифру дробной части числа.
# in 6.78  >> out 7   in 0.34  >> out 3

a = float(input())
ferst_num = a * 10 % 10

if ferst_num != 0:
    print(int(ferst_num))
else:
    print("No")



