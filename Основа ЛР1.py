'''
tuple1 = (1,2,3,4,5,6,7,8,9,10)
print('Кортеж:\n', tuple1)
#----------------
tuple1 = (1,2,3,4,5,6,7,8,9,10)
list1=[]
for i in range(len(tuple1)):
    if tuple1[i]%2==0:
        list1.insert(i, int(tuple1[i]*5))
    else:
        list1.insert(i, int(tuple1[i]+3))
    i+=1
list1+=tuple1
print('Новый список:\n',list1)
sorted_list1=sorted(list1, reverse=True)
print('Отсортированный список:\n',sorted_list1)
#----------------
set1=set(sorted_list1)
print('Множество из элементов списка:\n',set1)
#----------------
list1=[3,4,242,64,77,55,1]
print('Произвольный список:\n', list1)
A=list1[0]
list1[0]=list1[len(list1)-1]
list1[len(list1)-1]=A
print('Поменяли местами 1й и последний элементы списка:\n', list1)
#----------------
import math
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
#----------------
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
    for i in range(I):
        if list1[i]%2==0:
            t+=list1[i]**2
    i=0
    a=math.sqrt(t)
    def data_filter(element):
        if (element%2)==1 and (element%3)==0:
            return True
        else:
            return False
    set1=set(filter(data_filter, list1))
    ''''''ВАЖНО! filter не преобразуется в list, если есть переменная с именем list! для проверки:
    print(list) должен выдавать class 'list', а не что-то названное автором кода''''''

    #в головном файле этот код не будет работать, тк есть множества, названные set. код будет работать только в отдельном файле
    
    #еще важно: комментарии через '''''' должны табулироваться по правилам XD иначе, если у комма выше убрать табы, код выдаст ошибку (cringe)
    return set1

print('Итоговое множество:\n', list_creating(1,11,2))
'''#----------------

ctrl_dict={'сколько будет 1+2?': 3, #контрольный словарь на вход
       'сколько будет 2+2?': 4,
       'сколько будет 3+2?': 5,
       'сколько будет 4+2?': 6,
       'сколько будет 5+2?': 7}
ctrl_list=['сколько будет 4+2?', #контрольный список ключей на вход
       'сколько будет 1+2?',
       'сколько будет 3+2?',
       'сколько будет 2+2?',
       'сколько будет 5+2?']
def result(dict0, list0):
    list1=[] #список значений, которые достали из dict0 по ключам из list0
    i=0 #индекс
    for i in range(len(list0)):
        list1.insert(i, int(dict0[list0[i]]))
    i=0
    print(list1)
    list2=sorted(list1) #сортировка для поиска медианы
    print(list2)
    median=list2[len(list2)//2] #поиск медианы
    print(median)
    list3=list(filter(lambda element: element>=median,list2))
    print(list3)

print(result(ctrl_dict, ctrl_list))

