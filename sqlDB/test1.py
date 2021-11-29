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
    game, gmonth, gweek, gold, cashratio, gtime, pay = "", "", "", "", "", "", ""

    game = edit1.get()
    gmonth = edit2.get()
    gweek = edit3.get()
    gold = edit4.get()
    cashratio = edit5.get()
    gtime = edit6.get()
    pay = edit7.get()

    # SQL 쿼리 만들기
    sql = ""
    sql = "INSERT INTO cashTBL (game,gmonth,gweek,gold,cashratio,gtime,pay) VALUES" \
          "('"+ game +"', '"+ gmonth +"','"+gweek+"','"+gold+"','"+cashratio+"','"+gtime+"','"+pay+"')"


    # 쿼리 실행
    try :
        cur.execute(sql)
    except :
        messagebox.showerror("입력 오류", "데이터 입력 오류가 발생했습니다.")
    else:
        # 쿼리 실행이 완료 (오류없이)
        # 1) 메시지 박스로 성공 알림
        messagebox.showinfo("성공", "일주일 고생하셨습니다.")
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
    edit7.delete(0, "end")
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



    lgame, lgmonth, lgweek, lgold, lcashratio, lgtime, lpay = [],[],[],[],[],[],[]


    lgame.append("게임 이름")
    lgame.append("---------")

    lgmonth.append("플레이 달")
    lgmonth.append("---------")

    lgweek.append("플레이 주차")
    lgweek.append("---------")

    lgold.append("획득 골드")
    lgold.append("---------")

    lcashratio.append("골드 현금 비율 1:")
    lcashratio.append("---------")

    lgtime.append("플레이타임(min)")
    lgtime.append("---------")

    lpay.append("최종교환 현금")
    lpay.append("---------")

    sql = 'SELECT * FROM cashTBL'
    cur.execute(sql)

    while(True) :
        row = cur.fetchone()

        if row == None:
            break

        #lgame, lgmonth, lgweek, lgold, lcashratio, lgtime, lpay
        lgame.append(row[0])
        lgmonth.append(row[1])
        lgweek.append(row[2])
        lgold.append(row[3])
        lcashratio.append(row[4])
        lgtime.append(row[5])
        lpay.append(row[6])

    #GUI ListBox에 insert
    # listgame, listgmonth, listgweek, listgold, listcasgratio, listgtime, listpay
    # 1) 리스트 박스 초기화
    listgame.delete(0, listgame.size()-1)
    listgmonth.delete(0, listgmonth.size() - 1)
    listgweek.delete(0, listgweek.size() - 1)
    listgold.delete(0, listgold.size() - 1)
    listcashratio.delete(0, listcashratio.size() - 1)
    listgtime.delete(0, listgtime.size() - 1)
    listpay.delete(0, listpay.size() - 1)

    # 2) select 해온 데이터 insert
    for item1, item2, item3, item4, item5, item6, item7 in \
            zip(lgame, lgmonth, lgweek, lgold, lcashratio, lgtime, lpay):
        listgame.insert(END, item1)
        listgmonth.insert(END, item2)
        listgweek.insert(END, item3)
        listgold.insert(END, item4)
        listcashratio.insert(END, item5)
        listgtime.insert(END, item6)
        listpay.insert(END, item7)

    conn.close()





# GUI 화면 구성
window = Tk()
window.geometry('1500x300')
window.title("게임 골드 시급 계산기")

editFrame = Frame(window)
editFrame.pack()

listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

label1 = Label(editFrame, text="게임 이름")
label1.pack(side=LEFT, padx=10, pady=10)
edit1 = Entry(editFrame, width=10)
edit1.pack(side=LEFT, padx=10, pady=10)

label2 = Label(editFrame, text="플레이 달")
label2.pack(side=LEFT, padx=10, pady=10)
edit2 = Entry(editFrame, width=10)
edit2.pack(side=LEFT, padx=10, pady=10)

label3 = Label(editFrame, text="플레이 주차")
label3.pack(side=LEFT, padx=10, pady=10)
edit3 = Entry(editFrame, width=10)
edit3.pack(side=LEFT, padx=10, pady=10)

label4 = Label(editFrame, text="획득 골드")
label4.pack(side=LEFT, padx=10, pady=10)
edit4 = Entry(editFrame, width=10)
edit4.pack(side=LEFT, padx=10, pady=10)

label5 = Label(editFrame, text="골드 현금 비율 1:")
label5.pack(side=LEFT, padx=10, pady=10)
edit5 = Entry(editFrame, width=10)
edit5.pack(side=LEFT, padx=10, pady=10)

label6 = Label(editFrame, text="플레이타임(min)")
label6.pack(side=LEFT, padx=10, pady=10)
edit6 = Entry(editFrame, width=10)
edit6.pack(side=LEFT, padx=10, pady=10)

label7 = Label(editFrame, text="최종교환 현금")
label7.pack(side=LEFT, padx=10, pady=10)
edit7 = Entry(editFrame, width=10)
edit7.pack(side=LEFT, padx=10, pady=10)

#버튼
btuInsert = Button(editFrame, text="입력", command=insertData)
btuInsert.pack(side=LEFT, padx=10, pady=10)

btuSelect = Button(editFrame, text="조회", command=selectData)
btuSelect.pack(side=LEFT, padx=10, pady=10)

btusum = Button(editFrame, text="총 얼마?", command=selectData)
btusum.pack(side=RIGHT, padx=10, pady=10)

# listgame, listgmonth, listgweek, listgold, listcashratio, listgtime, listpay
listgame = Listbox(listFrame)
listgame.pack(side=LEFT, fill=BOTH, expand=1)

listgmonth = Listbox(listFrame)
listgmonth.pack(side=LEFT, fill=BOTH, expand=1)

listgweek = Listbox(listFrame)
listgweek.pack(side=LEFT, fill=BOTH, expand=1)

listgold = Listbox(listFrame)
listgold.pack(side=LEFT, fill=BOTH, expand=1)

listcashratio = Listbox(listFrame)
listcashratio.pack(side=LEFT, fill=BOTH, expand=1)

listgtime = Listbox(listFrame)
listgtime.pack(side=LEFT, fill=BOTH, expand=1)

listpay = Listbox(listFrame)
listpay.pack(side=LEFT, fill=BOTH, expand=1)



window.mainloop()
