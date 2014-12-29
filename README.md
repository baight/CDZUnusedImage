CDZUnusedImage
==============

查找工程中，未使用到的图片或其它资源 的 python3脚本

python3 script to search an project for unused images or other resource. 

使用 Use
==============

该脚本 基于 python3，需要安装 python3运行环境

把该脚本 放于 xcode工程 根目录，命令行运行之（$> python3 /目录/CDZUnusedImage.py）即可，

输出 未使用的 图片路径


it is based on python3, you should install python3 first

put it in the root directory of your project, and just run it ($> python3 /your dirs/CDZUnusedImage.py)

then, it will output the unused image path 

配置 Config
==============
// 要查找的 图片(或其它资源)文件后缀名，大小写敏感

// the suffixs of your images or other resource

imageSuffix = (".png", ".jpg", ".PNG", ".JPG")

----------

// 用于判断图片是否使用过的 代码文件后缀名，大小写敏感

// the suffixs of your code (to determine whether it has been used)

codeFileSuffix = (".h", ".m", ".xib", ".storyboard", ".plist", ".json")

----------

//需要忽略的图片文件，大小写敏感

//the image files to ignore

ignoreFile = set(("icon120.png", "icon29.png"))

