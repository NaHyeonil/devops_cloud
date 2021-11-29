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
        db='cashcalculator',  # 데이터베이스명
        charset='utf8')


    cur = conn.cursor()
    game, gmonth, gweek, gold, cashratio, gtime = "", "", "", "", "", ""

    game = edit1.get()
    gmonth = edit2.get()
    gweek = edit3.get()
    gold = edit4.get()
    cashratio = edit5.get()
    gtime = edit6.get()

    # SQL 쿼리 만들기
    sql = ""
    sql = "INSERT INTO cashcalculator VALUES" \
          "('"+ game +"', '"+ gmonth +"','"+gweek+"','"+gold+"','"+cashratio+"','"+gtime+"')"



    # 쿼리 실행
    try :
        cur.execute(sql)
    except :
        messagebox.showerror("입력 오류", "데이터 입력 오류가 발생했습니다.")
    else:
        # 쿼리 실행이 완료 (오류없이)
        # 1) 메시지 박스로 성공 알림
        messagebox.showinfo("성공")
        # 2) 데이터 커밋 (진짜 저장)
        conn.commit()
        # 3) 테이블 조회 (새로고침)
        selectData()

    # GUI에 입력한 데이터 삭제
    edit1.delete(0, "end")
    edit2.delete(0, "end")
    edit3.delete(0, "end")
    edit4.delete(0, "end")
    edit5.delete(0, "end")
    edit6.delete(0, "end")
    # DB 접속 종료
    conn.close()



def selectData():
    conn = None
    cur = None

    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',  # 접속계정의 계정명
        passwd='1234',  # 접속계정의 암호
        db='cashcalculator',  # 데이터베이스명
        charset='utf8')

    cur = conn.cursor()
    conn.commit()



    lPay = []


    lPay.append("시급 기준")
    lPay.append("---------")


    sql = 'SELECT SUM(((gold*cashratio)/gtime)*60) AS "시급(원)" FROM cashcalculator'
    cur.execute(sql)

    while(True) :
        row = cur.fetchone()

        if row == None:
            break

        #lUserID, lName, lBirthYear, lAddr
        lPay.append(row[0])

    #GUI ListBox에 insert
    # listUserID, listName, listBirthYear, listAddr
    # 1) 리스트 박스 초기화
    listPay.delete(0, listPay.size()-1)

    # 2) select 해온 데이터 insert
    for item1 in zip(lPay) :
        listPay.insert(END, item1)


    conn.close()

# GUI 화면 구성
window = Tk()
window.geometry('1000x300')
window.title("게임 골드 시급 계산기")

editFrame = Frame(window)
editFrame.pack()

listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

label1 = Label(editFrame, text="게임명")
label1.pack(side=LEFT, padx=10, pady=10)
edit1 = Entry(editFrame, width=10)
edit1.pack(side=LEFT, padx=10, pady=10)

label2 = Label(editFrame, text="월")
label2.pack(side=LEFT, padx=10, pady=10)
edit2 = Entry(editFrame, width=10)
edit2.pack(side=LEFT, padx=10, pady=10)

label3 = Label(editFrame, text="주차")
label3.pack(side=LEFT, padx=10, pady=10)
edit3 = Entry(editFrame, width=10)
edit3.pack(side=LEFT, padx=10, pady=10)

label4 = Label(editFrame, text="획득골드")
label4.pack(side=LEFT, padx=10, pady=10)
edit4 = Entry(editFrame, width=10)
edit4.pack(side=LEFT, padx=10, pady=10)

label5 = Label(editFrame, text="교환비율")
label5.pack(side=LEFT, padx=10, pady=10)
edit5 = Entry(editFrame, width=10)
edit5.pack(side=LEFT, padx=10, pady=10)

label6 = Label(editFrame, text="플레이타임")
label6.pack(side=LEFT, padx=10, pady=10)
edit6 = Entry(editFrame, width=10)
edit6.pack(side=LEFT, padx=10, pady=10)

#버튼
btuInsert = Button(editFrame, text="계산", command=insertData)
btuInsert.pack(side=LEFT, padx=10, pady=10)

listPay = Listbox(listFrame)
listPay.pack(side=LEFT, fill=BOTH, expand=1)


window.mainloop()


