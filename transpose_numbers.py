#!/usr/bin/env python3
"""Transpose rows of numbers into tagged columns.

Input: one row per line, numbers separated by commas (spaces are ignored).
Output: one line per column, prefixed by a tag, listing that column's value
        across every row.

Usage:
    python3 transpose_numbers.py                # paste rows, then press Ctrl-D
    python3 transpose_numbers.py data.txt       # read rows from a file

You can edit TAGS below to give the columns custom names. If there are more
columns than tags, the extra ones fall back to Tag1, Tag2, ...
"""

import sys

# Optional custom column names. Leave empty to use Tag1, Tag2, ...
TAGS = ['TO[0.0,0.1]','TO[0.1,0.2]','TO[0.2,0.3]','TO[0.3,0.4]','TO[0.4,0.5]']


def read_rows(source):
    rows = []
    for line in source:
        line = line.strip()
        if not line:
            continue
        # Split on commas, drop empty pieces, convert to float.
        values = [float(x) for x in line.split(',') if x.strip() != '']
        rows.append(values)
    return rows


def tag_for(col_index):
    if col_index < len(TAGS):
        return TAGS[col_index]
    return f'Tag{col_index + 1}'


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            rows = read_rows(f)
    else:
        rows = read_rows(sys.stdin)

    if not rows:
        print('No numbers were provided.')
        return

    n_cols = max(len(r) for r in rows)
    for col in range(n_cols):
        # Pick the value of this column from every row that has it.
        column_values = [str(row[col]) for row in rows if col < len(row)]
        print(f'{tag_for(col)} ' + ' '.join(column_values))


if __name__ == '__main__':
    main()
