import os
import time

# 1. 需要备份的文件与目录将被
# 指定在一个列表
# 例如在window下：
source = ['"D:\\test"','D:\\PycharmProjects']
# 2.备份文件存储目标位置
target_dir = 'E:\\backup'

# 3. 备份文件将打包压缩成 zip 文件。
# 4. zip 压缩文件的文件名由当前日期与时间构成。
target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'   # os.sep 变量的使用方式 在 Windows 中它会是 '\\'
# 如果目标目录还不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # 创建目录
# 5. 我们使用 zip 命令将文件打包成 zip 格式
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')