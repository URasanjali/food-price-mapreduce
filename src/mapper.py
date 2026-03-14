#!/usr/bin/env python3
import sys
import csv

def mapper():
    # In Hadoop Streaming, input is provided through stdin
    reader = csv.reader(sys.stdin)
    header_skipped = False

    # Loop through each row in the CSV input
    for row in reader:
        if not header_skipped:
            header_skipped = True
            continue

        try:
            #Check if the row has enough columns
            #If it has fewer than 17 columns, skip the row
            if len(row) < 17:
                continue

            country   = row[1].strip()   # Country name
            commodity = row[7].strip()   # Commodity name
            year      = row[15].strip()  # Year
            price_str = row[16].strip()  # Price as string

            if not country or not commodity or not year or not price_str:
                continue

            price = float(price_str)
            print(f"{country}|{commodity}|{year}\t{price}")

        except (ValueError, IndexError):
            continue

if __name__ == "__main__":
    mapper()
