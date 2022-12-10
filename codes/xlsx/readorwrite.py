import pyexcel as p
from devtools import pprint

my_dict = p.get_dict(file_name="marks1.xlsx", name_columns_by_row=0)

pprint(my_dict)

data = [
    [1, 'Ajeeb', 'Engineer'],
    [2, 'Dr Nimitha Aboobaker', 'Professor'],
]
p.save_as(array=data, dest_file_name="jobs.xlsx")