# encode/decode

name = 'dfa'
print(name, type(name))

name1 = name.encode()
print(name1, type(name1))

name2 = name1.decode()
print(name2, type(name2))

# 图片、视频、音频，需要以bytes类型的格式去保存


'''
requests基本使用
'''
import requests

url = 'https://github.com/Januarymyhat'
# 发送请求
response = requests.get(url)
print(response)

# 打印响应内容
print(response.text)  # 有乱码，requests模块会自动寻求一种解码方式去解码
print(response.content.decode())  
