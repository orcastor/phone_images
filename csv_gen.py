import os
import csv
from natsort import natsorted

# 获取当前目录下的所有文件名
files = os.listdir('./android')

# 过滤出文件名
file_names = [file for file in files if os.path.isfile(os.path.join('./android', file))]

# 对文件名进行自然排序
file_names_sorted = natsorted(file_names)

# 写入 CSV 文件
with open('./android/android', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['File Name'])
    for file_name in file_names_sorted:
        writer.writerow([file_name.replace('.jpg', '')])

print("CSV 文件已生成并按照文件名进行自然排序。")