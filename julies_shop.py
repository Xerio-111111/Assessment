from tkinter import*
from datetime import datetime

def quit() :
    main_window.destroy()
    
def print_customer_details():
    global detail_count, total_entries
    detail_count = 0
    Label(main_window, font=("Helvetica 12"), text="Reciept Number").grid(column=0, row=7)
    Label(main_window, font=("Helvetica 10"), text="Name").grid(column=1, row=7)
    Label(main_window, font=("Helvetica 10"), text="Items Hired").grid(column=2, row=7)
    Label(main_window, font=("Helvetica 10"), text="Amount Hired").grid(column=3, row=7)
    Label(main_window, font=("Helvetica 10"), text="Order Date").grid(column=4, row=7)
    Label(main_window, font=("Helvetica 10"), text="Return Date").grid(column=5, row=7)
    while detail_count < total_entries:
        Label(main_window, text=detail_count).grid(column=0, row=detail_count+8)
        #Label(main_window, text=(customer_details[detail_count][0])).grid(column=1, row=detail_count+8)
        #Label(main_window, text=(customer_details[detail_count][1])).grid(column=2, row=detail_count+8)
        #Label(main_window, text=(customer_details[detail_count][2])).grid(column=3, row=detail_count+8)
        #Label(main_window, text=(customer_details[detail_count][3])).grid(column=4, row=detail_count+8)
        detail_count =+ 1

def check_inputs():
    global detail_count, entry_first_name, entry_last_name, entry_item_hire, entry_amount_hire, entry_order_date, entry_return_date, total_entries
    input_check = 0 
    Label(main_window, text="           ").grid(column=2, row=0)
    Label(main_window, text="           ").grid(column=2, row=1)
    Label(main_window, text="           ").grid(column=2, row=2)
    Label(main_window, text="           ").grid(column=2, row=3)
    if len(entry_first_name.get()) == 0:
        Label(main_window, fg="red" ,text="Required")
        input_check = 1
    if len(entry_last_name.get()) == 0:
        Label(main_window, fg="red" ,text="Required")
        input_check = 1 
    if len(entry_item_hire.get()) == 0:
        Label(main_window, fg="red" ,text="Required")
        input_check = 1 
    if len(entry_amount_hire.get().isdigit()):
        if int(entry_amount_hire.get()) < 0:
            Label(main_window, fg="red" ,text="Required")
            input_check = 1
    else:
        Label(main_window, fg="red" ,text="Required")
        input_check = 1
    if len(entry_order_date.get()) == 0 or "":
        Label(main_window, fg="red", text="Required")
        input_check = 1
    if len(entry_return_date.get()):
        Label(main_window, fg="red", text="Required")
        input_check = 1
        
    

def append_details():
    global detail_count, entry_first_name, entry_last_name, entry_item_hire, entry_amount_hire, entry_order_date, entry_return_date, total_entries
    detail_count.append([entry_first_name.get(),entry_last_name.get(),entry_item_hire.get(),entry_amount_hire.get(),entry_order_date.get(),entry_order_date.get()])
    entry_first_name.delete(0,'end')
    entry_last_name.delete(0,'end')
    entry_item_hire.delete(0,'end')
    entry_amount_hire.delete(0,'end')
    entry_order_date.delete(0,'end')
    entry_return_date.delete(0,'end')
    total_entries += 1

def setup():
    global entry_first_name, entry_last_name, entry_item_hire, entry_amount_hire, entry_order_date, entry_return_date, total_entries
    Label(main_window, font=("Helvetica 10"), text="First Name").grid(column=0,row=0,sticky=E)
    entry_first_name = Entry(main_window)
    entry_first_name.grid(column=1,row=0)
    Label(main_window, font=("Helvetica 10"), text="Last Name").grid(column=0,row=1,sticky=E)
    entry_last_name = Entry(main_window)
    entry_last_name.grid(column=1,row=1)
    Label(main_window, font=("Helvetica 10"), text="Items Hired").grid(column=0,row=2,sticky=E)
    entry_item_hire = Entry(main_window)
    entry_item_hire.grid(column=1,row=2)
    Label(main_window, font=("Helvetica 10"), text="Amount Hired").grid(column=0,row=3,sticky=E)
    entry_amount_hire = Entry(main_window)
    entry_amount_hire.grid(column=1,row=3)
    Label(main_window, font=("Helvetica 10"), text="Order Date").grid(column=0,row=4,sticky=E)
    entry_order_date = Entry(main_window)
    entry_order_date.grid(column=1,row=4)
    Label(main_window, font=("Helvetica 10"), text="Return Date").grid(column=0,row=5,sticky=E)
    entry_return_date = Entry(main_window)
    entry_return_date.grid(column=1,row=5)
    Label(main_window, font=("Helvetica 10"), text="Row #",)

def main():
    global main_window, total_entries
    total_entries = 0
    detail_count = []
    setup()
    Button(main_window, text="Quit", command=quit)
    Button(main_window, text="Append Details", command=check_inputs)
    main_window.mainloop()

main_window =Tk()
main()