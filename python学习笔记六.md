>微信公众号： 点击蓝色字体<font color=blue size=2.5>小白图像与视觉</font>进行关注
>
>关于技术、关注`yysilence00`。有问题或建议，请公众号留言

下面主要编写一个实用脚本
------------------------------
> * 整理知识，学习笔记
> * 发布日记，杂文，所见所想

## 问题

我们希望解决的问题如下：

> 我想要一款程序来备份我所有的重要文件。

虽然这是一个简单的问题，但是其中并没有足够的信息有助于让我们开始规划一份解决方案。我们需要进行一些*分析（Analysis）*。例如，我们应该如何指定_哪些_文件是我们需要备份的？它们应该_如何_进行备份？储存到_哪里_?

在正确地分析了这些问题过后，我们便开始*设计（Design）*我们的程序。我们将列出一份关于我们的程序应如何运转的清单。在这个案例中，我已经编写了如下清单来说明_我_将如何工作。如果由你来设计程序，你可能不会做出同样的分析，因为每个人都有其自己的行事方式，所以出现不同是完全正常、且正确的。

- 需要备份的文件与目录应在一份列表中予以指定。
- 备份必须存储在一个主备份目录中。
- 备份文件将打包压缩成 zip 文件。
- zip 压缩文件的文件名由当前日期与时间构成。
- 我们使用在任何 GNU/Linux 或 Unix 发行版中都会默认提供的标准 `zip` 命令进行打包。在这里你需要了解到只要有命令行界面，你就可以使用任何需要用到的压缩或归档命令。

###第一版
```python
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

```

输出：

```bash
(py36) D:\PycharmProjects>python backup_ver1.py
Zip command is:
zip -r E:\backup\20191202200220.zip "D:\test" D:\PycharmProjects
Running:
  adding: test/ (248 bytes security) (stored 0%)
  adding: PycharmProjects/ (248 bytes security) (stored 0%)
  adding: PycharmProjects/.idea/ (248 bytes security) (stored 0%)
  adding: PycharmProjects/.idea/misc.xml (160 bytes security) (deflated 39%)
  adding: PycharmProjects/.idea/modules.xml (160 bytes security) (deflated 39%)
  adding: PycharmProjects/.idea/PycharmProjects.iml (160 bytes security) (deflated 42%)

  adding: PycharmProjects/.idea/vcs.xml (160 bytes security) (deflated 23%)
  adding: PycharmProjects/.idea/workspace.xml (160 bytes security) (deflated 73%)
  adding: PycharmProjects/all.log (160 bytes security) (deflated 77%)
  adding: PycharmProjects/backup_ver1.py (160 bytes security) (deflated 32%)
  adding: PycharmProjects/backup_ver2.py (160 bytes security) (deflated 41%)
  adding: PycharmProjects/backup_ver3.py (160 bytes security) (deflated 44%)
  adding: PycharmProjects/break.py (160 bytes security) (deflated 22%)
  adding: PycharmProjects/continue.py (160 bytes security) (deflated 24%)
  adding: PycharmProjects/ds_str_methods.py (160 bytes security) (deflated 40%)
  adding: PycharmProjects/ds_using_dict.py (160 bytes security) (deflated 42%)
  adding: PycharmProjects/ds_using_list.py (160 bytes security) (deflated 43%)
  adding: PycharmProjects/ds_using_reference.py (160 bytes security) (deflated 47%)
  adding: PycharmProjects/ds_using_seq.py (160 bytes security) (deflated 56%)
  adding: PycharmProjects/ds_using_set.py (160 bytes security) (deflated 32%)
  adding: PycharmProjects/ds_using_tuple.py (160 bytes security) (deflated 47%)
  adding: PycharmProjects/expression.py (160 bytes security) (deflated 33%)
  adding: PycharmProjects/for.py (160 bytes security) (deflated 26%)
  adding: PycharmProjects/from_import.py (160 bytes security) (deflated 43%)
  adding: PycharmProjects/from_logging_import_handles.py (160 bytes security) (deflated
 53%)
  adding: PycharmProjects/function1.py (160 bytes security) (deflated 27%)
  adding: PycharmProjects/function_docstring.py (160 bytes security) (deflated 39%)
  adding: PycharmProjects/function_global.py (160 bytes security) (deflated 29%)
  adding: PycharmProjects/function_keyword.py (160 bytes security) (deflated 31%)
  adding: PycharmProjects/function_local.py (160 bytes security) (deflated 18%)
  adding: PycharmProjects/function_param.py (160 bytes security) (deflated 54%)
  adding: PycharmProjects/function_return.py (160 bytes security) (deflated 57%)
  adding: PycharmProjects/function_varargs.py (160 bytes security) (deflated 44%)
  adding: PycharmProjects/funcyion_default.py (160 bytes security) (deflated 27%)
  adding: PycharmProjects/if.py (160 bytes security) (deflated 37%)
  adding: PycharmProjects/logging_test.py (160 bytes security) (deflated 31%)
  adding: PycharmProjects/module_using_name.py (160 bytes security) (deflated 30%)
  adding: PycharmProjects/module_using_sys.py (160 bytes security) (deflated 31%)
  adding: PycharmProjects/myfirstproject.py (160 bytes security) (deflated 29%)
  adding: PycharmProjects/mymodule.py (160 bytes security) (deflated 2%)
  adding: PycharmProjects/mymodule_demo.py (160 bytes security) (deflated 22%)
  adding: PycharmProjects/mymodule_demo2.py (160 bytes security) (deflated 26%)
  adding: PycharmProjects/operator.ipynb (160 bytes security) (deflated 71%)
  adding: PycharmProjects/stdlib_logging.py (160 bytes security) (deflated 39%)
  adding: PycharmProjects/str_format.py (160 bytes security) (deflated 43%)
  adding: PycharmProjects/var.py (160 bytes security) (deflated 33%)
  adding: PycharmProjects/while.py (160 bytes security) (deflated 41%)
  adding: PycharmProjects/__pycache__/ (248 bytes security) (stored 0%)
  adding: PycharmProjects/__pycache__/logging_test.cpython-36.pyc (160 bytes security)
(deflated 19%)
  adding: PycharmProjects/__pycache__/module_using_name.cpython-36.pyc (160 bytes secur
ity) (deflated 25%)
  adding: PycharmProjects/__pycache__/module_using_sys.cpython-36.pyc (160 bytes securi
ty) (deflated 26%)
  adding: PycharmProjects/__pycache__/mymodule.cpython-36.pyc (160 bytes security) (def
lated 29%)
Successful backup to E:\backup\20191202200220.zip

```

