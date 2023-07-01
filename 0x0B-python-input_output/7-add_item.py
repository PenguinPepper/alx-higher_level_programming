#!/usr/bin/python3
""""Moule contains function that adds given arguments to a file"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


length = len(sys.argv)
arry = []
filename = "add_item.json"

for i in range(1, length):
    arry.append(sys.argv[i])

new_arry = load_from_json_file(filename)
for j in new_arry:
    arry.append(j)
save_to_json_file(arry, filename)
