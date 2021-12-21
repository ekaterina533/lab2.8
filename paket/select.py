#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def select():
    parts = command.split(' ', maxsplit=2)
    sel = (parts[1])
    count = 0
    for bases in base:
        if bases.get('month') == sel:
            count += 1
            print(
                '{:>4}: {}'.format(count, bases.get('name', ''))
            )
    if count == 0:
        print("В этом месяце ни у кого нет дня рождения.")

