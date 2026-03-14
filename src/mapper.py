#!/usr/bin/env python3
import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin)
    header_skipped = False

    for row in reader:
        if not header_skipped:
            header_skipped = True
            continue

        try:
            if len(row) < 17:
                continue

            country   = row[1].strip()
            commodity = row[7].strip()
            year      = row[15].strip()
            price_str = row[16].strip()

            if not country or not commodity or not year or not price_str:
                continue

            price = float(price_str)
            print(f"{country}|{commodity}|{year}\t{price}")

        except (ValueError, IndexError):
            continue

if __name__ == "__main__":
    mapper()
