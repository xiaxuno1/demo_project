# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: demo1
# Author: xiaxu
# DATA: 2023/2/27
# Description:acsii to hex
# ---------------------------------------------------
def main():
    try:		#为确保健壮性，需要对异常进行处理
        def hexToAscii(hN):
            n=map(lambda x:chr(int(x,16)),hN.split(' ')) #将多个16进制分割成单个，转换为字符串，再将多组字符串组成映射
            for i in n:
                print(i,end="")			#对映射进行遍历
        n = input('输入十六进制数，以空格为分隔符:')
        hexToAscii(n)
        print()
    except:	 #不正常的输入的情况下，会提示你重新输入，并再次执行主函数
            print("请输入正确的数!")
            main()
main()

