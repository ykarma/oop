from urllib import request, parse

def youdao(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


    data = {
        "i": key,
        "from": "AUTO",
        "to":"AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "1536325606561",
        "sign": "2905a20eedb1f83198f9b3dd1078e194",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }

    data = parse.urlencode(data).encode()

    headers = {
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        #"Accept-Encoding": "gzip, deflate",
        "Accept - Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "200",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=1128499867@221.218.112.218;YOUDAO_EAD_UUID=d15b016f-d6a8-47a4-99fb-38da9b1ae130;JSESSIONID=aaa7KcFR0zFN_h8QDi0ww;OUTFOX_SEARCH_USER_ID_NCOO=574720862.0753857;fanyi-ad-id=49841;fanyi-ad-closed=1;___rl__test__cookies=1536325606540",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML, likeGecko)Chrome/68.0.3440.106Safari/537.36X-Requested-With:XMLHttpRequest"
    }

    req = request.Request(url=url, data=data, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)

if __name__ == '__main__':
    youdao('boy')