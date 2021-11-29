import pymysql


conn = None
cur = None

# 데이터 베이스 접속속
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',  # 접속계정의 계정명
    passwd='1234',  # 접속계정의 암호
    db='sqldb',  # 데이터베이스명
    charset='utf8'
)
# 커서
cur = conn.cursor()

# userTBL의 회원 데이터 Insert
sql = ""
# userID, name, birthYear, addr
userID = "",
name = ""
birthYear = ""
addr = ""
mobile1 = ""
mobile2 = ""
height = ""

# userTBL의 회원 데이터 Insert (NULL 없이 모든 컬럼의 데이터
while(True) :
    userID = input("사용자 ID ==> ")
    if userID == "" :
        break
    name = input("사용자 이름 ==> ")
    birthYear = input("사용자 출생년도 ==> ")
    addr = input("사용자 주소 ==> ")
    mobile1 = input("사용자 휴대폰번호 앞3자리 ==> ")
    mobile2 = input("사용자 휴대폰번호 뒤8자리 ==> ")
    height = input("사용자 키 ==> ")

    sql = "INSERT INTO userTBL (userID, name, birthYear, addr, mobile1, mobile2, height, mDate) VALUE" \
          "('"+ userID +"' , '"+ name +"' , '"+ birthYear +"' , '"+ addr +"' , '"+ mobile1 +"' , '"+ mobile2 +"' , '"+ height +"' , CURDATE())"
    cur.execute(sql)

conn.commit()
conn.close()

