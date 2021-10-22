parsed_dict = {'ip': [], 'date': [], 'act': [], 'numbs': [], 'protocol': []}
file_1 = open(r'E:\Users\NeoHan\PycharmProjects\HomeWork\nginx_logs.txt', 'r', encoding='utf-8')
for i in file_1:
    f_string = file_1.readline()
    ip = f_string.find('- -')
    parsed_dict['ip'].append(f_string[:ip])
    parsed_dict['date'].append(f_string[f_string.find('[')+1:f_string.find(']')])
    act = [f_string.find('"')+1, f_string.find('"', f_string.find('"')+1)]
    parsed_dict['act'].append(f_string[act[0]:act[1]])
    numbs = [act[1]+1, f_string.find('"', act[1]+1)]
    parsed_dict['numbs'].append(f_string[numbs[0]+1:numbs[1]-1])
    protocol = [-1, f_string.find('"', -2)]
    parsed_dict['protocol'].append(f_string[f_string.find('"', numbs[1]+4):-2])
file_1.close()
print(parsed_dict)
spamer = ''
set_ips = set(parsed_dict['ip'])
counter = 0
for i in set_ips:
    if counter < parsed_dict['ip'].count(i):
        counter = parsed_dict['ip'].count(i)
        spamer = i
print(spamer)
