# region conditions
# a=-5
# if a>-5:
#     print('Yes')
#     print('Hello')
# else:
#     print('NO')


# ###########################
# a=-7 #0
# if a>0:
#     print('Yes')
# elif a>-5:
#     print('Test')
# else:
#     print('No')
#



#

# endregion
#############################################################################################
# region conditions2
# func_output = None
# msg = func_output or "Пусто"
# print(msg)

# a=10
# a>5 and print('asdasd')

# endregion
#############################################################################################
# region bool
# print(int(True),int(False))

# x y res
# 1 1  1
# 1 0  1
# 0 1  1
# 0 0  0
#
#
# a,b=5,10
#       # 0         1
# # c = a==b or int(b==10)
# # c = int(b==10) or a==b
# print(a,b,c)

# a=19
# print(a<10)
# print(10<=a<=20)

# def t1 ():
#     print(1)
#     return False
#
# def t2 ():
#     print(2)
#     return False
#
# print(t1() or t2())  #Вызовет только первую функцию

# x,y=100,5
# print(any([x>10,y>15]))
# print(all([x>10,y>15]))

# endregion
#############################################################################################
# region try
# try:
#     a=10/5
#     # a=10/0
# except:
#     print(123)
# else:
#     print(345)
# finally:
#     print(3)


try:
    a = int('dfss')
    print(10/0)

except ZeroDivisionError:
    print('ert')
except :
    print (1)

# endregion
#############################################################################################
