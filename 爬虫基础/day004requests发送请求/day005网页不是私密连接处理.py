import requests

url = "https://yjcclm.com/"
#ssl.CertificateError...的话verify=False设置这个参数的话 就忽略证书
response = requests.get(url, verify=False)