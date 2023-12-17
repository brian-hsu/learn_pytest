import requests
import json

# 定义全局变量来存储学生ID
student_id = None

# 添加新学生
def test_add_student():
    global student_id

    # 定义API的基本URL和要添加的学生数据
    API_URL = "https://thetestingworldapi.com/Api/studentsDetails"
    student_data = {
        "first_name": "John",
        "middle_name": "K",
        "last_name": "Doe",
        "date_of_birth": "2000-01-01"
    }

    # 发送POST请求，添加新学生
    response = requests.post(API_URL, json=student_data)
    response_json = response.json()

    # 提取学生ID
    student_id = response_json['id']
    print("New student added with ID:", student_id)

# 获取学生详细信息
def test_get_student_details():
    global student_id

    # 定义API的基本URL
    API_URL = "https://thetestingworldapi.com/Api/studentsDetails"

    # 构建完整的API URL，包括基本URL和学生ID
    full_url = f"{API_URL}/{student_id}"

    # 发送GET请求，获取学生详细信息
    response = requests.get(full_url)
    print("get", response.text)
    response_json = (response.json())["data"]

    # 打印学生详细信息
    print("Student Details:")
    print("ID:", response_json['id'])
    print("First Name:", response_json['first_name'])
    print("Middle Name:", response_json['middle_name'])
    print("Last Name:", response_json['last_name'])
    print("Date of Birth:", response_json['date_of_birth'])

# 执行测试用例
test_add_student()
test_get_student_details()
