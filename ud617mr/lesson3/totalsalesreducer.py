#!/usr/bin/python
import sys


def reducer():
    sales_total = 0
    sales_count = 0
    old_key = None

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        sales_total += float(data[1])
        sales_count += 1

    print("{0}\t{1}".format(sales_count,sales_total))

reducer()
