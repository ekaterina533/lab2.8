#!/usr/bin/env python3
# -*- coding: utf-8 -*-


base = []


def list():
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 8
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
            "№",
            "Ф.И.",
            "Номер телефона",
            "Дата рождения"
        )
    )
    print(line)
    for idx, bases in enumerate(base, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                idx,
                bases.get('name', ''),
                bases.get('number', ''),
                bases.get('month', 0)
            )
        )
    print(line)


