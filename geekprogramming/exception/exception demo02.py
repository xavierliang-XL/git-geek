class ShortInputError(Exception):
    def __init__(self,length,min_len):
        self.length=length
        self.min_len=min_len

    def __str__(self):
        return f'你的长度是{self.length},不能少于{self.min_len}字符'

def main():
    try:
        con=input('清输入密码：')
        if len(con)<3:
            raise ShortInputError(len(con),3)
    except Exception as result:
        print(result)
    else:
        print('密码输入完成')
main()