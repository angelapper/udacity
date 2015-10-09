#!/usr/bin/python
import sys


def mapper():
    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) == 6:
            date, time, store, item, cost, payment = data
            print("{0}\t{1}".format(store, cost))

def make_entry(x):
        return {
            'server_ip':x.group('ip'),
            'uri':x.group('uri'),
            'time':x.group('time'),
            'status_code':x.group('status_code'),
            'referral':x.group('referral'),
            'agent':x.group('agent'),
            }


mapper()
