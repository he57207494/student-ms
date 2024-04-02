import pymysql

userName = "root"
password = "ai57207494?"

def open():
    db = pymysql.connect(host="localhost",user= userName,password= password, database="db_student",charset='utf8')
    return db

#执行数据库的增加、删除、修改操作
def exec(sql,values):
    db = open()
    cursor = db.cursor()
    try:
        cursor.execute(sql,values)
        db.commit()
        return 1
    except:
        db.rollback()
        return 0
    finally:
        cursor.close()
        db.close()

#带参数的精确查询
def query(sql,values):
    db = open()
    cursor = db.cursor()
    cursor.execute(sql,values)

    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

def query2(sql):
    db = open()
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

