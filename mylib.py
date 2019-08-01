import sys,os

xcimageSetSuffix = '.imageset'


# 寻找rootDir目录下，所有 xxx.imageset 文件夹，获得 xxx字符串，结果以数组形式返回
def GetXcassetsImageNameListInDirectory(theDir, ignoreDirs=[], ignoreFiles=[], ignorePrefix=[]) -> list:
    imageNameList = []
    for dirpath, dirnames, filenames in os.walk(theDir):
        if xcimageSetSuffix in dirpath:
            continue

        isIgnore = False
        for ignDir in ignoreDirs:
            if ignDir in dirpath:
                isIgnore = True
                break

        if isIgnore:
            continue

        for dirname in dirnames:
            components = os.path.splitext(dirname)
            image_name = components[0]   # 文件名
            suf = components[1]         # 文件后缀
            if suf == xcimageSetSuffix and image_name not in ignoreFiles:
                for prefix in ignorePrefix:
                    if image_name.startswith(prefix):
                        image_name = image_name[len(prefix):]
                        print(image_name)
                        break
                imageNameList.append(image_name)
    return imageNameList


# 寻找rootDir目录下，所有 不在 xxx.imageset 文件夹 的图片，结果以数组形式返回
def GetNotXcassetsImageNameListInDirectory(theDir, ignoreDirs=[], ignoreFiles=[],
                                           imageFileSuffixs = (".png", ".PNG", ".jpg", "JPG", '.jpeg', '.JPEG'),
                                           ignorePrefix=[]) -> list:
    imageNameList = []
    for dirpath, dirnames, filenames in os.walk(theDir):
        if xcimageSetSuffix in dirpath:
            continue

        isIgnore = False
        for ignDir in ignoreDirs:
            if ignDir in dirpath:
                isIgnore = True
                break

        if isIgnore:
            continue

        for filename in filenames:
            components = os.path.splitext(filename)
            image_name = components[0]   # 文件名
            if '@' in image_name:
                image_name = image_name.split("@")[0]
            suf = components[1]         # 文件后缀
            if suf in imageFileSuffixs and image_name not in ignoreFiles:
                for prefix in ignorePrefix:
                    if image_name.startswith(prefix):
                        image_name = image_name[len(prefix):]
                        break
                imageNameList.append(image_name)
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


# 查找指定文件中，是否包含 textSet 里边的文本，返回包含的text集合
def IsFileContainTextSet(filePath, textSet) -> set:
    usedSet = set()
    if not os.path.exists(filePath):
        return usedSet
    f = open(filePath)
    try:
        content = f.read()
        for text in textSet:
            textflag = '"' + text + '"'
            if textflag in content:
                usedSet.add(text)
    except Exception as e:
        #print("--> 读取文件 %s 发生异常" % (filePath))
        pass
    f.close()
    return usedSet


# created by baight 303730915@qq.com

