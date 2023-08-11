#!/usr/bin/python3
for v in range(97, 127):
    if chr(v) != 'q' and chr(v) != 'e':
        print("{}".format(chr(v)), end="")
