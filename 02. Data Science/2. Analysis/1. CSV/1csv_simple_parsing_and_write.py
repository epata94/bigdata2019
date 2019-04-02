# 목적: CSV 파일 읽고 쓰기
import sys

input_file = sys.argv[1]  # supplier_data.csv
output_file = sys.argv[2] # output_files/1output_index_false.csv

with open(input_file, 'r', newline='') as filereader:
	with open(output_file, 'w', newline='') as filewriter:
		header = filereader.readline() # 헤더행
		header = header.strip()
		header_list = header.split(',')
		print(header_list)
		filewriter.write(','.join(map(str,header_list))+'\n')
		for row in filereader:
			row = row.strip()
			row_list = row.split(',')
			print(row_list)
			filewriter.write(','.join(map(str,row_list))+'\n')