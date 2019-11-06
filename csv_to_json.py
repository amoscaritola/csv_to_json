import csv
import json
import argparse

# Python3
# https://github.com/amoscaritola
# 2019-10-23

def write_json(data, json_file, output_format):
	"""Convert csv data into json and write it"""
	with open(json_file, "w", encoding="utf-8",) as f:
		if output_format == "pretty":
			f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False))
		else:
			f.write(json.dumps(data, ensure_ascii=False))

def read_csv(csv_file, json_file, o_format):
	"""Read the csv file and use first row as keys"""
	csv_rows = []
	with open(csv_file, "r", encoding="utf-8") as csvfile:
		reader = csv.DictReader(csvfile)
		title = reader.fieldnames
		for row in reader:
			csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
		write_json(csv_rows, json_file, o_format)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'-i', '--input', dest='input_file',
		help='Path to csv input file')
	parser.add_argument(
		'-o', '--output', dest='output_file',
		help='Path to the json output file')
	parser.add_argument(
		'-f', '--format', dest='output_format', choices=['dump', 'pretty'], default='pretty',
		help='Select if the json output will be regular or pretty format ')
	args = parser.parse_args()

	if args.input_file == None:
		print('csv_json.py -i <path to inputfile> -o <path to outputfile> -f <dump/pretty>')
		exit()
	if args.output_file == None:
		print('csv_json.py -i <path to inputfile> -o <path to outputfile> -f <dump/pretty>')
		exit()
		
	read_csv(args.input_file, args.output_file, args.output_format)

if __name__ == '__main__':
	main()
