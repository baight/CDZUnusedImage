
# 该脚本功能是，查找脚本所在目录（包括子目录）中，未使用到的图片资源
# 该脚本 基于 python3，需要安装 python3运行环境
# 把该脚本 放于 xcode工程 根目录，命令行运行之（$> python3 /目录/CDZUnusedImage.py）即可，
# 输出 未使用的 图片名称

# 脚本 寻找所有 xxx.imageset 文件夹，获得 xxx字符串
# 查找 "xxx" 字符串，是否在 .h .m .xib .storyboard 文件中 出现过
# 出现过，则认为该图片使用过，反之认为没有使用过
# 2016-06-16

import sys,os
from mylib import *
from color_print import *

# 跳转到当前目录
curDir = sys.path[0];
os.chdir(curDir)

#--------------------配 置-------------------->
# 图片文件后缀名
imageFileSuffixs = (".png", ".PNG", ".jpg", "JPG", '.jpeg', '.JPEG')

# 用于判断图片是否使用过的 代码文件后缀名，大小写敏感
# the suffixs of your code
codeFileSuffixs = (".h", ".m", ".xib", ".storyboard")

# 需要忽略的图片文件，大小写敏感
# the image names to ignore
ignoreFiles = set(("ignorePictur0", "ignorePictur1"))

# 需要忽略的图片名称前缀，大小写敏感。如果 BBS_abc.png，那么它将只会寻找 abc.png，忽略掉了前缀
# the image names prefix to ignore
ignorePrefix = ["BBS_",]

# 需要忽略的文件夹
# the dir names to ignore
ignoreDirs = ("app.xcassets", ".bundle", "Example")
#--------------------配 置--------------------<


#--------------------工 作-------------------->
print ("--> 初始化...")
# 寻找所有图片名称
xcimageNameList = GetXcassetsImageNameListInDirectory(curDir, ignoreDirs=ignoreDirs, ignoreFiles=ignoreFiles,
                                                      ignorePrefix=ignorePrefix)

notXcimageNameList = GetNotXcassetsImageNameListInDirectory(curDir, ignoreDirs=ignoreDirs, ignoreFiles=ignoreFiles,
                                                            imageFileSuffixs=imageFileSuffixs,
                                                            ignorePrefix=ignorePrefix)
imageNameList = xcimageNameList + notXcimageNameList
print("--> 总共查找到 %d 张图片" % (len(imageNameList)))

# 获取源文件列表
sourceFilePathList = GetFileListOfSuffix(curDir, codeFileSuffixs)
print("--> 总共查找到 %d 个源文件" % (len(sourceFilePathList)))

print ("--> 正在筛选未使用过的图片...")
unusedImageSet = set(imageNameList)
for filePath in sourceFilePathList:
    used = IsFileContainTextSet(filePath, unusedImageSet)
    unusedImageSet = unusedImageSet - used

index = 0
for unusedImage in unusedImageSet:
    color_text = ColorText()
    color_text.appendColorText(str(index+1) + "-> ")
    color_text.appendColorText(unusedImage, TextColor.Cyan)
    color_text.appendColorText(' is not used')
    printColorText(color_text)
    index = index + 1

print ("--> 查找结束")
#--------------------工 作--------------------<


# created by baight 303730915@qq.com

