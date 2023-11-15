from tkinter import *

mw = Tk()
mw.title('calculator')
# Entry display
num1 = Entry(mw,width=50)
num1.grid(row=0, column=0, columnspan=3,pady=10,padx=10)
# result display
r_l=Label(mw,text='Result')
r_l.grid(row=7,column=1)
result_d = Entry(mw)
result_d.grid(row=8, column=0, columnspan=3,padx=60)

# functions------------------------------------------
#count is used to upgrade index when we enter value or symbol
# i make count as global becaues it has to upgrade when we enter any symbol or value
count = 0
def zero():
    global count
    num = 0
    num1.insert(count, num)
    count += 1
def one():
    global count
    num = 1
    num1.insert(count, num)
    count += 1
def two():
    global count
    num = 2
    num1.insert(count, num)
    count += 1
def three():
    global count
    num = 3
    num1.insert(count, num)
    count += 1
def four():
    global count
    num = 4
    num1.insert(count, num)
    count += 1
def five():
    global count
    num = 5
    num1.insert(count, num)
    count += 1
def six():
    global count
    num = 6
    num1.insert(count, num)
    count += 1
def seven():
    global count
    num = 7
    num1.insert(count, num)
    count += 1
def eight():
    global count
    num = 8
    num1.insert(count, num)
    count += 1
def nine():
    global count
    num = 9
    num1.insert(count, num)
    count += 1
# symbol functions------------------------------------------------------------------------
def mux():
    global count
    num = "*"
    num1.insert(count, num)
    count += 1
def div():
    global count
    num = "/"
    num1.insert(count, num)
    count += 1
def add():
    global count
    num = "+"
    num1.insert(count, num)
    count += 1
def sub():
    global count
    num = "-"
    num1.insert(count, num)
    count += 1
def cons():
    result = num1.get()
    try:
        res = eval(result)
    except SyntaxError:
        res = 'check'
    finally:
        result_d.insert(0, res)
def clear():
    num1.delete(0, END)
    result_d.delete(0, END)
def undo():
    t = num1.get()
    le = len(t)
    num1.delete(le - 1, END)
# buttons and function linking for numbers
button_0 = Button(mw, text="0", padx=36, pady=10, command=zero)
button_1 = Button(mw, text="1", padx=36, pady=10, command=one)
button_2 = Button(mw, text="2", padx=36, pady=10, command=two)
button_3 = Button(mw, text="3", padx=36, pady=10, command=three)
button_4 = Button(mw, text="4", padx=36, pady=10, command=four)
button_5 = Button(mw, text="5", padx=36, pady=10, command=five)
button_6 = Button(mw, text="6", padx=36, pady=10, command=six)
button_7 = Button(mw, text="7", padx=36, pady=10, command=seven)
button_8 = Button(mw, text="8", padx=36, pady=10, command=eight)
button_9 = Button(mw, text="9", padx=36, pady=10, command=nine)
# buttons and function linking for clear and undo
button_clear = Button(mw, text='clear', padx=36, pady=10, command=clear)
button_undo = Button(mw, text="undo", padx=36, pady=10, command=undo)
# buttons and linking for mathematical functions
button_mux = Button(mw, text='*', padx=36, pady=10, command=mux)
button_div = Button(mw, text='/', padx=36, pady=10, command=div)
button_add = Button(mw, text='+', padx=36, pady=10, command=add)
button_sub = Button(mw, text='-', padx=36, pady=10, command=sub)
button_equal = Button(mw, text="=", padx=46, pady=30, command=cons)
# To display function on window
button_1.grid(row=3, column=0, padx=2, pady=2)
button_2.grid(row=3, column=1, padx=2, pady=2)
button_3.grid(row=3, column=2, padx=2, pady=2)
button_4.grid(row=2, column=0, padx=2, pady=2)
button_5.grid(row=2, column=1, padx=2, pady=2)
button_6.grid(row=2, column=2, padx=2, pady=2)
button_7.grid(row=1, column=0, padx=1, pady=2)
button_8.grid(row=1, column=1, padx=2, pady=2)
button_9.grid(row=1, column=2, padx=2, pady=2)
button_0.grid(row=4, column=0, padx=2, pady=2)

button_clear.grid(row=4, column=2, padx=2, pady=2)
button_undo.grid(row=4, column=1, padx=2, pady=2)

button_mux.grid(row=5, column=0, padx=2, pady=2)
button_div.grid(row=5, column=1, padx=2, pady=2)
button_add.grid(row=6, column=0, padx=2, pady=2)
button_sub.grid(row=6, column=1, padx=2, pady=2)
button_equal.grid(row=5, column=2, rowspan=2)

mw.mainloop()
''' from this project i learn
entry---   to show  display for inserting data
get() --- to get the data present in display but we have to write.get method in some function and we 
           have to create button for it
insert---- to insert data into display box insert(index,value)
grid() or pack()  --- is mandatory to add content to window
Label  -----to add matter on window
Button ----- To create button  in  which command is used  to link button and function
'''
