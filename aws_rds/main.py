# AWS RDS 연결

import pymysql

host = "database-2.cluster-cqzcylqtuiiu.ap-northeast-2.rds.amazonaws.com"
port = 3306
db = "database-2-instance-1"
user = "admin"
passwd = "12345678"


def connect_db(host, user, passwd, db, port):
    conn = pymysql.connect(
        host, user, passwd, db, port, use_unicode=True, charset="utf8"
    )
    cursor = conn.cursor()
    return conn, cursor


if __name__ == "__main__":
    conn, cursor = connect_db(host, user, passwd, db, port)
