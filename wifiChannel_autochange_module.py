from selenium import webdriver
import time

def wifiChannel(channel):#信道设置
    a = channel
    if a in range (0,14):
        browse = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        browse.get("http://192.168.0.1/")
        print(browse.title)
        time.sleep(2)
        browse.find_element_by_id("wireless").click()
        time.sleep(2)
        option = browse.find_element_by_id("wifiChannel")#option赋值为“wifiChannel”
        option = option.find_elements_by_xpath("option")#获取所有的option子元素 注意 是elements
        option[a].click()#选择第2个元素
        time.sleep(2)
        browse.find_element_by_id('submit').click()           #点击确定保存
        # time.sleep(1)
        browse.close()
        if a == 0:
            print("信道设置完成，当前信道设置为：自动")
        else:
            print("信道设置完成，当前信道设置为：",a)
    else:
        print("信道设置错误!")

list = [0,99,9] #使用列表管理WiFi设置参数如此列表的第二位（lsit[1]）就是目标信道
wifiChannel(list[1])