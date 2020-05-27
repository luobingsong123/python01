import time
import sys


class Logger(object):

    def __init__(self, filename='default.log', stream=sys.stdout):
        self.terminal = stream

        self.log = open(filename, 'w')

    def write(self, message):
        self.terminal.write(message)

        self.log.write(message)

    def flush(self):
        pass


sys.stdout = Logger('掉电测试.txt', sys.stdout)

i = 1
while True:
    if i < 200:
        print("第",i,"次操作~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("开机")
        time.sleep(10)
        print("关机")
        time.sleep(10)
        i += 1
    elif i >= 200:
        K = int(input("查看属性值是否符合预期，输入1为符合预期，继续进行测试，输入其他则不符合预期，测试失败："))
        if K == 1:
            i = 1
        else:
            print("测试失败")
    else:
        break