###第二版
```python
import os
import time

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

# zip文件
target = today + os.sep + now + '.zip'
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
```


输出：
```bash
(py36) D:\PycharmProjects>python backup_ver2.py just a comment
Zip command is:
zip -r E:\backup\20191202\201810.zip "D:\test" D:\PycharmProjects
Running:
  adding: test/ (248 bytes security) (stored 0%)
  adding: PycharmProjects/ (248 bytes security) (stored 0%)
  adding: PycharmProjects/.idea/ (248 bytes security) (stored 0%)
  adding: PycharmProjects/.idea/misc.xml (160 bytes security) (deflated 39%)
  adding: PycharmProjects/.idea/modules.xml (160 bytes security) (deflated 39%)
  adding: PycharmProjects/.idea/PycharmProjects.iml (160 bytes security) (deflated 42%)

  adding: PycharmProjects/.idea/vcs.xml (160 bytes security) (deflated 23%)
  adding: PycharmProjects/.idea/workspace.xml (160 bytes security) (deflated 73%)
  adding: PycharmProjects/all.log (160 bytes security) (deflated 77%)
  adding: PycharmProjects/backup_ver1.py (160 bytes security) (deflated 32%)
  adding: PycharmProjects/backup_ver2.py (160 bytes security) (deflated 41%)
  adding: PycharmProjects/backup_ver3.py (160 bytes security) (deflated 44%)
  adding: PycharmProjects/break.py (160 bytes security) (deflated 22%)
  adding: PycharmProjects/continue.py (160 bytes security) (deflated 24%)
  adding: PycharmProjects/ds_str_methods.py (160 bytes security) (deflated 40%)
  adding: PycharmProjects/ds_using_dict.py (160 bytes security) (deflated 42%)
  adding: PycharmProjects/ds_using_list.py (160 bytes security) (deflated 43%)
  adding: PycharmProjects/ds_using_reference.py (160 bytes security) (deflated 47%)
  adding: PycharmProjects/ds_using_seq.py (160 bytes security) (deflated 56%)
  adding: PycharmProjects/ds_using_set.py (160 bytes security) (deflated 32%)
  adding: PycharmProjects/ds_using_tuple.py (160 bytes security) (deflated 47%)
  adding: PycharmProjects/expression.py (160 bytes security) (deflated 33%)
  adding: PycharmProjects/for.py (160 bytes security) (deflated 26%)
  adding: PycharmProjects/from_import.py (160 bytes security) (deflated 43%)
  adding: PycharmProjects/from_logging_import_handles.py (160 bytes security) (deflated
 53%)
  adding: PycharmProjects/function1.py (160 bytes security) (deflated 27%)
  adding: PycharmProjects/function_docstring.py (160 bytes security) (deflated 39%)
  adding: PycharmProjects/function_global.py (160 bytes security) (deflated 29%)
  adding: PycharmProjects/function_keyword.py (160 bytes security) (deflated 31%)
  adding: PycharmProjects/function_local.py (160 bytes security) (deflated 18%)
  adding: PycharmProjects/function_param.py (160 bytes security) (deflated 54%)
  adding: PycharmProjects/function_return.py (160 bytes security) (deflated 57%)
  adding: PycharmProjects/function_varargs.py (160 bytes security) (deflated 44%)
  adding: PycharmProjects/funcyion_default.py (160 bytes security) (deflated 27%)
  adding: PycharmProjects/if.py (160 bytes security) (deflated 37%)
  adding: PycharmProjects/logging_test.py (160 bytes security) (deflated 31%)
  adding: PycharmProjects/module_using_name.py (160 bytes security) (deflated 30%)
  adding: PycharmProjects/module_using_sys.py (160 bytes security) (deflated 31%)
  adding: PycharmProjects/myfirstproject.py (160 bytes security) (deflated 29%)
  adding: PycharmProjects/mymodule.py (160 bytes security) (deflated 2%)
  adding: PycharmProjects/mymodule_demo.py (160 bytes security) (deflated 22%)
  adding: PycharmProjects/mymodule_demo2.py (160 bytes security) (deflated 26%)
  adding: PycharmProjects/operator.ipynb (160 bytes security) (deflated 71%)
  adding: PycharmProjects/stdlib_logging.py (160 bytes security) (deflated 39%)
  adding: PycharmProjects/str_format.py (160 bytes security) (deflated 43%)
  adding: PycharmProjects/var.py (160 bytes security) (deflated 33%)
  adding: PycharmProjects/while.py (160 bytes security) (deflated 41%)
  adding: PycharmProjects/__pycache__/ (248 bytes security) (stored 0%)
  adding: PycharmProjects/__pycache__/logging_test.cpython-36.pyc (160 bytes security)
(deflated 19%)
  adding: PycharmProjects/__pycache__/module_using_name.cpython-36.pyc (160 bytes secur
ity) (deflated 25%)
  adding: PycharmProjects/__pycache__/module_using_sys.cpython-36.pyc (160 bytes securi
ty) (deflated 26%)
  adding: PycharmProjects/__pycache__/mymodule.cpython-36.pyc (160 bytes security) (def
lated 29%)
Successful backup to E:\backup\20191202\201810.zip


```

