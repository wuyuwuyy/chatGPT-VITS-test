import sys
import subprocess

# 获取用户输入的库名称
libraries = input("请输入需要安装的库名称（用空格隔开）：").strip().split(" ")

# 存储安装失败的库
failed_libraries = []

# 循环安装库
for library in libraries:
    result = subprocess.run(["pip", "install", "--user",library])
    if result.returncode == 0:
        print("库 '{}' 安装成功".format(library))
    else:
        print("库 '{}' 安装失败".format(library), file=sys.stderr)
        failed_libraries.append(library)

# 输出安装失败的库
if failed_libraries:
    print("以下库安装失败：", file=sys.stderr)
    for library in failed_libraries:
        print("- {}".format(library), file=sys.stderr)
