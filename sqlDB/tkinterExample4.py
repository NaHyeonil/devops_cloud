from tkinter import *
from tkinter import messagebox

#버튼을 사용하여 알림 창 띄우기
def clickButtion() :
    messagebox.showinfo("버튼 클릭", "버튼을 클릭했습니다.") #메세지 버튼 타이틀

#문자를 표현할 수 있는 라벨 사용
window = Tk()
window.title("버튼 이벤트 연습")
window.geometry("200x200")

button1 = Button(window, text="요기 눌러요1", command=clickButtion)
button2 = Button(window, text="요기 눌러요2", command=clickButtion)
button3 = Button(window, text="요기 눌러요3", command=clickButtion)

button1.pack(side=TOP, padx=10, pady=10)
button2.pack(side=TOP, padx=10, pady=10)
button3.pack(side=TOP, padx=10, pady=10)




#GUI 화면 코딩

window.mainloop()