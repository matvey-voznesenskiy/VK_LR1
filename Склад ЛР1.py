#----------
tuple=[]

for i in range(-1,9):
    i+=1
    tuple.insert(i,int(i+1))
print(tuple)
i=0

#-----------

tuple = (1,2,3,4,5,6,7,8,9,10)
print(tuple)

list=[]
for i in range(len(tuple)):#увеличиваем+вводим в список
    if tuple(i)%2==0:
        list.insert(i, int(tuple(i)*5)) #не работает тк нельзя обратиться к кортежу
    else:
        list.insert(i, int(tuple(i)+3))
    i+=1
print(list)

list=[0]*len(tuple) #мб вернуть как было
for i in range(len(tuple)): #не работает тк нельзя обратиться к кортежу (тоже)
    list[i]=tuple(i) #ОШИБКА в том что элемент задаю через () а не через []
for i in range(len(list)):
    if list[i]%2==0:
        list[i]=list[i]*5
    else:
        list[i]=list[i]+3
    i+=1
print(list)

list=[0]*len(tuple) #мб вернуть как было
for i in range(len(tuple)): #не работает тк нельзя обратиться к кортежу (тоже)
    list[i]=int(tuple(i))  #ОШИБКА в том что элемент задаю через () а не через []
for i in range(len(list)):
    if list[i]%2==0:
        list[i]=list[i]*5
    else:
        list[i]=list[i]+3
    i+=1
print(list)

list=list(tuple) #мб вернуть как было
for i in range(len(tuple)): #не работает тк нельзя обратиться к кортежу (тоже)
    list[i]=tuple(i) #ОШИБКА в том что элемент задаю через () а не через []
for i in range(len(list)):
    if list[i]%2==0:
        list[i]=list[i]*5
    else:
        list[i]=list[i]+3
    i+=1
print(list)

#------------------------

list=[1,4,242,64,77,55,1]
print(list)
A=list[0]
list[0]=list[len(list)-1]
list[len(list)-1]=A
print(list)

#------------------------

def list_creating(min,max,step):
    list=[] #список, который будем заполнять
    i=0 #индекс чисел в списке
    t=0 #сумма квадратов
    a=0 #корень из суммы квадратов
    for n in range(min,max+1,step):
        list.insert(i, int(n))
        i+=1
    I=i #размер списка
    i=0
    print(list)
    for i in range(I):
        if list[i]%2==0:
            t+=list[i]**2
    print(t)
    a=math.sqrt(t)
    return a

print(list_creating(1,11,3))


import math
def list_creating(min,max,step):
    list=[] #список, который будем заполнять
    i=0 #индекс чисел в списке/множестве
    t=0 #сумма квадратов
    a=0 #корень из суммы квадратов
    set={} #множество, которое будем заполнять
    for n in range(min,max+1,step):
        list.insert(i, int(n))
        i+=1
    I=i #размер списка
    i=0 #обнулять после цикла for обязательно
    n=0
    print(list)
    for i in range(I):
        if list[i]%2==0:
            t+=list[i]**2
    i=0
    print(t)
    a=math.sqrt(t)
    print(a)
    for n in range(min,max+1,step):
        if ... and ...:
            set.insert(i, int(n))
            i+=1
    i=0

print(list_creating(1,11,3))

def data_filter(element):
    if(element%2)== 1 and (element%3)==0:
        return True
    else:
        return False #data_filter должна быть внутри или снаружи list_creating?

set=set(set)





import math

def list_creating(min,max,step):
    list=[] #список, который будем заполнять
    i=0 #индекс чисел в списке/множестве
    t=0 #сумма квадратов
    a=0 #корень из суммы квадратов
    set={} #множество, которое будем заполнять
    for n in range(min,max+1,step):
        list.insert(i, int(n))
        i+=1
    I=i #размер списка
    i=0 #обнулять после цикла for обязательно
    n=0
    print(list)
    for i in range(I):
        if list[i]%2==0:
            t+=list[i]**2
    i=0
    print(t)
    a=math.sqrt(t)
    print(a)
    def data_filter(element):
        if (element%2)==1 and (element%3)==0:
            return True
        else:
            return False #data_filter должна быть внутри или снаружи list_creating? походу без разницы в д.с.
    filtered_set=filter(data_filter, list)
    print(filtered_set) #ВАЖНО! filter не преобразуется в list, если есть переменная с именем list! для проверки:
                        #print(list) должен выдавать class 'list', а не что-то названное автором кода
    return set

print(list_creating(1,11,2))

import math

def list_creating(min,max,step):
    list1=[] #список, который будем заполнять
    i=0 #индекс чисел в списке/множестве
    t=0 #сумма квадратов
    a=0 #корень из суммы квадратов
    set1={} #множество, которое будем заполнять
    for n in range(min,max+1,step):
        list1.insert(i, int(n))
        i+=1
    I=i #размер списка
    i=0 #обнулять после цикла for обязательно
    n=0
    print(list1)
    for i in range(I):
        if list1[i]%2==0:
            t+=list1[i]**2
    i=0
    print(t)
    a=math.sqrt(t)
    print(a)
    def data_filter(element):
        if (element%2)==1 and (element%3)==0:
            return True
        else:
            return False
    set1=set(filter(data_filter, list1))
    '''ВАЖНО! filter не преобразуется в list, если есть переменная с именем list! для проверки:
    print(list) должен выдавать class 'list', а не что-то названное автором кода'''

    #в головном файле этот код не будет работать, тк есть множества, названные set. код будет работать только в отдельном файле
    
    #еще важно: комментарии через ''' должны табулироваться по правилам XD иначе, если у комма выше убрать табы, код выдаст ошибку (cringe)
    return set1

print(list_creating(1,11,2))

#------------------------

dict1={'сколько будет 1+2?': 3, #словарь на вход
       'сколько будет 2+2?': 4,
       'сколько будет 3+2?': 5,
       'сколько будет 4+2?': 6,
       'сколько будет 5+2?': 7}
list1=['сколько будет 5+2?', #список ключей на вход
       'сколько будет 4+2?',
       'сколько будет 3+2?',
       'сколько будет 2+2?',
       'сколько будет 1+2?']
def result(dict0, list0):
    res_list=[] #список значений, которые достали из dict1 по ключам из list1
    i=0 #индекс в list1/list2
    for i in range(len(list0)):
        #res_list[i]=dict0[list0[i]] узнать почему он не хочет вот так работать
        #res_list[i]=dict0['сколько будет 5+2?']
        #print(dict0[list0[i]])
        #res_list[i]=int(dict0[list0[i]])
        res_list.insert(i, int(dict0[list0[i]]))
    i=0

print(result(dict1, list1))
