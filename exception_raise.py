# ecoding=UTF-8

# 我们创建了我们自己的异常类型。这一新的异常类型叫作ShortInputException
class ShortInputException(Exception):
    '''一个有用户定义的异常类'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('enter something -->')
    if(len(text)) < 3:
        # raise 语句来引发一次异常，具体方法是提供错误名或异常名以及要抛出 （Thrown）异常的对象
        raise ShortInputException(len(text),3)
    #其他工作在此正常执行
except EOFError:
    print('why did you do an EOF on me?')
except ShortInputException as e:
    print(('ShortInputException: The input was ' + '{0} long,expected at least {1}').format(e.length, e.atleast))
else:
    print('No exception was raised.')
