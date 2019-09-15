# coding: utf-8
import numpy
import time
import sys
# 文件打开方式:
#   r-->只读
#   w-->只写
#   r+ -->读写
#   w+ -->读写
#   a -->追加写
#   a+ -->追加读写
# ​文件以w+打开后，读取出来的内容为空；而以r+打开，写入的内容为追加
#  格式：open("文件名"，"打开方式",coding="编码格式")

if __name__ == "__main__":
    path = "D:\password_8.txt"
    file = open(path, "w")
    passwordData = "0123456789" \
                   # "abcdefghijklmnopqrstuvwxyz" \
                   # "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
                   # r"~!@#$%^&*()_+-`,.\/<>?:;'|[]{}"
    passwordData = numpy.array(list(passwordData))
    pwdArr = numpy.array(["1", "2", "3", "4", "5", "6", "7", "8"])
    print("开始记录")
    oldtime = time.time()
    for num1 in range(len(passwordData)):
        sys.stdout.write("\r目前进度:"+str((num1/len(passwordData)*100.0))+"%")
        sys.stdout.flush()
        pwdArr[0] = passwordData[num1]
        for num2 in range(len(passwordData)):
            sys.stdout.write("\r目前进度:"+str((num1/len(passwordData)*100.0)+(num2/len(passwordData)*10.0))+"%")
            sys.stdout.flush()
            pwdArr[1] = passwordData[num2]
            for num3 in range(len(passwordData)):
                sys.stdout.write("\r目前进度:"+str((num1/len(passwordData)*100.0)+(num2/len(passwordData)*10.0)+(num3/len(passwordData)*1.0))+"%")
                sys.stdout.flush()
                pwdArr[2] = passwordData[num3]
                for num4 in range(len(passwordData)):
                    pwdArr[3] = passwordData[num4]
                    for num5 in range(len(passwordData)):
                        pwdArr[4] = passwordData[num5]
                        for num6 in range(len(passwordData)):
                            pwdArr[5] = passwordData[num6]
                            for num7 in range(len(passwordData)):
                                pwdArr[6] = passwordData[num7]
                                for num8 in range(len(passwordData)):
                                    pwdArr[7] = passwordData[num8]
                                    file.write("".join(pwdArr)+"\n")
    file.close()
    newtime = time.time()
    Time = newtime-oldtime
    # sys.stdout.write(r)
    # sys.stdout.flush()
    # print("循环"+str(len(passwordData)**8/10000/10000)+"亿次需要"+str(Time)+"秒")
    sys.stdout.write("\r目前进度:已完成！")
    sys.stdout.flush()
    print("写入完成")
    print("密码文本写入花费时间"+str(Time)+"秒")
