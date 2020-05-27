from selenium import webdriver  # web自动化
from selenium.webdriver.common.keys import Keys  # 键盘控制
import time
import xlrd  # excel管理
import serial  # 串口模块
import datetime  # 时间
import sys
import re

def testunit_read(data_path_in, sheetname_in, rows_in):
    data_path = data_path_in
    sheetname = sheetname_in
    rows = rows_in
    data = []
    datas = xlrd.open_workbook(data_path)
    sheet = datas.sheet_by_name(sheetname)
    for i in range(int(sheet.ncols)):
        a = sheet.cell_value(rows, i)  # Rows ，Column
        data.append(a)
    return data


def comConnect(atstr,value,iuname):
    data_0 = atstr
    values = value
    iunames = iuname
    try:
        #串口参数(port='COM5', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=5, xonxoff=False, rtscts=False, dsrdtr=False)
        portx = "COM5"
        bps = 115200
        timex = 5
        ser = serial.Serial(portx, bps, timeout=timex)
        print("串口详情参数：", ser)
        print(ser.port)  # 获取到当前打开的串口名
        print(ser.baudrate)  # 获取波特率
        result = ser.write(data_0.encode("gbk"))
        print("写总字节数:", result)
        time.sleep(1)
        while True:
            if ser.in_waiting:
                str = ser.read(ser.in_waiting).decode("gbk")
                print('发送数据：', data_0)
                time.sleep(1)
                if str == "exit":
                    break
                else:
                    print("收到数据：", str)
                    if re.match(values, str):
                        print(iunames, '用例测试成功')
                        time.sleep(0.1)
                    else:
                        print(iunames, '用例测试失败')
                    time.sleep(1)
                    break
        print("---------------")
        ser.close()  # 关闭串口
    except Exception as e:
        print("---异常---：", e)


# def wifi_ssid ( ssid, hide):  # SSID名称， 是否隐藏,要查看一下勾选不勾选的ID状态是否改变
#     new_ssid = ssid
#     hide_ssid = hide

def wifi_control(wifiSecurityMode_age, wifiMode_age, wifiChannel_age, wifiBandwidth_age, wifiSsid_age):
    browse = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    browse.get("http://192.168.0.1/")  # 不同设备管理IP会有区别，可以添加配置节点
    browse.find_element_by_id("wireless").click()
    print(browse.title)
    time.sleep(1)

    # 设置判断参数是否需要修改WiFi的SSID名称，然后再进行如下操作
    new_ssid = wifiSsid_age
    time.sleep(1)
    #    browse.find_element_by_id("wifiHideSSID").click()
    time.sleep(1)
    ceear = browse.find_element_by_id("wifiSSID")
    ceear.send_keys(Keys.CONTROL, 'a')
    ceear.send_keys(Keys.BACKSPACE)
    ceear.send_keys(new_ssid)

    a = wifiSecurityMode_age  # 加密模式
    if a in range(0, 4):
        option_3 = browse.find_element_by_id("wifiSecurityMode")
        option_3 = option_3.find_elements_by_xpath("option")
        option_3[a].click()
        time.sleep(1)
        list_2 = ['不加密', 'WPA-PSK', 'WPA2-PSK', 'WPA/WPA2-PSK 混合（推荐）']
        print("加密方式设置完成，当前加密方式为：", list_2[a])
    else:
        print("加密方式错误!")

    b = wifiMode_age  # WiFi协议
    if b in range(0, 4):
        option_1 = browse.find_element_by_id("wifiMode")
        option_1 = option_1.find_elements_by_xpath("option")
        option_1[b].click()
        time.sleep(1)
        list_1 = ['11b/g/n', '11b/g', '11g', '11b']
        print("网络协议模式完成，当前网络协议模式为：", list_1[b])
    else:
        print("网络协议模式错误!")

    c = wifiChannel_age  # 信道
    if c in range(0, 14):
        option_2 = browse.find_element_by_id("wifiChannel")
        option_2 = option_2.find_elements_by_xpath("option")
        option_2[c].click()
        time.sleep(1)
        if c == 0:
            print("信道设置完成，当前信道设置为：自动")
        else:
            print("信道设置完成，当前信道设置为：", c)
    else:
        print("信道设置错误!")

    d = wifiBandwidth_age  # 频宽
    if d == 0:  # a/b/g信道频宽只有20MHz 后面兼容逻辑会很难处理
        if d in range(0, 3):
            option_4 = browse.find_element_by_id("wifiBandwidth")
            option_4 = option_4.find_elements_by_xpath("option")
            option_4[d].click()
            time.sleep(1)
            list_3 = ['自动', '20MHz', '40MHz']
            print("频宽设置完成，当前频宽设置为：", list_3[d])
        else:
            print("频宽设置错误!")
    else:
        print("802.11a/b/g只支持20MHz频宽！")

    time.sleep(5)
    browse.find_element_by_id('submit').click()
    browse.close()


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


start_time_0 = datetime.datetime.now()
data_path = "D:\wifi模块功能自动化验证测试工具设计方案\用例格式规范_初稿.xlsx"
sheetname = "Sheet1"
rows = xlrd.open_workbook(data_path).sheet_by_name(sheetname).nrows
i = 2

for i in range(2, rows):
    start_time_1 = datetime.datetime.now()
    data = testunit_read(data_path, sheetname, i)
    print('用例内容：', data)
    wifi_control(int(data[0]), int(data[1]), int(data[2]), int(data[3]), data[4])
    time.sleep(1)
    comConnect(data[10],data[11],data[12])
    end_time_1 = datetime.datetime.now()
    all_time_1 = end_time_1 - start_time_1
    print("执行本用例时间：", all_time_1)
    print('---------------\n')


# 05/15：需要增加回显匹配
end_time_0 = datetime.datetime.now()
all_time_0 = end_time_0 - start_time_0
print("执行本次测试时间：", all_time_0)
print('测试结束')