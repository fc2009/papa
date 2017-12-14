import pymysql
# port  端口号不要用双引号括起来，charset 要写utf8 不要写utf-8;
con = pymysql.Connect(host='127.0.0.1', port=3306, user='root',
                      password='fanyubin', db='stock', charset='utf8')
# cursor 是游标。
cursor = con.cursor()
# execute是操作数据库的函数
cursor.execute("select * from gupiao")
cursor.execute("desc gupiao")
# 把最近的excute里的内容全部打印出来（元组的形式）
# fetchone 打印一行
print(cursor.fetchall())

cursor.close()
con.close()