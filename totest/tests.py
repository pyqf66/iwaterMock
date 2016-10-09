from django.test import TestCase

# Create your tests here.

# 由于需要建立测试数据库,账号没权限故此测试程序无发使用
class MyWebTest(TestCase):

    def setUp(self):
        pass

    def test_apimock(self):
        response = self.client.post('mockPlatform/tool/getWaterSettings')
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        pass
