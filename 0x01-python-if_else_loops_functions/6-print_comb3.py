#!/bin/python3
for i in range(1, 89):
    if i < 10 or i // 10 < 1 % 10:
        print('{:02d}'.format(i), end=", ")
        print(89)
