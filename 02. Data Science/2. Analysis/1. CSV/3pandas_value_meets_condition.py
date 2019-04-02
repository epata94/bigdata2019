# 목적: pandas 문법으로 특정 행을 필터링하기
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)

data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name']\
.str.contains('Z')) | (data_frame['Cost'] > 600.0), :]
# loc 내부에 ,를 생략하면 에러발생

data_frame_value_meets_condition.to_csv(output_file, index=False)