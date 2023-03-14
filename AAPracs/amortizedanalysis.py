import re
set_data_structure = ''
def line_by_line(input_file):
f = open(input_file, "r")
arr = f.read().split('\n')
# Remove blanks
arr = list(filter(None, arr))
# trim each element
arr = [x.strip() for x in arr]
return arr
line_by_line("/content/sample_data/input")
# Pattern matching for stack
stack_str = "(def top\(\):|def pop\(\):|def push\(a: int\):)"
data_structure_dict = {"stack": {"name": 'stack', 'regex_str': stack_str}}
print(data_structure_dict)
for ds in data_structure_dict:
a = data_structure_dict[ds]
re_str = a['regex_str']
x = re.search(re_str, 'def pop():')
if x: