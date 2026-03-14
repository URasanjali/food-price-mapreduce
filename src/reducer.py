#!/usr/bin/env python3
"""
Reducer: Aggregates prices and computes:
  - Average price
  - Min price
  - Max price
  - Count of records
Output: Country | Commodity | Year | AvgPrice | MinPrice | MaxPrice | Count
"""
import sys

def reducer():
    current_key  = None
    total_price  = 0.0
    min_price    = float('inf')
    max_price    = float('-inf')
    count        = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        parts = line.split('\t')
        if len(parts) != 2:
            continue

        key, value = parts[0], parts[1]

        try:
            price = float(value)
        except ValueError:
            continue

        if current_key == key:
            total_price += price
            min_price    = min(min_price, price)
            max_price    = max(max_price, price)
            count       += 1
        else:
            # Output previous key's result
            if current_key is not None:
                avg = total_price / count
                country, commodity, year = current_key.split('|')
                print(f"{country}\t{commodity}\t{year}\t"
                      f"{avg:.2f}\t{min_price:.2f}\t{max_price:.2f}\t{count}")

            # Reset for new key
            current_key = key
            total_price = price
            min_price   = price
            max_price   = price
            count       = 1

    # Don't forget last key
    if current_key is not None:
        avg = total_price / count
        country, commodity, year = current_key.split('|')
        print(f"{country}\t{commodity}\t{year}\t"
              f"{avg:.2f}\t{min_price:.2f}\t{max_price:.2f}\t{count}")

if __name__ == "__main__":
    reducer()
