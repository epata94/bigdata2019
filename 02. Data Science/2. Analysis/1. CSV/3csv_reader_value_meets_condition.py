# 목적: 파이썬 기본 문법으로 특정 행을 필터링하기
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header = next(filereader)
		filewriter.writerow(header)
		for row_list in filereader:
			supplier = str(row_list[0]).strip()
			# cost = str(row_list[3]).strip('$').replace(',', '')
			cost = str(row_list[3]).strip('$')
			if supplier == 'Supplier Z' or float(cost) > 600.0:
			# Supplier Z 이고 가격이 600 보다 작은 레코드가 있을 때 의미가 있음
			# if float(cost) > 600.0: # 같은 결과가 예상
				filewriter.writerow(row_list)