###第三版

```python
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

```

输出：
```bash
Enter a comment - -> yanyong
Zip command is:
zip -r E:\backup\20191202\201940_yanyong.zip "D:\test" D:\PycharmProjects
Running:
  adding: test/ (248 bytes security) (stored 0%)
  adding: PycharmProjects/ (248 bytes security) (stored 0%)
  adding: PycharmProjects/.idea/ (248 bytes security) (stored 0%)
  adding: PycharmProjects/.idea/misc.xml (160 bytes security) (deflated 39%)
  adding: PycharmProjects/.idea/modules.xml (160 bytes security) (deflated 39%)
  adding: PycharmProjects/.idea/PycharmProjects.iml (160 bytes security) (deflated 42%)

  adding: PycharmProjects/.idea/vcs.xml (160 bytes security) (deflated 23%)
  adding: PycharmProjects/.idea/workspace.xml (160 bytes security) (deflated 73%)
  adding: PycharmProjects/all.log (160 bytes security) (deflated 77%)
  adding: PycharmProjects/backup_ver1.py (160 bytes security) (deflated 32%)
  adding: PycharmProjects/backup_ver2.py (160 bytes security) (deflated 41%)
  adding: PycharmProjects/backup_ver3.py (160 bytes security) (deflated 44%)
  adding: PycharmProjects/break.py (160 bytes security) (deflated 22%)
  adding: PycharmProjects/continue.py (160 bytes security) (deflated 24%)
  adding: PycharmProjects/ds_str_methods.py (160 bytes security) (deflated 40%)
  adding: PycharmProjects/ds_using_dict.py (160 bytes security) (deflated 42%)
  adding: PycharmProjects/ds_using_list.py (160 bytes security) (deflated 43%)
  adding: PycharmProjects/ds_using_reference.py (160 bytes security) (deflated 47%)
  adding: PycharmProjects/ds_using_seq.py (160 bytes security) (deflated 56%)
  adding: PycharmProjects/ds_using_set.py (160 bytes security) (deflated 32%)
  adding: PycharmProjects/ds_using_tuple.py (160 bytes security) (deflated 47%)
  adding: PycharmProjects/expression.py (160 bytes security) (deflated 33%)
  adding: PycharmProjects/for.py (160 bytes security) (deflated 26%)
  adding: PycharmProjects/from_import.py (160 bytes security) (deflated 43%)
  adding: PycharmProjects/from_logging_import_handles.py (160 bytes security) (deflated
 53%)
  adding: PycharmProjects/function1.py (160 bytes security) (deflated 27%)
  adding: PycharmProjects/function_docstring.py (160 bytes security) (deflated 39%)
  adding: PycharmProjects/function_global.py (160 bytes security) (deflated 29%)
  adding: PycharmProjects/function_keyword.py (160 bytes security) (deflated 31%)
  adding: PycharmProjects/function_local.py (160 bytes security) (deflated 18%)
  adding: PycharmProjects/function_param.py (160 bytes security) (deflated 54%)
  adding: PycharmProjects/function_return.py (160 bytes security) (deflated 57%)
  adding: PycharmProjects/function_varargs.py (160 bytes security) (deflated 44%)
  adding: PycharmProjects/funcyion_default.py (160 bytes security) (deflated 27%)
  adding: PycharmProjects/if.py (160 bytes security) (deflated 37%)
  adding: PycharmProjects/logging_test.py (160 bytes security) (deflated 31%)
  adding: PycharmProjects/module_using_name.py (160 bytes security) (deflated 30%)
  adding: PycharmProjects/module_using_sys.py (160 bytes security) (deflated 31%)
  adding: PycharmProjects/myfirstproject.py (160 bytes security) (deflated 29%)
  adding: PycharmProjects/mymodule.py (160 bytes security) (deflated 2%)
  adding: PycharmProjects/mymodule_demo.py (160 bytes security) (deflated 22%)
  adding: PycharmProjects/mymodule_demo2.py (160 bytes security) (deflated 26%)
  adding: PycharmProjects/operator.ipynb (160 bytes security) (deflated 71%)
  adding: PycharmProjects/stdlib_logging.py (160 bytes security) (deflated 39%)
  adding: PycharmProjects/str_format.py (160 bytes security) (deflated 43%)
  adding: PycharmProjects/var.py (160 bytes security) (deflated 33%)
  adding: PycharmProjects/while.py (160 bytes security) (deflated 41%)
  adding: PycharmProjects/__pycache__/ (248 bytes security) (stored 0%)
  adding: PycharmProjects/__pycache__/logging_test.cpython-36.pyc (160 bytes security)
(deflated 19%)
  adding: PycharmProjects/__pycache__/module_using_name.cpython-36.pyc (160 bytes secur
ity) (deflated 25%)
  adding: PycharmProjects/__pycache__/module_using_sys.cpython-36.pyc (160 bytes securi
ty) (deflated 26%)
  adding: PycharmProjects/__pycache__/mymodule.cpython-36.pyc (160 bytes security) (def
lated 29%)
Successful backup to E:\backup\20191202\201940_yanyong.zip
test/
PycharmProjects/
PycharmProjects/.idea/
PycharmProjects/.idea/misc.xml
PycharmProjects/.idea/modules.xml
PycharmProjects/.idea/PycharmProjects.iml
PycharmProjects/.idea/vcs.xml
PycharmProjects/.idea/workspace.xml
PycharmProjects/all.log
PycharmProjects/backup_ver1.py
PycharmProjects/backup_ver2.py
PycharmProjects/backup_ver3.py
PycharmProjects/break.py
PycharmProjects/continue.py
PycharmProjects/ds_str_methods.py
PycharmProjects/ds_using_dict.py
PycharmProjects/ds_using_list.py
PycharmProjects/ds_using_reference.py
PycharmProjects/ds_using_seq.py
PycharmProjects/ds_using_set.py
PycharmProjects/ds_using_tuple.py
PycharmProjects/expression.py
PycharmProjects/for.py
PycharmProjects/from_import.py
PycharmProjects/from_logging_import_handles.py
PycharmProjects/function1.py
PycharmProjects/function_docstring.py
PycharmProjects/function_global.py
PycharmProjects/function_keyword.py
PycharmProjects/function_local.py
PycharmProjects/function_param.py
PycharmProjects/function_return.py
PycharmProjects/function_varargs.py
PycharmProjects/funcyion_default.py
PycharmProjects/if.py
PycharmProjects/logging_test.py
PycharmProjects/module_using_name.py
PycharmProjects/module_using_sys.py
PycharmProjects/myfirstproject.py
PycharmProjects/mymodule.py
PycharmProjects/mymodule_demo.py
PycharmProjects/mymodule_demo2.py
PycharmProjects/operator.ipynb
PycharmProjects/stdlib_logging.py
PycharmProjects/str_format.py
PycharmProjects/var.py
PycharmProjects/while.py
PycharmProjects/__pycache__/
PycharmProjects/__pycache__/logging_test.cpython-36.pyc
PycharmProjects/__pycache__/module_using_name.cpython-36.pyc
PycharmProjects/__pycache__/module_using_sys.cpython-36.pyc
PycharmProjects/__pycache__/mymodule.cpython-36.pyc
0 0
0 179
0 369
312 565
289 936
505 1294
185 1778
9700 2100
955 4900
942 5296
1076 6114
1494 6926
483 7944
353 8496
690 8941
1174 9538
1047 10404
1312 11186
1297 12072
341 12822
1016 13234
121 13958
469 14218
1398 14739
1375 15715
156 16561
353 16853
177 17255
225 17565
221 17905
733 18270
347 18788
1145 19121
110 19944
1024 20209
823 21023
672 21774
738 22429
97 23126
83 23378
76 23636
91 23877
1666 24127
788 24794
1834 25456
922 26687
878 27478
0 28168
591 28370
789 29053
964 29853
273 30780
```

### 软件开发流程

我们已经经历了开发一款软件的流程中的各个`阶段（Phases）`。现在可以将这些阶段总结如下：

1. What/做什么（分析）
2. How/怎么做（设计）
3. Do It/开始做（执行）
4. Test/测试（测试与修复错误）
5. Use/使用（操作或开发）
6. Maintain/维护（改进）

编写程序时推荐的一种方式是遵循我们在编写备份脚本时所经历的步骤：进行分析与设计；开始实现一个简单版本；测试并修复错误；开始使用以确保工作状况皆如期望那般。现在，你可以添加任何你所希望拥有的功能，并继续去重复这一“开始做—测试—使用”循环，需要做多少次就去做多少次。
**更多请长按扫码关注**：
<center>
<img src="https://note.youdao.com/yws/api/personal/file/WEB4c5a2ba9b0d3fcdf7fa67543141b1cc0?method=download&shareKey=d962d52c470d4121f8d0c474be34c56f" width="350" hegiht="350" align=center/>
</center>