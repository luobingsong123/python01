import binascii
import serial
import time
import sys
import re


class Logger(object):

    def __init__(self, filename='default.log', stream=sys.stdout):
        self.terminal = stream

        self.log = open(filename, 'w')

    def write(self, message):
        self.terminal.write(message)

        self.log.write(message)

    def flush(self):
        pass


sys.stdout = Logger('0521.txt', sys.stdout)


def hexShow(argv):  # 十六进制显示 方法1
    try:
        result = ''
        hLen = len(argv)
        for i in range(hLen):
            hvol = argv[i]
            hhex = '%02x' % hvol
            result += hhex + ' '
        print('hexShow:', result)
        if re.match(result, value):
            print('指令下发成功')
        else:
            print('指令下发失败')
    except:
        print('指令下发失败')
        pass


Input = "01 16 7B 28 00 00 00 00 00 00 00 00 00 00 51 51 29 7D 7E 04"
value = '01167b285337303057463030303252018501a0297d7e04'
i = 0


while i < 30000:  # 循环重新启动串口
    t = serial.Serial('com5', 115200)
    # portx = "COM5"
    # bps = 115200
    # timex = 5
    # ser = serial.Serial(portx, bps, timeout=timex)
    # print("串口详情参数：", ser)
    print("串口详情参数：", t,'\n输入字符串：',Input)
    strInput = Input
    try:  # 如果输入不是十六进制数据--
        n = t.write(bytes.fromhex(strInput))
    except:  # --则将其作为字符串输出
        n = t.write(bytes(strInput, encoding='utf-8'))

    print("字符数",n)
    time.sleep(0.1)  # sleep() 与 inWaiting() 最好配对使用
    num = t.inWaiting()

    if num:
        try:  # 如果读取的不是十六进制数据--
            data = str(binascii.b2a_hex(t.read(num)))[2:-1]  # 十六进制显示方法2
            if data == None :
                print('指令下发失败')
            else:
                print("返回字符",)
                print(data)
                if re.match(data, value):
                    print('指令下发成功')
                else:
                    print('指令下发失败')
        except:  # --则将其作为字符串读取
            str = t.read(num)
            # print(str)
            hexShow(str)
    serial.Serial.close(t)

    i += 1
