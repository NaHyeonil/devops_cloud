from tkinter import *

#문자를 표현할 수 있는 라벨 사용
window = Tk()
window.title("라벨 연습")
window.geometry("400x100") #넓이 * 높이

#라벨 선언
label1  = Label(window, text="This is MariaDB를")
label2  = Label(window, text="열심히", font=("궁서체",30),fg="blue")
label3  = Label(window, text="공부 중입니다.", bg="magenta",width=20,height=5)
                #부모 윈도우, 출력될 글, 설정:font, fg=글자색, bg=배경색, anchor는 글자의 위치

#위젯 적용
label1.pack()
label2.pack()
label3.pack()

#GUI 화면 코딩

window.mainloop()