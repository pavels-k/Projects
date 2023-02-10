#! /usr/bin/env python
# -*- coding: utf-8 -*-

import operator
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

from input_data import input_parameters


# Создание класса полиомина
class Polimino:
    def __init__(self, poli, kind):
        self.xlengh = len(poli)  # Количество клеток по горизонтали
        self.ylengh = len(poli[0])  # Количество клеток по вертикали
        self.kind = kind  # Вид полиомина
        self.area = sum_poli(poli)  # Площадь полиомина
        self.rotations = {}
        self.count_rotations = 0  # Количество поворотов
        self.rotations[0] = np.array(poli)
        if self.kind == 'R':
            if self.xlengh != self.ylengh:  # Не квадрат
                self.count_rotations = 1
                self.rotations[1] = np.rot90(poli)
        if self.kind == 'L':
            self.count_rotations = 3
            self.rotations[1] = np.rot90(poli)
            self.rotations[2] = np.rot90(self.rotations[1])
            self.rotations[3] = np.rot90(self.rotations[2])


class Error(BaseException):
    def __init__(self, mess, signal=False):
        self.message = 'Error: ' + mess
        self.signal = signal


# Площадь полиомина
def sum_poli(param):
    sum = 0
    for item_row in param:
        for item in item_row:
            sum = sum + item
    return sum


# Вывод полиомина
def print_poli(param):
    for item_row in param:
        for item in item_row:
            print(item)  # , end="")
        print()
    print()


# Проверка на наличие в матрице числа больше 1
def check_cross(param):
    for item_row in param:
        for item in item_row:
            if item > 1:
                return False
    return True


# Построение границ клетки для графика
def rect(pos):
    r = plt.Rectangle(pos - 0.5,
                      1,
                      1,
                      facecolor="none",
                      edgecolor="k",
                      linewidth=2)
    plt.gca().add_patch(r)


print('1.', input_parameters[0], ' – размер прямоугольника-стола.')
print(
    '2.', input_parameters[1],
    ' – лист из тапл-пар, содержащий информацию об опорных прямоуголных полиомино.'
)
print('3.', input_parameters[2],
      ' – лист из тапл-пар, содержащий информацию об опорных L-полиомино.')
print()
# Количество клеток стола по x
x_lim = input_parameters[0][0]
# Количество клеток стола по y
y_lim = input_parameters[0][1]

# Инициализация стола в виде двумерного списка
table = [0] * x_lim
for i in range(x_lim):
    table[i] = [0] * y_lim

# Инициализация прямоугольных полиоминов в виде двумерного списка
poliomino_r = []
for poliomino in input_parameters[1]:
    inner_poli = []
    inner_poli = [1] * poliomino[0][0]
    for i in range(poliomino[0][0]):
        inner_poli[i] = [1] * poliomino[0][1]
    # Учитываем мощность
    for N in range(poliomino[1]):
        poliomino_r.append(inner_poli)

# Инициализация L-полиоминов в виде двумерного списка
poliomino_l = []
for poliomino in input_parameters[2]:
    inner_poli = []
    inner_poli = [0] * poliomino[0][0]
    for i in range(poliomino[0][0]):
        inner_poli[i] = [0] * poliomino[0][1]
        for j in range(poliomino[0][1]):
            if j == 0:
                inner_poli[i][j] = 1
            # Не первый ряд и последний столбец
            elif j != 0 and i == poliomino[0][0] - 1:
                inner_poli[i][j] = 1
    # Учитываем мощность
    for N in range(poliomino[1]):
        poliomino_l.append(inner_poli)

# Создание экземпляров класса
POLIMINOS = []
for poli in poliomino_r:
    POLIMINOS.append(Polimino(poli, 'R'))
for poli in poliomino_l:
    POLIMINOS.append(Polimino(poli, 'L'))

# Сортировка полиоминов по площади
POLIMINOS = sorted(POLIMINOS, key=operator.attrgetter('area'), reverse=True)

