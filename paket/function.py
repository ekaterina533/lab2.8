#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def function1(c, k):
    def function2(s):
        s = s.replace(c, k)
        st = ""
        for i in range(0, len(s)):
            if s[i] != s[i - 1]:
                st += s[i]
        return st
    return function2


