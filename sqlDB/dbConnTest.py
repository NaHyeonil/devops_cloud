import pymysql  # 실행을 위해 pymysql 라이브러리 설치가 필요 : pip install pymysql

# 각 데이터베이스 접속 정보에 맞게 세팅하고, DB에 연결합니다.
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',  # 접속계정의 계정명
    passwd='1234',  # 접속계정의 암호
    db='sqldb',  # 데이터베이스명
    charset='utf8'
)