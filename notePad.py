import tkinter as tk
out=""
def COF():
    f_o=open(fn.get()+".txt","w")
    f_o.write(m.get("1.0","end-1c"))
    f_o.close()

def AF():
    f_o=open(fn.get()+".txt","a")
    f_o.write(m.get("1.0","end-1c"))
    f_o.close()

def OF():
    f_o=open(fn.get()+".txt","r")
    '''lines = f_o.readlines()
    for line in lines:
        print(line,end='')'''
    c=f_o.read()
    m.insert('1.0',c)
    f_o.close()



window = tk.Tk()

fn=tk.Entry()
l1=tk.Label(window,text="Enter file name")

m=tk.Text(window,height=10)
l2=tk.Label(window,text="Enter text here")

b1=tk.Button(window,text="Create/OverWrite file",command=COF)
b2=tk.Button(window,text="Add to / update file",command=AF)
b3=tk.Button(window,text="open file",command=OF)
l1.pack()
fn.pack()
l2.pack()
m.pack()
b1.pack()
b2.pack()
b3.pack()
tk.Button(window,text="Exit",command=window.destroy).pack()

window.title("Notepad")
window.geometry("700x400")
window.mainloop()
