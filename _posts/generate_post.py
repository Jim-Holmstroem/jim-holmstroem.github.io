#!/usr/bin/env python
from __future__ import print_function

import argparse

import os
import sys

from datetime import datetime


template = """---
layout: post
title: "{title}"
date: {datetime}
categories: {category}
---

"""


def main(title, category, datetime):
    date, _ = (
        datetime.split(' ')[0].split('-'),
        datetime.split(' ')[1].split(':'),
    )
    filename = '{date}-{title}.markdown'.format(
        date='-'.join(date),
        title='-'.join(title.lower().split(' ')),
    )
    if not os.path.isfile(filename):
        with open(filename, 'w') as f:
            f.write(
                template.format(
                    title=title,
                    category=category,
                    datetime=datetime,
                )
            )

    else:
        print('File already exists')
        sys.exit(-1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generates a skeleton post.',
        prog='generate_post',
    )
    now = datetime.now()
    datetime_string = '{}-{}-{} {}:{}'.format(
        now.year,
        now.month,
        now.day,
        now.hour,
        now.minute,
    )
    parser.add_argument(
        '-t', '--title',
        required=True,
        help='Post title'
    )
    parser.add_argument(
        '-c', '--category',
        required=True,
        help='Post category'
    )
    parser.add_argument(
        '-d', '--datetime',
        default=datetime_string,
        help='Post datetime on the format YYYY-MM-DD hh:mm, defaults to now.'
    )

    args = parser.parse_args()

    main(
        title=args.title,
        category=args.category,
        datetime=args.datetime
    )
