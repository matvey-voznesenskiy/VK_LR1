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
    
    '''def data_filter(element):
        if element>=median:
            return True
        else:
            return False
    dict1=dict(filter(data_filter, dict0))
    print(dict1)'''

    list3=list(filter(lambda x: x>=median,list2)) #?????????
    print(list3)


#filtered = dict(filter(lambda x: x[1] >= median, dictionary.items()))
#return filtered



#поменять на dict
    dict1=dict0
    for i in range(len(list3)):
        n=-1
        for val in dict0.values(): #как организовать удаление из исходного словаря?????
            n+=1
            if list3[i]!=val:
                del dict1[n]
#в 2 этапа
    '''for val in dict0.values():
        for i in range(len(list3)):
            if ...:
                del''' 

    '''dict1={}
    for new_keys, new_values in zip(dict0, list3):
        dict1[new_keys] = new_values'''
    return dict1

print(result(ctrl_dict, ctrl_list))
    
