# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zRwyyEm3mKnzvhbXpZIu0nNNFs1kWu9M
"""

import math

def get_radius(prompt):
    r = int(input(prompt))
    return r

def calculate_area(radius):
    return math.pi * radius ** 2

radius = get_radius("원의 반지름을 입력하세요: ")

area = calculate_area(radius)

print(f"반지름 {radius}인 원의 넓이는 {area:.2f}입니다.")

