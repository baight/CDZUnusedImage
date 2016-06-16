
# 该脚本功能是，查找脚本所在目录（包括子目录）中，未使用到的图片资源
# 该脚本 基于 python3，需要安装 python3运行环境
# 把该脚本 放于 xcode工程 根目录，命令行运行之（$> python3 /目录/CDZUnusedImage.py）即可，
# 输出 未使用的 图片名称

# 脚本 视 image.png impage@2x.png image@3x.png 为同一张图片，只会查找一次
# 脚本 会忽略 .bundle .xcassets 目录下的 图片文件
# 查找 "image" 和 "image.png"，是否在 .h .m .xib .storyboard 文件中 出现过
# 出现过，则认为该图片使用过，反之认为没有使用过
# 2014-12-26


import sys,os
# 跳转到当前目录
curDir = sys.path[0];
os.chdir(curDir)

#--------------------配 置-------------------->

# 要查找的 图片文件后缀名，大小写敏感
# the suffixs of your images
imageSuffix = (".png", ".jpg", ".PNG", ".JPG")

# 用于判断图片是否使用过的 代码文件后缀名，大小写敏感
# the suffixs of your code
codeFileSuffix = (".h", ".m", ".xib", ".storyboard", ".plist")

# 需要忽略的图片文件，大小写敏感
# the image files to ignore
ignoreFile = set(("musicButton-0.png",
    "musicButton-1.png",
    "musicButton-2.png",
    "musicButton-3.png",
    "musicButton-4.png",
    "musicButton-5.png",
    "musicButton-6.png",
    "musicBtn_gold-0.png",
    "musicBtn_gold-1.png",
    "musicBtn_gold-2.png",
    "musicBtn_gold-3.png",
    "musicBtn_gold-4.png",
    "musicBtn_gold-5.png",
    "musicBtn_gold-6.png"))

ignoreDir = ("app.xcassets",
            ".bundle")


#--------------------配 置--------------------<



#--------------------函 数-------------------->
# 获取指定后缀名的文件列表, 忽略 .bundle 目录
def FindFilesOfSuffix(dir, suffix):
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

# 查找指定文件中，是否包含 text1 或 text2
def IsFileContainString(filePath, text1, text2):
    f=open(filePath)
    try:
        for line in f:
            if(text1 in line or text2 in line):
                return True
                break
    except:
        pass
    f.close()
    return False

#--------------------函 数--------------------<



#--------------------工 作-------------------->

print ("--> 初始化...")
# 获取所有 图片文件 文件名
imageList = FindFilesOfSuffix(curDir, imageSuffix)
tmp = imageList
imageList = []
imageDic = {}
# 将image@2x.png 转换为 image.png
for filePath in tmp:
    basename = os.path.basename(filePath)
    imageDic[basename] = filePath
    basename = basename.replace("@2x", "")
    basename = basename.replace("@3x", "")
    imageList.append(basename)
    if( basename in imageDic):
        path = imageDic[basename]
        if( "@" in path):
            imageDic[basename] = filePath
    else:
        imageDic[basename] = filePath

# 去重
imageList = set(imageList)
# 去 需要忽略的文件
imageList = imageList - ignoreFile

# 获取所有 .h .m .xib .storyboard .plist .json 文件
fileList = FindFilesOfSuffix(curDir, codeFileSuffix)

print ("--> 正在查找...")
index = 1;
for image in imageList:
    isUse = False
    for filePath in fileList:
        suf = os.path.splitext(filePath)[1]
        if (suf == ".plist"):
            imageT = os.path.splitext(image)[0]
        else:
            imageT = '"' + os.path.splitext(image)[0] + '"'
        if IsFileContainString(filePath, image, imageT):
            isUse = True
            break
    if not isUse :
        dir = os.path.dirname(imageDic[image])
        print(str(index) + "-> " + os.path.join(dir, "") + "\033[36m" + image + "\033[0m is not used")
        index = index + 1
print ("--> 查找结束")
#--------------------工 作--------------------<


# created by baight 303730915@qq.com

