import requests

# 指定目标网页的URL
url = 'https://www.example.com'

try:
    # 发送GET请求获取网页内容
    response = requests.get(url)

    # 检查响应状态码
    if response.status_code == 200:
        # 打印网页内容
        print(response.text)
    else:
        print("Failed to fetch data from the URL.")
except requests.RequestException as e:
    print("Error:", e)
