import IPy

# ip = IPy.IP('172.16.0.0/26')

# print(ip.len())
# for i in ip:
#     print(i)


def comput(ipaddr: str):
    ip = IPy.IP(ipaddr)
    print('一共有{}个ip地址'.format(ip.len()))
    num = 1
    for i in ip:
        print('第{}个ip地址：'.format(num), i)
        num = num + 1


if __name__ == "__main__":
    print('请输入例如 172.16.0.0/26 的ip \n')
    ipaddr = input()
    comput(ipaddr)
    # print("请输入正确ip")
