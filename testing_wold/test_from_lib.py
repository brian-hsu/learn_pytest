import data_driven
import requests

# 創建庫檔案中類的對象
obj = data_driven.DataDrivenLibrary('./ts_data.xlsx', 'sheet1')

# 獲取列數、鍵列表和行數
column_count = obj.fetch_column_count()
key_list = obj.fetch_key_names()
row_count = obj.fetch_row_count()

# API URL
api_url = "https://httpbin.org/post"

# 從Excel中讀取數據並發送API請求
for i in range(2, row_count + 1):
    json_request = {}  # 預設的JSON請求
    updated_json_request = obj.update_request_with_data(i, json_request, key_list)
    response = requests.post(api_url, json=updated_json_request)
    print(f"Response for row {i}: {response.status_code}")
