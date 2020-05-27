from selenium import webdriver  # web自动化
import time
import xlrd     # excel管理
import serial   # 串口模块
import datetime #时间

def testunit_read(data_path_in, sheetname_in,rows_in):
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


def comconnect(atstr):
    data_0 = atstr
    try:
        portx = "COM5"
        bps = 115200
        timex = 5
        ser = serial.Serial(portx, bps, timeout=timex)
        print("串口详情参数：", ser)
        print(ser.port)  # 获取到当前打开的串口名
        print(ser.baudrate)  # 获取波特率
        result = ser.write(data_0.encode("gbk"))
        print("写总字节数:", result)
        time.sleep(2)
        while True:
            if ser.in_waiting:
                str = ser.read(ser.in_waiting).decode("gbk")
                print('发送数据：', data_0)
                time.sleep(1)
                if (str == "exit"):
                    break
                else:
                    print("收到数据：", str)
                    time.sleep(1)
                    break
        print("---------------")
        ser.close()  # 关闭串口
    except Exception as e:
        print("---异常---：", e)


def wifi_control(wifiSecurityMode_age, wifiMode_age, wifiChannel_age, wifiBandwidth_age):
    browse = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    browse.get("http://192.168.0.1/")  # 不同设备管理IP会有区别，可以添加配置节点
    print(browse.title)
    time.sleep(2)
    browse.find_element_by_id("wireless").click()
    time.sleep(2)

    a = wifiSecurityMode_age  # 加密模式
    if a in range(0, 4):
        option_3 = browse.find_element_by_id("wifiSecurityMode")
        option_3 = option_3.find_elements_by_xpath("option")
        option_3[a].click()
        time.sleep(2)
        list_2 = ['不加密', 'WPA-PSK', 'WPA2-PSK', 'WPA/WPA2-PSK 混合（推荐）']
        print("加密方式设置完成，当前加密方式为：", list_2[a])
    else:
        print("加密方式错误!")

    b = wifiMode_age  # WiFi协议
    if b in range(0, 4):
        option_1 = browse.find_element_by_id("wifiMode")
        option_1 = option_1.find_elements_by_xpath("option")
        option_1[b].click()
        time.sleep(2)
        list_1 = ['11b/g/n', '11b/g', '11g', '11b']
        print("网络协议模式完成，当前网络协议模式为：", list_1[b])
    else:
        print("网络协议模式错误!")

    c = wifiChannel_age  # 信道
    if c in range(0, 14):
        option_2 = browse.find_element_by_id("wifiChannel")
        option_2 = option_2.find_elements_by_xpath("option")
        option_2[c].click()
        time.sleep(2)
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
            time.sleep(2)
            list_3 = ['自动', '20MHz', '40MHz']
            print("频宽设置完成，当前频宽设置为：", list_3[d])
        else:
            print("频宽设置错误!")
    else:
        print("802.11a/b/g只支持20MHz频宽！")

    time.sleep(5)
    browse.find_element_by_id('submit').click()
    browse.close()

start_time_0 = datetime.datetime.now()
data_path = "D:\wifi模块功能自动化验证测试工具设计方案\用例格式规范_初稿.xlsx"
sheetname = "Sheet1"
rows = xlrd.open_workbook(data_path).sheet_by_name(sheetname).nrows
i = 2


for i in range (2,rows):
    start_time_1 = datetime.datetime.now()
    data = testunit_read(data_path, sheetname,i)
    print('用例内容：', data)
    wifi_control(int(data[0]), int(data[1]), int(data[2]), int(data[3]))
    time.sleep(2)
    comconnect(data[10])
    end_time_1 = datetime.datetime.now()
    all_time_1 = end_time_1 - start_time_1
    print("执行本用例时间：",all_time_1)
    print('---------------\n')


end_time_0 = datetime.datetime.now()
all_time_0 = end_time_0 - start_time_0
print("执行本次测试时间：",all_time_0)
print('测试结束')
