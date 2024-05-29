import os

# list_dir = os.listdir("./")
# for item in list_dir:
#     if item.endswith(".png") or item.endswith(".jpg") or item.endswith(".jpeg"):
#         with open("./data.txt", "a", encoding='utf-8') as f:
#             f.write(f'''import {item.replace('-', '').replace('.png','').lower()}Img from '@/public/assets/images/tech/{item}';''' + '\n')
        # print(f'''import {item.replace('-', '').replace('.png','').lower()}Img from '@/public/assets/images/tech/{item}';''')

# with open("./data.txt", "w", encoding='utf-8') as f:
#     print(f.read())
#-------------------
list_icons = []
with open('./data.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    for item in data:
        list_icons.append(item.split()[1])
with open('./a_icons.txt', 'w', encoding='utf-8') as f:
    f.write('export {' + '\n')
    for item in list_icons:
        f.write(item +','+ '\n')
    f.write('}' + '\n')
    