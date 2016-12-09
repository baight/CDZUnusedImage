import sys,os

# 寻找rootDir目录下，所有 xxx.imageset 文件夹，获得 xxx字符串，结果以数组形式返回
def GetImageNameListInDirectory(theDir, ignoreDirs=[], ignoreFiles=[]) -> list:
    imageNameList = []
    for dirpath, dirnames, filenames in os.walk(theDir):
        isIgnore = False
        for ignDir in ignoreDirs:
            if ignDir in dirpath:
                isIgnore = True
                break

        if isIgnore:
            continue

        for dirname in dirnames:
            components = os.path.splitext(dirname)
            imagename = components[0]   # 文件名
            suf = components[1]         # 文件后缀
            if suf == ".imageset" and imagename not in ignoreFiles:
                imageNameList.append(imagename)
    return imageNameList


# 获取指定后缀名的文件列表, 忽略 ignoreDir 中的目录
def GetFileListOfSuffix(dir, suffixs=[], ignoreDirs=[]) -> list:
    resultList = []
    for dirpath, dirnames, filenames in os.walk(dir):
        isIgnore = False
        for ignDir in ignoreDirs:
            if ignDir in dirpath:
                isIgnore = True
                break

        if isIgnore:
            continue

        for filename in filenames:
            suf = os.path.splitext(filename)[1]
            if suf in suffixs:
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


# created by baight 303730915@qq.com

