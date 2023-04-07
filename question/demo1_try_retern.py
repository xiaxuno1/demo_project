# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: demo1_try_retern
# Author: xiaxu
# DATA: 2023/3/24
# Description:
# ---------------------------------------------------

def test_finally(n):
    """
    测试当except return后是否会执行finally
    无论是否发生except，都会执行finally
    """
    try:
        if 2%n:
            return n
    except Exception as e:
        print(e)
        return e
    finally:
        print("我执行了finally！")
if __name__ == '__main__':
    print(test_finally(2))
    print(test_finally(0))
