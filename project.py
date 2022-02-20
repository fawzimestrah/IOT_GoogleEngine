
import googlesearch
from tkinter import *
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")



struct=Tk()
struct.geometry("354x400") #Defining Size of GUI box
struct.title("My Search Engine") 
label=Label(struct,text="Personal Search Engine",bg="teal",fg="white",font=("Times",20,"bold"))
label.pack(side=TOP) 
struct.config(background="teal")
query=StringVar()
country=StringVar()
num=IntVar()
start=IntVar()
stop=IntVar()
pause=IntVar()
tld=StringVar()
def mysearch():
    try:
        query1 =query.get()
        country1 =country.get()
        num1 =num.get()
        start1 =start.get()
        stop1 =stop.get()
        pause1 =pause.get()
        tld1=tld.get()
        file1 = open(query1+".txt","w")
    except:
        clear()
        return 0
    list1=[]
    for j in search(query1 ,country=country1,safe="off", num=num1,start=start1, stop=stop1, pause=pause1):
        file1.writelines(j)
        file1.writelines("\n")
        #list1.append(j)
        print(j)
        
def clear():
    query.set("")
    country.set("")
    num.set(0)
    start.set(0)
    stop.set(0)
    pause.set(0)
    tld.set("")
    
label=Label(struct,text="Enter here to search",bg="teal",fg="white",font=("Times",15,"bold"))
label.place(x=50,y=100)
label=Label(struct,text="query",bg="teal",fg="white",font=("Times",10,"bold"))
label.place(x=50,y=130)
label=Label(struct,text="country",bg="teal",fg="white",font=("Times",10,"bold"))
label.place(x=50,y=160)
label=Label(struct,text="num",bg="teal",fg="white",font=("Times",10,"bold"))
label.place(x=50,y=190)
label=Label(struct,text="start",bg="teal",fg="white",font=("Times",10,"bold"))
label.place(x=50,y=220)
label=Label(struct,text="stop",bg="teal",fg="white",font=("Times",10,"bold"))
label.place(x=50,y=250)
label=Label(struct,text="pause",bg="teal",fg="white",font=("Times",10,"bold"))
label.place(x=50,y=280)
label=Label(struct,text="tld",bg="teal",fg="white",font=("Times",10,"bold"))
label.place(x=50,y=310)






enter=Entry(struct,font=("Times",10,"bold"),textvar=query,width=30,bd=2,bg="white")
enter.place(x=120,y=130)
enter1=Entry(struct,font=("Times",10,"bold"),textvar=country,width=30,bd=2,bg="white")
enter1.place(x=120,y=160)
enter=Entry(struct,font=("Times",10,"bold"),textvar=num,width=30,bd=2,bg="white")
enter.place(x=120,y=190)
enter1=Entry(struct,font=("Times",10,"bold"),textvar=start,width=30,bd=2,bg="white")
enter1.place(x=120,y=220)
enter=Entry(struct,font=("Times",10,"bold"),textvar=stop,width=30,bd=2,bg="white")
enter.place(x=120,y=250)
enter1=Entry(struct,font=("Times",10,"bold"),textvar=pause,width=30,bd=2,bg="white")
enter1.place(x=120,y=280)
enter1=Entry(struct,font=("Times",10,"bold"),textvar=tld,width=30,bd=2,bg="white")
enter1.place(x=120,y=310)



button1=Button(struct,text="clear",font=("Times",10,"bold"),width=15,bd=2,command=clear)
button1.place(x=70,y=340)
button=Button(struct,text="Search",font=("Times",10,"bold"),width=15,bd=2,command=mysearch)
button.place(x=200,y=340)
struct.mainloop()

file1.close()