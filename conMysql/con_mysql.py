# import pymysql
#
#
# # 建立连接
# con = pymysql.connect(host="",user="",password="",database="",port=3306)
#
# # 创建游标
# cur = con.cursor()
#
# # 查询sql语句
# query_user_info_sql = "select * from students limit 3"
#
# # 使用游标执行SQL语句
# cur.execute(query_user_info_sql)
#
# # 显示查到的数据
#
# print(cur.fetchall())
#
# con.rollback()
#
# con.commit()
#
# # 关闭连接
# con.close()
