#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Licença: GoHorser v3.0

import os
import sys
import math
#import time


# pega o passado como parametro
try:
    f = int(sys.argv[1])
except IndexError: #ahh esses humanos, sem codigo, manda um teste na excessão, garantindo parametros ...
    f = 100
    print ('\033[32m'+'seed da sequencia ausente, experimente: python fibo.py numero'+'\033[0;0m')

def fibonacci(n):
    a = 0
    b = 1
    while b < n:
        print b
        a = b
        b = a+b

print 'horser code'
fibonacci(f)
