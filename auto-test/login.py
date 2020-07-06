import requests
import hashlib
import json
from hyper.contrib import HTTP20Adapter
import http.cookiejar as cj

##
# 登录操作
# 暂定在此文件修改登录配置
##

username = ""
password = ""
# login_url = ""
# username = "18312345678"
# password = "123456"
login_url = ""

# 前端加密算法 md5
def md5(str):
    m = hashlib.md5()
    b = str.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()
    print(str_md5)
    return str_md5


def form_data():
    password_md5 = md5(password)
    data = {
        "mobile": username,
        "password": password_md5
    }
    return json.dumps(data)


def header():
    return {
        ':authority': 'v2-app.delicloud.com',
        ':method': 'POST',
        ':path': '/api/v2.0/auth/loginMobile',
        ':scheme': 'https',
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'client_id': 'eplus_web',
        'content-length': '70',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://v2-web.delicloud.com',
        'pragma': 'no-cache',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'x-service-id': 'userauth'
    }


if __name__ == '__main__':
    s = requests.Session()
    s.cookies = cj.LWPCookieJar()
    s.mount(login_url, HTTP20Adapter())
    r = s.post(login_url, data=form_data() ,headers=header())
    s.cookies.save(filename='cookies.txt', ignore_discard=True, ignore_expires=True)

    obj = json.loads(r.text);

    print(json.loads(r.text))

    token = obj['data']['token'];
    print(token)
    mainUrl = ""

    header={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235',
        'cookie': 'PHPSESSID=2prvdqmt1p2nid41i31170blr2; __eplus_uid__=461558041571536896; __eplus_org_id__=461550259019517953; gr_user_id=28296f37-ab8e-4dd5-a9b1-0fb4790bd988; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22user.461558041571536896%22%2C%22first_id%22%3A%221730d0bf1794ad-08deeeefcacb77-b79183d-1049088-1730d0bf17a147%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221730d0bf1794ad-08deeeefcacb77-b79183d-1049088-1730d0bf17a147%22%7D; gr_session_id_8926433e4893eb23=242ce6c2-7050-46d4-b23b-5f05fe7946b9; gr_session_id_8926433e4893eb23_242ce6c2-7050-46d4-b23b-5f05fe7946b9=true; __eplus_token__=b0211f805db548129bba5072fa02de884d1e67a4ce007af077c42de7ff404bfd'
    }
    html = requests.get(mainUrl,headers = header)
    print(html.text)



    # c=HTTP20Connection("v2-app.delicloud.com:443",secure=True,ssl_context = tls.init_context(cert_path='ca.crt',cert=('mgr.crt', 'mgr.key')))#cert_path为服务端证书，cert客户端证书
    # response = c.request('GET', "/api/v2.0/auth/loginMobile")#你的请求URL
    # resp = c.get_response(response)
    # print(resp.read())
