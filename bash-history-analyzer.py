#!/usr/bin/env python

import os, sys

bash_history_path = os.environ['HOME'] + '/.bash_history'

records = {}

def check_line(line):
    cmd = line.split()[0]
    if cmd in records:
        records[cmd] += 1
    else:
        records[cmd] = 1

def print_top(n):
    l  = [[cmd,records[cmd]] for cmd in records]
    l.sort(key = lambda r: r[1], reverse = True)
    count = 1
    for record in l[:n]:
        print '#%d -- Command %s: used %d times' % (count, record[0],record[1])
        count += 1

if __name__ == '__main__':
    with open(bash_history_path, 'r') as f:
        for line in f.readlines():
            check_line(line)

    # set top x to print
    top = 10
    try:
        top = int(sys.argv[1])
    except:
        pass

    print_top(n=top)
