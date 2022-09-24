# Напишите программу, которая принемает на вход
# цифру, обозначающую день недели, и проверяет
# является ли этот день выходным
# in 5 >> out "Workday"     in 6 >> out "Weekend"

num = int(input('Введите число от 1 до 7: '))

if num == 1:
    print("Workday")
elif num == 2:
    print("Workday") 
elif num == 3:
    print("Workday")
elif num == 4:
    print("Workday")
elif num == 5:
    print("Workday")
elif num == 6:
    print("Weekend")
elif num == 7:
    print("Weekend")
else:
    print("от 1 до 7 Вася!")                
