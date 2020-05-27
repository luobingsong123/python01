from selenium import webdriver
import time

def wifiMode(mode):#网络协议模式
    a = mode
    if a in range (0,4):
        browse = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        browse.get("http://192.168.0.1/")
        print(browse.title)
        time.sleep(2)
        browse.find_element_by_id("wireless").click()
        time.sleep(2)
        option = browse.find_element_by_id("wifiMode")#option赋值为“wifiChannel”
        option = option.find_elements_by_xpath("option")#获取所有的option子元素 注意 是elements
        option[a].click()#选择第2个元素
        time.sleep(2)
        browse.find_element_by_id('submit').click()           #点击确定保存
        # time.sleep(1)
        browse.close()
        list = ['11b/g/n','11b/g','11g','11b']
        print("网络协议模式完成，当前网络协议模式为：",list[a])
    else:
        print("网络协议模式错误!")

list = [0,99,9] #使用列表管理WiFi设置参数如此列表的第二位（lsit[1]）就是目标信道
wifiMode(list[2])