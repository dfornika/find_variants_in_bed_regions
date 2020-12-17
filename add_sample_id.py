#!/usr/bin/env python3

import argparse
import csv
import os.path
import re

def main(args):
    for input_file in args.input_files:
        input_file_basename = os.path.basename(input_file)
        sample_id = input_file_basename.split(args.sample_id_delimiter)[0]

        with open(input_file, 'r') as f:
            for line in f:
                line = line.rstrip()
                if re.match(args.header_regex, line):
                    if args.no_header:
                        continue
                    else:
                        print(args.field_delimiter.join(['sample_id', line]))
                else: 
                    print(args.field_delimiter.join([sample_id, line]))
        


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_files', nargs='+')
    parser.add_argument('--sample-id-delimiter', default='.')
    parser.add_argument('--field-delimiter', default='\t')
    parser.add_argument('--header-regex')
    parser.add_argument('--no-header', action='store_true')
                        
    args = parser.parse_args()
    main(args)