# Подсчёт общей площади и добавление условия выхода
area = 0
for poli in POLIMINOS:
    # размеры полиомино >= размеров стола, с учётом поворота
    if ((poli.xlengh > x_lim or poli.ylengh > y_lim)
            and ((poli.ylengh > x_lim) or (poli.xlengh > y_lim))):
        raise Error('Полиомион выходит за границы стола!')
    area += poli.area
if (area > x_lim * y_lim):
    raise Error('Площадь Полиомионов больше стола!')

step = 0
data_list = []

print('Введите любой ключ, чтобы продолжить...')
input()


# Рекурсивная функция ставит полиомин на стол
def Insert_poli(step, table, data_list):
    # Проход всех индексов
    for i in range(len(table)):
        for j in range(len(table[i])):
            # Проход с учётом поворота
            for count_rotation in range((POLIMINOS[step].count_rotations) + 1):
                # Проверка на возможность вставки
                if i + len(
                        POLIMINOS[step].rotations[count_rotation]
                ) <= x_lim and j + len(
                        POLIMINOS[step].rotations[count_rotation][0]) <= y_lim:
                    # Проход индексов полиомина и присвоение значение стола
                    for index_i, poli in enumerate(
                            POLIMINOS[step].rotations[count_rotation]):
                        for index_j, item in enumerate(poli):
                            table[i + index_i][j + index_j] += item
                    # Проверка на отсутствие пересечений
                    if check_cross(table):
                        step += 1  # Следующий полиомин
                        data_list.append([i, j,
                                          count_rotation])  # Сохранение шага
                        if step == len(
                                POLIMINOS):  # Если пройдены все полиомины
                            return data_list  # Возвращение всех, необходимых данных для шага
                        result_recursion = Insert_poli(
                            step, table,
                            data_list)  # Вызов для следующего полиомина
                        # Если вставка произошла, то выход из всех рекурсивных функций
                        if result_recursion is not False:
                            return result_recursion
                        # Иначе продолжить вставку с предыдущего шага
                        step -= 1
                        # Удаление информации о вставке, которая не имела решений
                        data_list.pop()
                        # Вернуть прошлые значения стола
                        for index_i, poli in enumerate(
                                POLIMINOS[step].rotations[count_rotation]):
                            for index_j, item in enumerate(poli):
                                table[i + index_i][j + index_j] -= item
                    # Вернуть прошлые значения стола, если есть пересечение
                    else:
                        for index_i, poli in enumerate(
                                POLIMINOS[step].rotations[count_rotation]):
                            for index_j, item in enumerate(poli):
                                table[i + index_i][j + index_j] -= item
    # Не нашлось места в столе для вставки
    return False


# Результат функции, где хранятся индексы в соответствующем порядке
# и значение поворота для каждого полиомина, или значение False
data = Insert_poli(step, table, data_list)

# Обнуление стола
table = [0] * x_lim
for i in range(x_lim):
    table[i] = [0] * y_lim

# Заполняем список уникальными значениями(начиная c единицы) для каждого полиомина
for step, item in enumerate(data):
    for index_i, poli in enumerate(POLIMINOS[step].rotations[item[2]]):
        for index_j, item_value in enumerate(poli):
            if item_value != 0:
                table[item[0] + index_i][item[1] +
                                         index_j] += step + item_value
table = np.rot90(table)  # Поворот для правильной графической интерпретации

# Построение графика
if data is not False:
    cmap = cm.get_cmap("tab20c")  # Cтиль цветов
    colormap_r = mpl.colors.ListedColormap(
        cmap.colors[::-1])  # Реверс порядка цветов
    im = plt.imshow(table, cmap=colormap_r)

    x, y = np.meshgrid(np.arange(table.shape[1]), np.arange(
        table.shape[0]))  # Cетка для границы полиоминов
    m = np.c_[x[table.astype(bool)], y[table.astype(bool)]]
    # Создание границы
    for pos in m:
        rect(pos)

    print(True)
    plt.axis('off')
    plt.show()
else:
    print(False)
