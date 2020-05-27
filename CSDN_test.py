class SelectMock(unittest.TestCase):
    def test_request(self):
        i = 0
        for i in range (0,2):
            logger.logger.logger.debug('测试用例: "%s"' % re.test[i]['接口名称'])
            # 发送请求
            headers = sg.headers
            urle = re.test[i]['环境']
            url1 = re.test[i]['接口地址']
            url = urle + url1
            params = re.test[i]['参数']
            res = requests.get(url=url, params=params, headers=headers).json()
            logger.logger.logger.debug('返回结果：%s]' % (res))
            self.assertEqual(res['code'], 'success')
            i += 1