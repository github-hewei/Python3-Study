import pymysql

# 连接数据库配置
connect_info = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '1234',
    'database': 'z_data'
}
# 连接数据库
try:
    link = pymysql.connect(**connect_info)
except:
    print("连接失败")
    exit()

# 获取操作游标
cursor = link.cursor()

# 执行查询
cursor.execute("SELECT m_ID,m_Name,m_Vender,m_Speci FROM YBT_JKDrug")

for i in range(cursor.rowcount):
    print(cursor.fetchone())
    if i >= 100:
        break





