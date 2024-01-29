from django.test import TestCase, Client
from django.urls import reverse
from hiring.e04.models import Company
from rest_framework import status
import json

class testGetCompanies(TestCase):
    
    def setUp(self):
        # 设定测试客户端
        self.client = Client()
        # 设定URL，这里假设您在urls.py中定义的路由名称为'company-list'
        self.companies_url = reverse('companies:company-list')
        # 创建测试数据
        Company.objects.create(name='Amazon', status='hiring', application_link='', notes='')
        Company.objects.create(name='Google', status='hiring', application_link='', notes='')

    def test_zero_companies_should_return_empty_list(self):
        # 删除所有公司数据以测试空数据情况
        Company.objects.all().delete()
        response = self.client.get(self.companies_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), [])
    
    def test_get_companies(self):
        # 测试获取公司列表
        response = self.client.get(self.companies_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)), 2)  # 因为创建了两个测试公司

    def test_get_company_content(self):
        # 测试返回内容
        response = self.client.get(self.companies_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(response_data[0]['name'], 'Amazon')
        self.assertEqual(response_data[1]['name'], 'Google')

