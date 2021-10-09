import re
def re_file(line):
    RE_LINE = re.compile(r'^(\S+){1} - -\s*(\[.*])\s*(".*")\s(\d+)\s(\d+)\s+"-"\s+"(.*)')
    return RE_LINE.findall(line)


list_of_parsed_raw = []
with open(r'nginx_logs.txt') as file:
    for line in file:
        parsed_raw = re_file(line)
        list_of_parsed_raw.append(parsed_raw)
print(*list_of_parsed_raw[0:20], sep = "\n")



