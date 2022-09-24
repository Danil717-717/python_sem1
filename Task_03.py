# Напишите программу, которая будет на вход
# принемать число N и выводить числа от -N до N
# in 5   >> out -5,-4,-3,-2,-1,0,1,2,3,4,5

#print('Введите число: ')
#a = int(input())
# for i in range(-a, a + 1):
#    print(i, end = ' ')      #end выводит в строчку

# ###########################var2
#num = int(input())
#op_num = num + 1
#step = 1
# if num < 0:
#    op_num = num - 1
#    step = -1
#
# for i in range(-num, op_num, step):
#    print(i, end=", ")

# ##########################var3
num = int(input())
neg_num = -num
print(neg_num, end=", ")

while num != neg_num:
    if num > 0:
        neg_num += 1
    else:
        neg_num -= 1
    print(neg_num, end=", ")
