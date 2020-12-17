#!/usr/bin/env python3

import argparse
import csv
import json
import sys


def parse_bed(bedfile_path):
    bed_records = []
    with open(bedfile_path, 'r') as f:
        for line in f:
            bed_record = {}
            fields = line.rstrip().split('\t')
            bed_record['chrom'] = fields[0]
            bed_record['chromStart'] = int(fields[1])
            bed_record['chromEnd'] = int(fields[2])
            bed_record['name'] = fields[3]
            bed_records.append(bed_record)

    return bed_records


def main(args):
    bed_records = parse_bed(args.bed)
    # print(json.dumps(bed_records))
    for line in sys.stdin:
        line = line.rstrip()
        variants_fields = line.split()
        for bed_record in bed_records:
            chrom_matches = variants_fields[args.region_field_num] == bed_record['chrom']
            in_region = int(variants_fields[args.region_field_num + 1]) >= bed_record['chromStart'] and int(variants_fields[args.region_field_num + 1]) <= bed_record['chromEnd']
            in_alt_freq_range = float(variants_fields[args.region_field_num + 10]) >= args.min_alt_freq and float(variants_fields[args.region_field_num + 10]) <= args.max_alt_freq
            if chrom_matches and in_region and in_alt_freq_range:
                print(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bed')
    parser.add_argument('--region-field-num', type=int, default=0)
    parser.add_argument('--min-alt-freq', type=float, default=0.0)
    parser.add_argument('--max-alt-freq', type=float, default=1.0)
    args = parser.parse_args()
    main(args)
