#!/usr/bin/python3
"""
Log parsing
"""

import sys


stats: dict = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}
total: int = 0
count: int = 0


def print_stats(stats: dict, total: int) -> None:
    """
    print_stats function

    Format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

    E.g:
    4.21.109.220 - [2023-08-17 01:06:01.445472] "GET /projects/260 HTTP/1.1" 500 813
    """
    print("File size: {}".format(total))
    for key, value in sorted(stats.items()):
        if value != 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            data = line.split()
            if len(data) < 10:
                status = data[-2]
                if status in stats.keys():
                    stats[status] += 1
                total += int(data[-1])
                count += 1
            if count == 10:
                count = 0
                print_stats(stats, total)
    except Exception:
        pass
    finally:
        print_stats(stats, total)
