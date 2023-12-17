import requests
import json

# 定义API的基本URL
API_URL = "https://thetestingworldapi.com/Api/studentsDetails"

# 准备POST请求的JSON数据
data = {
    "first_name": "Testing",
    "middle_name": "K",
    "last_name": "World",
    "date_of_birth": "1990-01-01"
}

def test_post():
    # 发送POST请求
    response = requests.post(API_URL, json=data)

    # 打印响应文本
    print(response.text)
