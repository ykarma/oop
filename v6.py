from urllib import request,parse
import json


def translate(content):
    url = "http://fanyi.baidu.com/"
    data = parse.urlencode({"kw":content})  # 将参数进行转码

    req = request.Request(url,data=bytes(data,encoding="utf-8"))
    r = request.urlopen(req)
    #print(r.code)  查看返回的状态码
    html = r.read().decode('utf-8')
    # json格式化
    html = json.loads(html)
    print(html)
    for k in html["data"]:
        print(k["k"],k["v"])

if __name__ == '__main__':
    content = input("请输入您要翻译的内容：")
    translate(content)