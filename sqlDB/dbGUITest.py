import pymysql
from tkinter import *
from tkinter import messagebox


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
sql = "SELECT userID, name, birthYear, addr, " \
      "IFNULL(CONCAT(mobile1, '-',mobile2), '-') AS mobile, " \
      "IFNULL(height,0) AS height, " \
      "IFNULL(mDate,'-') AS mDate FROM userTBL;"

cur.execute(sql)

print("회원 ID  회원명 출생년도 주소    연락처     키    가입일 ")
print("-------------------------------------------------------------")

while(True) :
    row = cur.fetchone()
    if row == None :
        break
    userID = row[0]
    name = row[1]
    birthYear = row[2]
    addr = row[3]
    mobile = row[4]
    height = row[5]
    mDate = row[6]

    print("%5s %5s %d %5s %10s %d %5s" % (userID, name, birthYear, addr, mobile, height, mDate))


conn.close()


# GUI 화면 구성
window = Tk()
window.geometry('600x300')
window.title("MariaDB 연동 GUI")

editFrame = Frame(window)
editFrame.pack()

listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)





