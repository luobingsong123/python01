from selenium import webdriver
import time

def wifiBandwidth(Band):#频宽
    a = Band
    if a in range (0,3):
        browse = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        browse.get("http://192.168.0.1/")
        print(browse.title)
        time.sleep(2)
        browse.find_element_by_id("wireless").click()
        time.sleep(2)
        option = browse.find_element_by_id("wifiBandwidth")#option赋值为“wifiChannel”
        option = option.find_elements_by_xpath("option")#获取所有的option子元素 注意 是elements
        option[a].click()#选择第2个元素
        time.sleep(2)
        browse.find_element_by_id('submit').click()           #点击确定保存
        # time.sleep(1)
        browse.close()
        list = ['自动','20MHz','40MHz']
        print("频宽设置完成，当前频宽设置为：",list[a])
    else:
        print("频宽设置错误!")

list = [1,99,9,2] #使用列表管理WiFi设置参数如此列表的第二位（lsit[1]）就是目标信道
wifiBandwidth(list[3])