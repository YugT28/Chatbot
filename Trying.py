

from chatbot import *

from tkinter import *
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

root=Tk()
def click():
    msg=ent.get()
    tex.configure(state=NORMAL)
    tex.insert(END,"You:- "+msg+"\n")
    tex.configure(state=DISABLED)
    tex.see(END)t
    
def Bot(x):
    tex.configure(state=NORMAL)
    tex.insert(END,x+"\n")
    tex.configure(state=DISABLED)
    tex.see(END)
    
def CustomerCare():
    top=Toplevel()
    top.title("2")
    
    top.resizable(width=False, height=False)
    top.configure(width=470, height=550)

    line1 = Label(top, width=450, bg=BG_GRAY)
    line1.place(relwidth=1, rely=0.07, relheight=0.012)
        
    tex1 = Text(top, width=20, height=2,font=FONT, padx=5, pady=5)
    tex1.place(relheight=0.745, relwidth=1, rely=0.08)
    tex1.configure(cursor="arrow",state=DISABLED)

    scrollbar1 = Scrollbar(top)
    scrollbar1.place(relheight=1,relx=0.974)
    scrollbar1.configure(command=tex.yview)

    bottom_label1 = Label(top, bg=BG_GRAY,height=80)
    bottom_label1.place(relwidth=1, rely=0.825)   

    send_button1 = Button(bottom_label1, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,command=click)
    send_button1.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    ent1=Entry(bottom_label1,font=FONT)
    ent1.place(relwidth=0.75,relheight=0.07)

    
    
root.title("Chat")
root.resizable(width=False, height=False)
root.configure(width=470, height=550)

line = Label(root, width=450, bg=BG_GRAY)
line.place(relwidth=1, rely=0.07, relheight=0.012)
        
tex = Text(root, width=20, height=2,font=FONT, padx=5, pady=5)
tex.place(relheight=0.745, relwidth=1, rely=0.08)
tex.configure(cursor="arrow",state=DISABLED)

scrollbar = Scrollbar(root)
scrollbar.place(relheight=1,relx=0.974)
scrollbar.configure(command=tex.yview)

bottom_label = Label(root, bg=BG_GRAY,height=80)
bottom_label.place(relwidth=1, rely=0.825)   

send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,command=CustomerCare)
send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

ent=Entry(bottom_label,font=FONT)
ent.place(relwidth=0.75,relheight=0.07)

root.mainloop()




