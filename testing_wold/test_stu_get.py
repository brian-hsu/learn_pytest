import requests
import json

# 定义API的基本URL和要获取的学生的ID
API_URL = "https://thetestingworldapi.com/Api/studentsDetails"
student_id = "9369531"

# 构建完整的API URL
full_url = f"{API_URL}/{student_id}"


def test_pp():
    # 发送GET请求
    response = requests.get(full_url)

    # 打印响应文本
    print(response.text)

    # 将响应内容解析为JSON格式
    json_response = response.json()

    print(json_response)
    # 提取ID字段并进行断言
    assert json_response['data']['id'] == int(student_id)
