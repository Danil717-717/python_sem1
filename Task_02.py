# Напишите программу, которая на вход принемает 5 чисел и 
# находит максимальное из них
# in 1,3,5,6,2  >> out 6

max = 0
for i in range(5):
    n = int(input())
    if n > max:
        max = n
print(max)        
