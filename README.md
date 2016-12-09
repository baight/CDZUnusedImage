CDZUnusedImage
==============

查找工程中，可能未使用到的图片或其它资源 的 python3脚本

python3 script to search an project for images or other resource that may be unused

使用 Use
==============

该脚本 基于 python3，需要安装 python3运行环境

把该脚本 放于 xcode工程 根目录，命令行运行之（$> python3 /目录/CDZUnusedImage.py）即可，

输出 未使用的 图片路径


it is based on python3, you should install python3 first

put it in the root directory of your project, and just run it ($> python3 /your dirs/CDZUnusedImage.py)

then, it will output the unused image path 

原理 Principle
==============
脚本 寻找所有 xxx.imageset 文件夹，获得 xxx字符串
查找 "xxx" 字符串，是否在 .h .m .xib .storyboard 文件中 出现过
出现过，则认为该图片使用过，反之认为没有使用过

配置 Config
==============

// 用于判断图片是否使用过的 代码文件后缀名，大小写敏感

// the suffixs of your code (to determine whether it has been used)

codeFileSuffixs = (".h", ".m", ".xib", ".storyboard", ".plist", ".json")

----------

// 需要忽略的图片文件，大小写敏感

// the image files to ignore

ignoreFiles = set(("icon120", "icon29"))

注意 Notes
==============
该脚本存在误报的可能，在删除图片资源前，你需要再次确认

there exists possibility that it work out with some wrong results, you are supposed to confirm it again 
