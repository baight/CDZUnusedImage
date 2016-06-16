
# 该脚本功能是，查找脚本所在目录（包括子目录）中，未使用到的图片资源
# 该脚本 基于 python3，需要安装 python3运行环境
# 把该脚本 放于 xcode工程 根目录，命令行运行之（$> python3 /目录/CDZUnusedImage.py）即可，
# 输出 未使用的 图片名称

# 脚本 寻找所有 xxx.imageset 文件夹，获得 xxx字符串
# 查找 "xxx" 字符串，是否在 .h .m .xib .storyboard 文件中 出现过
# 出现过，则认为该图片使用过，反之认为没有使用过
# 2016-06-16


import sys,os
# 跳转到当前目录
curDir = sys.path[0];
os.chdir(curDir)

#--------------------配 置-------------------->

# 用于判断图片是否使用过的 代码文件后缀名，大小写敏感
# the suffixs of your code
codeFileSuffix = (".h", ".m", ".xib")

# 需要忽略的图片文件，大小写敏感
# the image names to ignore
ignoreFile = set(("refresh0", "refresh1", "refresh2", "refresh3",
    "refresh4", "refresh5", "refresh6", "refresh7", "refresh8",
    "refresh_arrow0", "refresh_arrow1", "refresh_arrow2", "refresh_arrow3",
    "refresh_arrow4", "refresh_arrow5", "refresh_arrow6",))

# 需要忽略的文件夹
# the dir names to ignore
ignoreDir = ("app.xcassets",
            ".bundle",
            ".imageset")


#--------------------配 置--------------------<



#--------------------函 数-------------------->
# 寻找rootDir目录下，所有 xxx.imageset 文件夹，获得 xxx字符串，结果以数组形式返回
def GetImageNameList(rootDir):
    imageNameList = []
    for dirpath, dirnames, filenames in os.walk(curDir):
        isIgnore = False
        for ignDir in ignoreDir:
            if ignDir in dirpath:
                isIgnore = True
                break

        if isIgnore:
            continue

        for dirname in dirnames:
            components = os.path.splitext(dirname)
            imagename = components[0]
            suf = components[1]
            if suf == ".imageset" and imagename not in ignoreFile:
                imageNameList.append(imagename)
    return imageNameList


# 获取指定后缀名的文件列表, 忽略 ignoreDir 中的目录
def GetFileListOfSuffix(dir, suffix):
    resultList = []
    isSufList = (isinstance(suffix, list) or isinstance(suffix, tuple) or isinstance(suffix, set))
    for dirpath, dirnames, filenames in os.walk(dir):
        isIgnore = False
        for ignDir in ignoreDir:
            if ignDir in dirpath:
                isIgnore = True
                break

        if isIgnore:
            continue

        for filename in filenames:
            suf = os.path.splitext(filename)[1]
            if(isSufList):
                for s in suffix:
                    if(suf == s):
                        resultList.append(os.path.join(dirpath, filename))
                        break
            else:
                if(suf == suffix):
                    resultList.append(os.path.join(dirpath, filename))
    return resultList

# 查找指定文件中，是否包含 textSet 的文本，返回包含的text集合
def IsFileContainTextSet(filePath, textSet):
    result = set()
    f = open(filePath)
    try:
        content = f.read()
        for text in textSet:
            textflag = '"' + text + '"'
            if textflag in content:
                result.add(text)
    except Exception as e:
        #print("--> 读取文件 %s 发生异常" % (filePath))
        pass
    f.close()
    return result

#--------------------函 数--------------------<



#--------------------工 作-------------------->

print ("--> 初始化...")
# 寻找所有图片名称
imageNameList = GetImageNameList(curDir)
print("--> 总共查找到 %d 张图片" % (len(imageNameList)))

# 获取源文件列表
sourceFilePathList = GetFileListOfSuffix(curDir, codeFileSuffix)
print("--> 总共查找到 %d 个源文件" % (len(sourceFilePathList)))


print ("--> 正在筛选未使用过的图片...")
unusedImageSet = set(imageNameList)
for filePath in sourceFilePathList:
    used = IsFileContainTextSet(filePath, unusedImageSet)
    unusedImageSet = unusedImageSet - used

index = 0
for unusedImage in unusedImageSet:
    print(str(index+1) + "-> " + "\033[36m" + unusedImage + "\033[0m is not used")
    index = index + 1

print ("--> 查找结束")
#--------------------工 作--------------------<


# created by baight 303730915@qq.com

