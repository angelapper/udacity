#!/usr/bin/python
# Find the monetary value for the highest individual sale for each separate store.
import sys


def reducer():
    sales_max = 0
    old_key = None

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        this_key, this_sale = data

        if old_key and old_key != this_key:
            print("{0}\t{1}".format(old_key, sales_max))
            sales_max = 0

        old_key = this_key
        # keep remember to convert string to number to compare
        this_sale = float(this_sale)
        if this_sale > sales_max:
            sales_max = float(this_sale)

    if old_key is not None:
        print("{0}\t{1}".format(old_key, sales_max))

reducer()
