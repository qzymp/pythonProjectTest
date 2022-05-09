class ShortInputException(Exception):
    '''自定义异常'''
    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast

    def __str__(self):
        return f'输入的长度是{self.length}, 长度至少是{self.atleast}'

def main():
    try:
        s = input('请输入--->')
        if len(s) < 3:
            # raise 引发一个自定义异常
            raise ShortInputException(len(s), 3)
    except ShortInputException as result:
        print('ShortInputException:' % result)
    else:
        print('没有异常发生')

main()