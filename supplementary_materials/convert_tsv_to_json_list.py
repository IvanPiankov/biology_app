import argparse
from pathlib import Path
import pandas as pd
import json


def main(input_tsv: Path, output_json: Path):
    data_tsv = pd.read_csv(input_tsv, sep='\t', header=0)
    data_tsv.rename(columns={'Unnamed: 0': 'Patient_id'}, inplace=True)
    result = data_tsv.to_json(orient="records")
    parsed = json.loads(result)
    with open(output_json, 'w') as out:
        json.dump(parsed, out, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Convert  tsv file to list with json objects')
    parser.add_argument('-i', '--input_tsv', help='Input tsv file')
    parser.add_argument('-o', '--output_json', help='Output json file')
    args = parser.parse_args()
    main(input_tsv=args.input_tsv, output_json=args.output_json)

