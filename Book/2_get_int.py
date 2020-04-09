#!/usr/bin/env python3

def get_int(msg):
    while True:
        try:
            smth_int = int(input(msg))
            return smth_int
        except ValueError as error_msg:
            print(error_msg)

result = get_int("Enter integer: ")
print(result)