import pymysql
from tkinter import *
from tkinter import messagebox



# 데이터베이스 연동 함수
def insertData():
    conn = None
    cur = None

    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',  # 접속계정의 계정명
        passwd='1234',  # 접속계정의 암호
        db='sqldb',  # 데이터베이스명
        charset='utf8')


    cur = conn.cursor()
    userID, name, birthYear, addr = "", "", "", ""

    userID = edit1.get()
    name = edit2.get()
    birthYear = edit3.get()
    addr = edit4.get()

    # SQL 쿼리 만들기
    sql = ""
    sql = "INSERT INTO userTBL (userID, name, birthYear, addr, mDate) VALUES" \
          "('"+ userID +"', '"+ name +"','"+birthYear+"','"+addr+"', CURDATE())"



    # 쿼리 실행
    try :
        cur.execute(sql)
    except :
        messagebox.showerror("입력 오류", "데이터 입력 오류가 발생했습니다.")
    else:
        # 쿼리 실행이 완료 (오류없이)
        # 1) 메시지 박스로 성공 알림
        messagebox.showinfo("성공","회원 정보가 등록되었습니다.")
        # 2) 데이터 커밋 (진짜 저장)
        conn.commit()
        # 3) 테이블 조회 (새로고침)
        selectData()

    # GUI에 입력한 데이터 삭제
    edit1.delete(0, "end")
    edit2.delete(0, "end")
    edit3.delete(0, "end")
    edit4.delete(0, "end")
    # DB 접속 종료
    conn.close()



def selectData():
    conn = None
    cur = None

    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',  # 접속계정의 계정명
        passwd='1234',  # 접속계정의 암호
        db='sqldb',  # 데이터베이스명
        charset='utf8')

    cur = conn.cursor()
    conn.commit()



    lUserID, lName, lBirthYear, lAddr = [],[],[],[]


    lUserID.append("회원 ID")
    lUserID.append("---------")

    lName.append("회원명")
    lName.append("---------")

    lBirthYear.append("출생년도")
    lBirthYear.append("---------")

    lAddr.append("회원주소")
    lAddr.append("---------")

    sql = 'SELECT userID, name, birthYear, addr FROM userTBL ORDER BY mDate DESC'
    cur.execute(sql)

    while(True) :
        row = cur.fetchone()

        if row == None:
            break

        #lUserID, lName, lBirthYear, lAddr
        lUserID.append(row[0])
        lName.append(row[1])
        lBirthYear.append(row[2])
        lAddr.append(row[3])

    #GUI ListBox에 insert
    # listUserID, listName, listBirthYear, listAddr
    # 1) 리스트 박스 초기화
    listUserID.delete(0, listUserID.size()-1)
    listName.delete(0, listName.size() - 1)
    listBirthYear.delete(0, listBirthYear.size() - 1)
    listAddr.delete(0, listAddr.size() - 1)

    # 2) select 해온 데이터 insert
    for item1, item2, item3, item4 in zip(lUserID, lName, lBirthYear, lAddr) :
        listUserID.insert(END, item1)
        listName.insert(END, item2)
        listBirthYear.insert(END, item3)
        listAddr.insert(END, item4)

    conn.close()

# GUI 화면 구성
window = Tk()
window.geometry('800x300')
window.title("MariaDB 연동 GUI")

editFrame = Frame(window)
editFrame.pack()

listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

label1 = Label(editFrame, text="회원ID")
label1.pack(side=LEFT, padx=10, pady=10)
edit1 = Entry(editFrame, width=10)
edit1.pack(side=LEFT, padx=10, pady=10)

label2 = Label(editFrame, text="회원명")
label2.pack(side=LEFT, padx=10, pady=10)
edit2 = Entry(editFrame, width=10)
edit2.pack(side=LEFT, padx=10, pady=10)

label3 = Label(editFrame, text="출생년도")
label3.pack(side=LEFT, padx=10, pady=10)
edit3 = Entry(editFrame, width=10)
edit3.pack(side=LEFT, padx=10, pady=10)

label4 = Label(editFrame, text="회원 주소")
label4.pack(side=LEFT, padx=10, pady=10)
edit4 = Entry(editFrame, width=10)
edit4.pack(side=LEFT, padx=10, pady=10)

#버튼
btuInsert = Button(editFrame, text="입력", command=insertData)
btuInsert.pack(side=LEFT, padx=10, pady=10)

btuSelect = Button(editFrame, text="조회", command=selectData)
btuSelect.pack(side=LEFT, padx=10 , pady=10)

listUserID = Listbox(listFrame)
listUserID.pack(side=LEFT, fill=BOTH, expand=1)

listName = Listbox(listFrame)
listName.pack(side=LEFT, fill=BOTH, expand=1)

listBirthYear = Listbox(listFrame)
listBirthYear.pack(side=LEFT, fill=BOTH, expand=1)

listAddr = Listbox(listFrame)
listAddr.pack(side=LEFT, fill=BOTH, expand=1)

window.mainloop()


