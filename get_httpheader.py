import urllib.request


def parse_headers(ipaddrr):
    file = urllib.request.urlopen(ipaddr)
    print('1、获取当前url:', file.geturl())
    print('2、HTTPResponse类型:', file.getcode)
    print('3、响应头部信息：', file.info())
    if file.headers['X-Forward-For']:
        print(file.headers['X-Forward-For'])
    return file


if __name__ == "__main__":
    print('money6的EIP为 113.31.102.3')
    print('请输入ULB公网ip：')
    ipaddr = 'http://'+str(input())
    parse_headers(ipaddr)
