from tkinter import*
from datetime import datetime

#quit the program
def quit() :
    main_window.destroy()

#print the customers details 
def print_customer_details():
    #global variables
    global detail_count, total_entries
    detail_count = 0
    #creating column headings
    Label(main_window, font=("Helvetica 12"), text="Customer ID").grid(column=0, row=7)
    Label(main_window, font=("Helvetica 10"), text="Name").grid(column=1, row=7)
    Label(main_window, font=("Helvetica 10"), text="Items Hired").grid(column=2, row=7)
    Label(main_window, font=("Helvetica 10"), text="Amount Hired").grid(column=3, row=7)
    Label(main_window, font=("Helvetica 10"), text="Order Date").grid(column=4, row=7)
    Label(main_window, font=("Helvetica 10"), text="Return Date").grid(column=5, row=7)
    #adding items in the list
    while detail_count < total_entries:
        Label(main_window, text=detail_count).grid(column=0, row=detail_count+8)
        Label(main_window, text=(customer_detail[detail_count][0])).grid(column=1, row=detail_count+8)
        Label(main_window, text=(customer_detail[detail_count][1])).grid(column=2, row=detail_count+8)
        Label(main_window, text=(customer_detail[detail_count][2])).grid(column=3, row=detail_count+8)
        Label(main_window, text=(customer_detail[detail_count][3])).grid(column=4, row=detail_count+8)
        Label(main_window, text=(customer_detail[detail_count][4])).grid(column=5, row=detail_count+8)
        Label(main_window, text=(customer_detail[detail_count][5])).grid(column=6, row=detail_count+8)
        detail_count =+ 1
        
#checks vadility of inputs
def check_inputs():
    #global variables
    global detail_count, entry_first_name, entry_last_name, entry_item_hire, entry_amount_hire, entry_order_date, entry_return_date, input_check, total_entries
    input_check = 0 
    #reset the "required" text
    Label(main_window, text="           ").grid(column=2, row=0)
    Label(main_window, text="           ").grid(column=2, row=1)
    Label(main_window, text="           ").grid(column=2, row=2)
    Label(main_window, text="           ").grid(column=2, row=3)
    Label(main_window, text="           ").grid(column=2, row=4)
    Label(main_window, text="           ").grid(column=2, row=5)
#checks if there is no input or an invalid input
    if len(entry_first_name.get()) == 0:
        Label(main_window, fg="red" ,text="Required")
        input_check = 1
#checks if there is no input or an invalid input
    if len(entry_last_name.get()) == 0:
        Label(main_window, fg="red" ,text="Required")
        input_check = 1 
#checks if there is no input or an invalid input
    if len(entry_item_hire.get()) == 0:
        Label(main_window, fg="red" ,text="Required")
        input_check = 1 
#checks if there is no input, invalid input or less than 0
    if len(entry_amount_hire.get().isdigit()):
        if int(entry_amount_hire.get()) < 0:
            Label(main_window, fg="red" ,text="Required")
            input_check = 1
    else:
        Label(main_window, fg="red" ,text="Required")
        input_check = 1
#checks if there is no input or an invalid input0 
    if len(entry_order_date.get()) == 0:
        Label(main_window, fg="red", text="Required")
        input_check = 1
#checks if there is no input or an invalid input
    if len(entry_return_date.get()) == 0:
        Label(main_window, fg="red", text="Required")
        input_check = 1

#add details to the customer detail list
def append_details():
#global variables
    global detail_count, entry_first_name, entry_last_name, entry_item_hire, entry_amount_hire, entry_order_date, entry_return_date, total_entries
#append the inputs
    customer_detail.append([entry_first_name.get(),entry_last_name.get(),entry_item_hire.get(),entry_amount_hire.get(),entry_order_date.get(),entry_order_date.get()])
#clear the input boxes
    entry_first_name.delete(0,'end')
    entry_last_name.delete(0,'end')
    entry_item_hire.delete(0,'end')
    entry_amount_hire.delete(0,'end')
    entry_order_date.delete(0,'end')
    entry_return_date.delete(0,'end')
    total_entries += 1

def delete_row():
#global variables
    global customer_detail, total_entries, delete_item, detail_count
    #delete the row
    del customer_detail[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0, 'end')
    #clear the deleted item
    Label(main_window, text="           ").grid(column=0, row=detail_count+7)
    Label(main_window, text="           ").grid(column=1, row=detail_count+7)
    Label(main_window, text="           ").grid(column=2, row=detail_count+7)
    Label(main_window, text="           ").grid(column=3, row=detail_count+7)
    Label(main_window, text="           ").grid(column=4, row=detail_count+7)
    Label(main_window, text="           ").grid(column=5, row=detail_count+7)
    #reprint items
    print_customer_details()

def setup():
    #global Variables
    global entry_first_name, entry_last_name, entry_item_hire, entry_amount_hire, entry_order_date, entry_return_date, total_entries, delete_item
    #creating the labels and input boxes for the shop 
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
    Label(main_window, font=("Helvetica 10"), text="Row (#)").grid(column=0, row=6)
    delete_item = Entry(main_window)
    delete_item.grid(column=1, row=6)
    Button(main_window, text="Quit", command=quit)
    Button(main_window, text="Append Details", command=check_inputs)
    

def main():
    #Global Variables
    global main_window, total_entries, customer_detail, full_name
    customer_detail = []
    total_entries = 0
    #Creating GUI
    main_window =Tk()
    setup()
    main_window.mainloop()
main()
