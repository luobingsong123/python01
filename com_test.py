from selenium import webdriver  # web自动化
from selenium.webdriver.common.keys import Keys  # 键盘控制
import xlrd  # excel管理
import serial  # 串口模块
import time
import re
import datetime
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


sys.stdout = Logger('a.txt', sys.stdout)

# sys.stderr = Logger('a.log_file', sys.stderr)


def comConnect(atstr, iuname, value, times):
    starttime = datetime.datetime.now()
    iunames = iuname
    data_0 = atstr
    values = value
    times = times
    i = 0
    failtime = 0
    while i < times:
        try:
            portx = "com5"
            bps = 115200
            timex = 5
            ser = serial.Serial(portx, bps, timeout=timex)
            print("串口详情参数：", ser)
            print(ser.port)  # 获取到当前打开的串口名
            print(ser.baudrate)  # 获取波特率
            # result = ser.write(data_0.encode("gbk")) # 字符串下发模式
            result = ser.write(bytes.fromhex(data_0))  # HEX下发模式
            print("写总字节数:", result)
            while True:
                if ser.in_waiting:
                    str = ser.read(ser.in_waiting).decode("gbk")
                    print('发送数据：', data_0)
                    time.sleep(0.1)
                    if (str == "exit"):
                        break
                    else:
                        print("收到数据：", str)
                        if re.match(values, str):
                            print(iunames, '第', i + 1, '次用例测试成功')
                            time.sleep(0.1)
                            i += 1
                        else:
                            print(iunames, '第', i + 1, '次用例测试失败')
                            failtime += 1
                            i += 1
                    break
            print("---------------")
            ser.close()  # 每次都需要关闭串口，能否实现串口长连接
        except Exception as e:
            print("---异常---：", e)


    endtime = datetime.datetime.now()
    print("总测试次数：", times, "\n成功次数", times - failtime, '\n失败次数', failtime)
    print('总测试时间：', endtime - starttime)


# AT\+CONNECT\=\=192\.168\.0\.144
# .*255\.255\.255\.255
# +++\r\n 进入AT指令模式
times = int(input('测试次数：'))
comConnect(
        '01 16 7B 28 00 00 00 00 00 00 00 00 00 00 51 51 29 7D 7E 04'
        'test item -- test',
        '.*?AT\+CONNECT\=\=192\.168\.', times)
