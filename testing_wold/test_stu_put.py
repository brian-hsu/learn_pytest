import requests
import json

# 定义API的基本URL和要获取的学生的ID
API_URL = "https://thetestingworldapi.com/Api/studentsDetails"
student_id = "9369531"

# 构建完整的API URL
full_url = f"{API_URL}/{student_id}"

# 准备要发送的更新数据，包括ID、中间名和出生日期
update_data = {
    "id": 9369531,
    "first_name": "br",
    "middlename": "K",
    "last_name": "hsu",
    "date_of_birth": "2000-01-02"
}

def test_put():
    # 发送PUT请求，并将更新数据转换为JSON格式
    response = requests.put(full_url, json=update_data)

    # 打印响应文本
    print(response.text)

    # 发送GET请求以验证数据是否已成功更新
    get_response = requests.get(full_url)

    # 打印GET请求的响应文本
    print(get_response.text)