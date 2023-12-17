import requests
import json
import jsonpath

# 你的API的URL
url = "https://reqres.in/api/users?page=2"


def test_status():
    # 发送GET请求
    response = requests.get(url)

    # 验证状态码
    assert response.status_code == 200, "状态码不是200"

    # 获取所有响应头
    print("\n响应头:", response.headers)

    # 获取特定的响应头信息
    date_header = response.headers.get("Date")
    server_header = response.headers.get("Server")
    print("\nDate 响应头:", date_header)
    print("\nServer 响应头:", server_header)

    # 获取Cookies
    print("\nCookies:", response.cookies)

    # 获取编码方式
    print("\n编码方式:", response.encoding)

    # 获取经过时间
    print("\n请求经过时间:", response.elapsed)

    json_response = json.loads(response.text)
    print("\nResp:", json_response)
    print("\ndata:", json_response["data"])
    data = jsonpath.jsonpath(json_response, "data")
    print("\njsonpath  data:", data)

    for i in range(0, 3):
        first_name = jsonpath.jsonpath(json_response, f"data[" + str(i) + "].first_name")
        print(first_name[0])
