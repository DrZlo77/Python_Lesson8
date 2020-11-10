# ==================================================================================
import time
import os
import random
import psutil
import sys

'''
1. Написать декоратор, замеряющий время выполнение декорируемой функции.
'''
# ==================================================================================

def show_time_decorate(f):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        print(time_start)
        f(*args, **kwargs)
        time_finish = time.time()
        print(time_finish)
        time_spend = time_finish - time_start
        print(f'Времени на выполнение затрачено {time_spend}')

    return wrapper


@show_time_decorate
def function_for_dimentions(n):
    list_f = [i ** 2 for i in range(n + 1)]


function_for_dimentions(100000)

'''
2. Сравнить время создания генератора и списка с элементами: натуральные числа от 1 до 1000000 (создание объектов оформить в виде функций).
'''
# ==================================================================================


def simple_list_dimentions_time(n):
    list_s = [i for i in range(n + 1)]
    return list_s


def simple_generate_dimentions_time(n):
    list_gen_s = (i for i in range(n + 1))
    return list_gen_s


def dimentions_time_for_list_generate(n):
    start_time_simple_list = time.time()
    simple_list_dimentions_time(n)
    finish_time_simple_list = time.time()
    time_spend_simple_list = finish_time_simple_list - start_time_simple_list
    print("Время создания списка с элементами", time_spend_simple_list)

    start_time_gen_list = time.time()
    simple_generate_dimentions_time(n)
    finish_time_gen_list = time.time()
    time_spend_gen_list = finish_time_gen_list - start_time_gen_list
    print("Время создания генератора списка", time_spend_gen_list)


dimentions_time_for_list_generate(1000000)

'''
3. Написать декоратор, замеряющий объем оперативной памяти, потребляемый декорируемой функцией.
'''
# ==================================================================================

def show_memory(f):
    def wrapper(*args, **kwargs):
        memory_size = sys.getsizeof(f(*args, **kwargs))
        print("Объем оперативной памяти, потребляемый декорируемой функцией:", memory_size)

    return wrapper


n = 10000000


@show_memory
def gen_list():
    simple_list_dimentions_time(n)


gen_list()

'''
4. Сравнить объем оперативной памяти для функции создания генератора и функции создания списка с элементами: натуральные числа от 1 до 1000000.
'''
# ==================================================================================

n = 10000000


def memory_dimentions():
    memory_size_simp_list = sys.getsizeof(simple_list_dimentions_time(n))
    memory_size_gen_list = sys.getsizeof(simple_generate_dimentions_time(n))

    print('Объем оперативной памяти функции создания списка:', memory_size_simp_list)
    print('Объем оперативной памяти функции создания списка:', memory_size_gen_list)
    print('Объем потребляемой оперативной памяти функции создания списка больше чем генератора списка на:', memory_size_simp_list - memory_size_gen_list)

memory_dimentions()
