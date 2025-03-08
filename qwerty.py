import random
import math
import statistics

print('ЗАДАНИЕ 1') # задание №1

result_list = []  # Создаем пустой список для хранения результатов
i = 0        # Инициализируем счетчик

while i <= 15:  # Пока счетчик не превысит 15
    result_list.append(i)  # Добавляем текущее значение в список
    i += 1            # Увеличиваем счетчик на 1

print(result_list)  # Выводим полученный список

print('ЗАДАНИЕ 2') # задание №2

result_set = set()               # Инициализируем пустое множество

for num in result_list:        # Итерируемся по элементам списка, созданного в задании №1
    if num > 10:                 # Если число превышает 10
        break                    # Прерываем цикл
    result_set.add(num)          # Добавляем число в множество

print(result_set)                # Выводим результат

print('ЗАДАНИЕ 3') # задание №3

i = 0  # Инициализируем индекс
while i < len(result_list):  # Пока не пройдены все элементы
    if result_list[i] < 11:  # Если элемент меньше 11
        del result_list[i]   # Удаляем элемент на текущей позиции
    else:
        i += 1                 # Переходим к следующему элементу

print(result_list)  # Выводим модифицированный список

print('ЗАДАНИЕ 4') # задание №4

tuple_length = random.randint(10, 15)   # Генерируем кортеж со случайным количеством элементов (от 10 до 15)
random_tuple = tuple(random.randint(29, 81) for _ in range(tuple_length))   # Заполняем кортеж случайными числами от 29 до 81

transformed_elements = []   # Преобразуем элементы кортежа
for num in random_tuple:
    if num >= 50:
        transformed_elements.append(num + 39)  # Увеличиваем на 39
    else:
        transformed_elements.append(num * 3)   # Умножаем на 3

result_list.clear() # Очищаем ранее созданный список

for num in transformed_elements:    # Заполняем очищенный список
    result_list.append(num)
print(result_list)

result_list.extend(reversed(random_tuple))  # Добавляем элементы кортежа в обратном порядке в конец списка
print(result_list)

print('ЗАДАНИЕ 5') # задание №5

list1 = [random.randint(1, 10) for _ in range(5)]   # Генерация тестовых данных
list2 = [random.randint(1, 10) for _ in range(5)]

def process_rectangles(lengths, widths):

    circle_areas = []   # Рассчитываем площади описанных окружностей
    for l, w in zip(lengths, widths):
        R = math.sqrt(l**2 + w**2)/2
        area = math.pi * R**2
        circle_areas.append(area)
    circle_areas = tuple(circle_areas)

    avg = sum(circle_areas) / len(circle_areas)  # Находим среднее арифметическое

    threshold = avg * 1.1    # Фильтруем значения, превышающие среднее более чем на 10%
    filtered = tuple(filter(lambda x: x <= threshold, circle_areas))

    product = 1 # Рассчитываем произведение
    for num in filtered:
        product *= num
    
    return product / len(lengths)

print(process_rectangles(list1, list2))

print('ЗАДАНИЕ 6') # задание №6

def generate_and_process_list(min_val, max_val, step):
    
    lst = []    # Генерация списка с заданными параметрами
    current = min_val
    while current <= max_val:   # Реализация с циклом while предполагает возможность дробного шага
        lst.append(current)
        current += step
    
    if not lst: # Проверка, что список не пуст (например, если min > max)
        return []
    
    multiples_of_7 = list(filter(lambda x: x % 7 == 0, lst))    # Количество чисел, кратных 7 (с использованием filter)
    count = len(multiples_of_7)
    
    median = statistics.median(lst) # Вычисление медианы
    
    result = count - median # Определение результата
    
    # Логика преобразования списка
    if result < 0:
        return lst[::-1]  # Используя возможность взять срез списка, возвращаем его в обратном порядке
    else:
        new_lst = lst.copy()
        new_lst.insert(0, result)  # Добавление результата в начало
        return new_lst

# Пример использования
min_val = 2
max_val = 15
step = 1.3
final_list = generate_and_process_list(min_val, max_val, step)
print("Итоговый список:", final_list)

print('ЗАДАНИЕ 7') # задание №7

def dice_game(num_players,  *names):    # Такой синтаксис позволяет передавать имена как отдельные аргументы, а не цельным списком
    # имена собираются в кортеж
    if len(names) != num_players:
        raise ValueError(f"Количество имён не соответствует числу игроков: ожидалось {num_players}, получено {len(names)}")
    
    results = [(name, random.randint(1, 6)) for name in names]  # Генерируем результаты бросков и собираем их в словарь (генератор списка)
    # проходка по словарю и создание пар ключ-значение с использованием random
    
    # Выводим результаты попыток
    print("Результаты бросков:")
    for name, score in results:
        print(f"{name} выбросил(а) {score}")    # Используем форматированный вывод
    
    # Определяем максимальное значение
    max_score = max(score for _, score in results)  # Используя генератор списка, достаем 2-й элемент кортежа (score), игнорируя name
    #print(max_score)
    winners = [name for name, score in results if score == max_score]   # Итерация по кортежам с распаковкой (достаем только ключ), если score == max_score
    #print(winners)
    
    # Выводим итоговый результат
    print("\nИтоговый результат:")
    if len(winners) == 1:
        print(f"Победитель: {winners[0]}")
    else:
        print(f"Ничья между: {', '.join(winners)}") # Ничья как вероятный результат
    
    return results, winners
    
dice_game(3, "Alice", "Bob", "Pididi")