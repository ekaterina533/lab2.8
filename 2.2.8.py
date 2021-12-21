#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 12. Использовать словарь, содержащий следующие ключи: фамилия, имя; номер телефона;
# дата рождения (список из трех чисел). Написать программу, выполняющую следующие
# действия: ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть размещены по алфавиту; вывод на экран информации о людях, чьи
# дни рождения приходятся на месяц, значение которого введено с клавиатуры; если таких
# нет, выдать на дисплей соответствующее сообщение


import sys
from paket import add, list, help, select


if __name__ == '__main__':
    base = []
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break

        elif command == 'add':
           add()

        elif command == 'list':
            list()

        elif command.startswith('select '):
           select.select()

        elif command == 'help':
            help.help()
        else:
            print("Неизвестная команда {command}", file=sys.stderr)
