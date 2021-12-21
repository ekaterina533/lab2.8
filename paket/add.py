#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def add():
    name = input("Фамилия, Имя? ")
    number = input("Номер телефона? ")
    print("Дата рождения:")
    day = input("День")
    month = input("Месяц")
    year = input("Год")
    bases = {
        'name': name,
        'number': number,
        'day': day,
        'month': month,
        'year': year,
    }
    base.append(bases)
    if len(base) > 1:
        base.sort(key=lambda item: item.get('name', ''))