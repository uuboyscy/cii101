import pymysql

def getStaff():
    host = 'localhost'
    port = 3307
    user = 'root'
    passwd = 'howdoyouturnthison'
    db = 'TESTDB'
    charset = 'utf8mb4'

    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = conn.cursor()

    sql = """
    SELECT ID, Name, DeptId, Age, Gender, Salary FROM Staff;
    """
    cursor.execute(sql)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data

if __name__ == '__main__':
    for r in getStaff():
        print(r)