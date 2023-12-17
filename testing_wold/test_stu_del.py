import requests
import json

API_URL = "https://thetestingworldapi.com/Api/studentsDetails"

# 准备POST请求的JSON数据
data = {
    "first_name": "Testing",
    "middle_name": "K",
    "last_name": "World",
    "date_of_birth": "1990-01-01"
}

def test_del():
    # 发送POST请求
    post_response = requests.post(API_URL, json=data)

    # 打印响应文本
    print(f'post:{post_response.text}')
    post_response_json = json.loads(post_response.text)
    student_id = post_response_json["id"]
    print(f'id:{student_id}')

    full_url = f"{API_URL}/{student_id}"

    get_response = requests.get(full_url)
    print(f'get:{get_response.text}')

    del_response = requests.delete(full_url)
    print(f'delete:{del_response.text}')

    get_response = requests.get(full_url)
    print(f'get:{get_response.text}')