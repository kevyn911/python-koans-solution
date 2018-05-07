#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from math import pi
from runner.koan import *


def extendto(value, shorter, longer):
    if len(shorter) > len(longer):
        raise ValueError('The `shorter` list is longer than the `longer` list')
    shorter.extend([value]*(len(longer) - len(shorter)))
class Elevator:

    people_lifted = 0

    def __init__(self,name):
        self.name = name
        self.people_lifted = 0

    def lift(self, people):
        self.people_lifted += people
        Elevator.people_lifted += people

class OneTime:
    s = ''
    def __init__(self):
        self.s = 'created'
    def normal_call(self):
        OneTime.s = 'normal_call'
    def call(self):
        OneTime.s = 'first_call'
        self.call = self.normal_call

class Cat:

    def add_idol(self, name):
        self.idols.append(name)

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.idols = []
    def dinner(self):
        self.weight += 0.4
    def breakfest(self):
        self.weight += 0.2
    def walk(self):
        self.weight -= 0.5

class AboutLazorishinetsKoans(Koan):

    # Задання діапазону до певних змінних
    def test_range(self):
        a, b = range(2)
        self.assertEqual(1, b)

    # 3мінна *rest, яка містить всі значення діапазону, крім вказаних у змінні
    def test_range1(self):
        a, *rest, b = range(10)
        self.assertEqual(0, a)
        self.assertEqual(9, b)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], rest)

    # Розширення коротшого списку на довжину довшого списку з значенням `value`
    def test_extend(self):
        a = [1,2]
        b = [1, 2, 3, 4, 5]
        extendto(10, a, b)
        self.assertEqual(a, [1, 2, 10, 10, 10])

    #Множення матриць за допомогою @ у Python 3.0+
    def test_maxtirx_multuplicate(self):
        a = np.array([[1, 0], [0, 1]])
        b = np.array([[4, 1], [2, 2]])
        self.assertEqual(str(a @ b), '[[4 1]\n [2 2]]')

    #Перевірка на входження підстроки в строку
    def test_substring(self):
        t = False
        string = "It's my python tests"
        if string.find('my') != -1:
            t = True
        self.assertTrue(t)

    #Реверс строки
    def test_reverse(self):
        a = "Леша на полке клопа нашел"
        self.assertEqual(a[::-1], "лешан аполк еклоп ан ашеЛ")

    # Доступність використання Unicode змінних в Python 3.0 +
    def test_unicode_variables(self):
        r = 12;
        π = pi
        area = π * r**2

        résumé = 'knows Python'
        self.assertTrue('Python' in résumé)

    # Нескінченно вкладений список
    def test_unlimited_added_list(self):
        a = [1, 2, 3, 4]
        a.append(a)
        self.assertTrue(a[4][4][4][4][4][4][4][4][4][4], a)

    # Форматування списка
    def test_formatting_list(self):
        l = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
        self.assertEqual(sum(l, []), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    # Генерування словників
    def test_generator_of_dictionary(self):
        self.assertEqual({a:a**2 for a in range(1, 10)}, {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81})

    # Приклад ООП (ліфт)
    def test_elevator(self):
        elevator_1 = Elevator("OTIS")
        elevator_2 = Elevator("PHILLIPS")
        elevator_1.lift(2)
        elevator_2.lift(3)
        elevator_2.lift(4)
        elevator_2.lift(1)

        self.assertEqual(elevator_1.name, "OTIS")
        self.assertEqual(elevator_2.name, "PHILLIPS")
        self.assertEqual(Elevator.people_lifted, 10)
        self.assertEqual(elevator_1.people_lifted, 2)
        self.assertEqual(elevator_2.people_lifted, 8)

    # Приклад ООП
    def test_cat_class(self):
        cat_1 = Cat("Murzik", 10)
        cat_2 = Cat("Pushok", 14)

        cat_1.breakfest()
        cat_1.dinner()
        cat_2.dinner()
        cat_2.dinner()
        cat_1.walk()
        cat_2.add_idol(cat_1.name)

        self.assertEqual(cat_1.name, "Murzik")
        self.assertEqual(cat_2.name, "Pushok")
        self.assertEqual(cat_1.weight, 10.1)
        self.assertEqual(cat_2.weight, 14.8)
        self.assertEqual(cat_2.idols, ['Murzik'])

    # Одноразова функція в класі
    def test_one_time_function(self):
        funct = OneTime()
        funct.call()
        self.assertEqual(OneTime.s, "first_call")
        funct.call()
        self.assertEqual(OneTime.s, "normal_call")
