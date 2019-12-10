import os
import time
import zipfile


# 1.需要备份的文件与目录将会在同一列表
source = ['"D:\\test"','D:\\PycharmProjects']
# 2.备份文件必须存储在一个主备份目录之中

target_dir = 'E:\\backup'

# 如果目标目录不存在则创建目录
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
# 3.备份文件将打包压缩成 zip 文件。
# 4.将当前日期作为主备份目录下的子目录名称
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 将当前时间作为 zip 文件的文件名
now = time.strftime('%H%M%S')

# 添加一条来自用户的注释以创建
comment = input('Enter a comment - -> ')
# 检查是否有评论更新文件中
if len(comment) == 0:
    target = today + os.sep + now + '.zip' # zip文件
else:
    target = today + os.sep + now + '_' + \
             comment.replace(' ', '_') + '.zip'
# 如果子目录尚不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# 5.使用命令zip将文件打包
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

z = zipfile.ZipFile(target, 'r')
for f in z.namelist():
    print(f)


for i in z.infolist():
    print(i.file_size, i.header_offset)
