import os
import shutil
u_dict = {'roots': [], 'dirs': []}
for root, dirs, files in os.walk('my_project'):
    if 'templates' == root.split('\\')[-1]:
        for i in dirs:
            u_dict['roots'].append(root)
            u_dict['dirs'].append(i)
for i, val in enumerate(u_dict['roots']):
    #print(val+r'\templates')
    shutil.copytree(val+r'\\' + u_dict['dirs'][i], r'my_project\templates\\' + u_dict['dirs'][i])