# # Задача 2: Найдите сумму цифр трехзначного числа.
# # 123 -> 6 (1 + 2 + 3)
# # 100 -> 1 (1 + 0 + 0)
# n= int(input('введите трехзначное число: '))
# summa=0
# while n>0:
#     x=n%10
#     summa=summa+x
#     n=n//10
# print(summa)
''''''

#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# # а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

# s=int(input("Введите сколько Журавликов сделали дети: "))
# c=int((s/3)*2)
# a=int((c/2)/2)
# b=int(a)
# print(a,b,c)
''''''
# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
#  Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
#  Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# # 123456 -> no
# n=input("Введите 6 значный номер билета: ")
# s1=int(n[0]) + int(n[1]) + int(n[2])
# s2=int(n[3]) + int(n[4]) + int(n[5])
# if s1==s2:
#     print('yes')
# else:
#     print('no')
''''''
# a = int(input('Введите номер билета: '))  
# sum_1 = 0
# sum_2 = 0
# for i in range(6):
#     if i < 3:
#         sum_1 = sum_1 + a // 10**i % 10
#     else:
#         sum_2 =  sum_2 + a // 10**i % 10 
# if sum_2 == sum_1:
#     print('yes')
# else:
#     print('no')  
''''''
#  Задача 8: Требуется определить, можно ли от шоколадки размером n × m 
# долек отломить k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no
# n=int(input())
# m=int(input())
# k=int(input())
# if k%n==0 or k%m==0:
#     print('yes')
# else:
#      print('no')