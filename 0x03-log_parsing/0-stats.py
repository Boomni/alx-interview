#!/usr/bin/python3
"""
Log parsing

Script that reads stdin line by line and computes metrics:

    Input format:
        <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
        <status code> <file size>
        (if the format is not this one, the line must be skipped)

    After every 10 lines and/or a keyboard interruption (CTRL + C),
    print these statistics from the beginning:
        Total file size: File size: <total size>
        where <total size> is the sum of all previous <file size>
        (see input format above)
        Number of lines by status code:
            possible status code:
                200, 301, 400, 401, 403, 404, 405 and 500
            if a status code doesn’t appear or is not an integer,
            don’t print anything for this status code

            format: <status code>: <number>
            status codes should be printed in ascending order
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
