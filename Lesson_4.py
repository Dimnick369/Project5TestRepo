# region while + infinit while

# a=0
# while a>=0:
#     print(a)
#     a+=1

# какое значение переменной после отработки кода?
# i = 0
# while i <= 10:
#     i = i + 1
#     if i > 7:
#         i = i + 2
#
#     if i >= 8:
#         i=i-4
#
#     print(i)


# print(i)
b=0
while b<=5:
    a=int(input())

    print(a, b)

    if a>100:
        continue

    b+=1

    if  a==0:
        break

else:
    print(123)

# endregion
#####################################################
# region while break continue

# a=1
# while a<=10:
#     print(a,a**2)
#     a+=1

# while True:
#     a,b=input().split()
#     a,b=int(a),int(b)
#
#     if a<0:
#         print('Exit...')
#         break
#     elif 0<=a<=10:
#         print('Next step')
#         continue
#
#     print('Result: ', a*b,a+b,a-b)

# endregion