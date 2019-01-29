import sys,os,enum


class TextColor(enum.Enum):
    Default = '0'
    Black = '30'
    Red = '31'
    Green = '32'
    Yellow = '33'
    Blue = '34'
    Purple = '35'
    Cyan = '36'
    White = '37'


class BackgroundColor(enum.Enum):
    Default = '0'
    Black = '40'
    Red = '41'
    Green = '42'
    Yellow = '43'
    Blue = '44'
    Purple = '45'
    Cyan = '46'
    White = '47'


class DisplayMode(enum.Enum):
    Default = '0'       # 默认
    Highlight = '1'     # 高亮
    Underline = '4'     # 下划线
    Flicker = '5'       # 闪烁
    Inverse = '7'       # 反白
    Hidden = '8'        # 不可见


class ColorTextComponent(object):
    def __init__(self):
        self.text = ''
        self.color = TextColor.Green
        self.backgroundColor = BackgroundColor.Default
        self.displayMode: DisplayMode.Default

    def getPrintString(self) -> str:
        if len(self.text) <= 0:
            return ''

        if self.color == TextColor.Default and self.backgroundColor == BackgroundColor.Default and self.displayMode == DisplayMode.Default:
            return self.text

        print_string = '\033['
        if self.displayMode != DisplayMode.Default:
            print_string = print_string + self.displayMode.value + ';'

        print_string = print_string + self.color.value

        if self.backgroundColor != BackgroundColor.Default:
            print_string = print_string + ';' + self.backgroundColor.value

        print_string = print_string + 'm' + self.text + '\033[0m'
        return print_string


class ColorText(object):
    def __init__(self):
        self.textComponentArray = []

    def appendColorText(self, text='', color=TextColor.Default, backgroundColor=BackgroundColor.Default,
                        displayMode=DisplayMode.Default):
        color_text_component = ColorTextComponent()
        color_text_component.text = text
        color_text_component.color = color
        color_text_component.backgroundColor = backgroundColor
        color_text_component.displayMode = displayMode
        self.textComponentArray.append(color_text_component)

    def getPrintString(self) -> str:
        print_string = ''
        for color_text_component in self.textComponentArray:
            print_string = print_string + color_text_component.getPrintString()
        return print_string


def printColorText(colorText:ColorText):
    print(colorText.getPrintString())





# created by baight 303730915@qq.com

