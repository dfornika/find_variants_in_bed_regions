# Find Variants in .bed Regions

# add_sample_id.py
By default, the `variants.tsv` files produced by `ivar variants` do not include a field for the sample ID. That information is normally included in the filename.
But if we want to concatenate many `variants.tsv` files together, that information is lost. This script takes the sample ID from the filename and adds an extra field

This script is made to be as generic as possible, so it should be compatible with other tsv/csv files that have their sample ID as the first part of the filename but
not in the body of the file. Use the `--sample-id-delimiter` flag to specify which character to split the filename on. The first element will be used as the sample ID after
splitting with that character. Use the `--field-delimiter` flag to specify the delimiter used in the input file (`'\t'` for `.tsv`, `','` for `.csv`. Use the `--no-header`
flag to suppress printing the header in the output. The header is identified using the `--header-regex`. For `ivar` `variants.tsv` files, use `^REGION` to match the header.

## Usage

```
usage: add_sample_id.py [-h] [--sample-id-delimiter SAMPLE_ID_DELIMITER] [--field-delimiter FIELD_DELIMITER] [--header-regex HEADER_REGEX] [--no-header] input_files [input_files ...]

positional arguments:
  input_files

optional arguments:
  -h, --help            show this help message and exit
  --sample-id-delimiter SAMPLE_ID_DELIMITER
  --field-delimiter FIELD_DELIMITER
  --header-regex HEADER_REGEX
  --no-header
```

# find_variants_in_bed_regions.py
Take variants.tsv data from `stdin`, and print those that fall within the regions defined by a `.bed` file to `stdout`. Optionally filter by minimum and maximum alternate allele frequency.

The `--region-field-num` flag is used to indicate which field is the `REGION` field in the input stream. By default, it is `0` (default `variants.tsv` format). If a `sample_id` or other fields
have been prepended, increase by the number of prepended fields. Set this value to `1` when using with the `add_sample_id.py` script above.

## Usage
```
usage: find_variants_in_bed_regions.py [-h] [--bed BED] [--region-field-num REGION_FIELD_NUM] [--min-alt-freq MIN_ALT_FREQ] [--max-alt-freq MAX_ALT_FREQ]

optional arguments:
  -h, --help            show this help message and exit
  --bed BED
  --region-field-num REGION_FIELD_NUM
  --min-alt-freq MIN_ALT_FREQ
  --max-alt-freq MAX_ALT_FREQ
```

# Combined usage

Find any samples that have ambiguous variants within primer regions (defined in `nCoV-2019.bed`).

```
add_sample_id.py --header-regex '^REGION' --no-header *.variants.tsv | find_variants_in_bed_regions.py --bed nCoV-2019.bed --min-alt-freq 0.25 --max-alt-freq 0.75 --region-field-num 1
```
