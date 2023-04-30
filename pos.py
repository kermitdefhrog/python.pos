from tkinter import *
import tkinter as tk
import hashlib
import datetime
import os
import time
import stripe

#author: kermit huddleston
#todo 
# do cardless stuff - not going to happen even though i would like to
#it seems like most ways of taking cardless payments really want you to use a card reader and the 
#only ways that i have seen examples of doing it without a card reader are for web based stuff and 
# dont think that putting it in this python program would be acceptable to do it that way
#be able to select items in the text boxes and delete them - low priority
#make the ui look better - very low priority since its never going to be used by anyone other than me
#globals need to move them up here when i get the chance
cash_in_till = 0.0
running_total = 0.0
cash_tendered = 0.0
approval = False
employee_name = ""
manager_id = ""
manager_password = ""
emp_id = ""
emp_name = ""
#functions
#this on is really the manager password screen I really should have named these all more clearly since now its confusing the hell out of me
def on_manager_enter(id):
    #buttons for password and a new window for the manager to enter in the password
    manager_pass_window = tk.Toplevel()
    manager_pass_window.title("Manager")
    manager_pass_window.geometry("800x600")
    frame = tk.Frame(manager_pass_window)
    manager_pass_box = tk.Text(frame, height=2, width=20)
    manager_pass_box.pack()
    frame.pack()
    #buttons for the manager password
    mgmt_pass_btn = tk.Frame(manager_pass_window, padx=10)
    tk.Button(mgmt_pass_btn, text="1", command=lambda: on_manager_pass_click("1")).grid(column=0, row=0)
    tk.Button(mgmt_pass_btn, text="2", command=lambda: on_manager_pass_click("2")).grid(column=1, row=0)
    tk.Button(mgmt_pass_btn, text="3", command=lambda: on_manager_pass_click("3")).grid(column=2, row=0)
    tk.Button(mgmt_pass_btn, text="4", command=lambda: on_manager_pass_click("4")).grid(column=3, row=0)
    tk.Button(mgmt_pass_btn, text="5", command=lambda: on_manager_pass_click("5")).grid(column=4, row=0)
    tk.Button(mgmt_pass_btn, text="6", command=lambda: on_manager_pass_click("6")).grid(column=5, row=0)
    tk.Button(mgmt_pass_btn, text="7", command=lambda: on_manager_pass_click("7")).grid(column=6, row=0)
    tk.Button(mgmt_pass_btn, text="8", command=lambda: on_manager_pass_click("8")).grid(column=7, row=0)
    tk.Button(mgmt_pass_btn, text="9", command=lambda: on_manager_pass_click("9")).grid(column=8, row=0)
    tk.Button(mgmt_pass_btn, text="0", command=lambda: on_manager_pass_click("0")).grid(column=9, row=0)
    tk.Button(mgmt_pass_btn, text="reset", command=lambda: on_manager_pass_click("reset")).grid(column=10, row=0)
    tk.Button(mgmt_pass_btn, text="enter", command=lambda: on_passcheck()).grid(column=11, row=0)
    mgmt_pass_btn.pack()
    tk.Label(manager_pass_window, text="Manager password enter").pack()


    #this is for getting the manager password
    def on_manager_pass_click(value):
        nomoreredlines = 1 + 1
        global manager_password
        if value == "reset":
            manager_password = ""
        else:
            manager_password = manager_password + value
        manager_pass_box.delete("1.0", tk.END)
        #probably want to change this to a * so that the password is hidden
        manager_pass_box.insert(tk.END, "*" * len(manager_password))

    #this takes the id and hashes the password and then checks it against the shadow file
    def on_passcheck():
        global manager_password
        global manager_id
        with open("shadow") as f:
            for line in f:
                line = line.strip()
                file_id = line.split(":")[0]
                file_password = line.split(":")[1]
                if file_id == manager_id:
                    hashed_password = hashlib.sha256(manager_password.encode()).hexdigest()
                    if file_password == hashed_password:
                        manager_screen()
                        manager_pass_window.destroy()
                        #clears the manager id and password variables so that they can be used again next time also clears the file id and password variables they should be cleared anyways but just to be safe
                        manager_id = ""
                        manager_password = ""
                        file_id = ""
                        file_password = ""
                        manager_pass_window.destroy()                        
                    else:
                        #clears the manager id and password variables so that they can be used again next time also clears the file id and password variables they should be cleared anyways but just to be safe
                        manager_id = ""
                        manager_password = ""
                        file_id = ""
                        file_password = ""
                        manager_pass_window.destroy()

                #clears the manager id and password variables so that they can be used again next time also clears the file id and password variables they should be cleared anyways but just to be safe
                manager_id = ""
                manager_password = ""
                file_id = ""
                file_password = ""

#this is for when the user will click the manager button on the default screen
def on_manager_click():
    #creates a new window that has a login screen for the manager
    manager_id_window = tk.Toplevel()
    manager_id_window.title("Manager")
    manager_id_window.geometry("800x600")
    frame = tk.Frame(manager_id_window)
    manager_box = tk.Text(frame, height=2, width=20)
    manager_box.pack()
    frame.pack()
    #buttons for the manager id
    mgmt_btn = tk.Frame(manager_id_window, padx=10)
    tk.Button(mgmt_btn, text="1", command=lambda: on_id_click("1")).grid(column=0, row=0)
    tk.Button(mgmt_btn, text="2", command=lambda: on_id_click("2")).grid(column=1, row=0)
    tk.Button(mgmt_btn, text="3", command=lambda: on_id_click("3")).grid(column=2, row=0)
    tk.Button(mgmt_btn, text="4", command=lambda: on_id_click("4")).grid(column=3, row=0)
    tk.Button(mgmt_btn, text="5", command=lambda: on_id_click("5")).grid(column=4, row=0)
    tk.Button(mgmt_btn, text="6", command=lambda: on_id_click("6")).grid(column=5, row=0)
    tk.Button(mgmt_btn, text="7", command=lambda: on_id_click("7")).grid(column=6, row=0)
    tk.Button(mgmt_btn, text="8", command=lambda: on_id_click("8")).grid(column=7, row=0)
    tk.Button(mgmt_btn, text="9", command=lambda: on_id_click("9")).grid(column=8, row=0)
    tk.Button(mgmt_btn, text="0", command=lambda: on_id_click("0")).grid(column=9, row=0)
    tk.Button(mgmt_btn, text="reset", command=lambda: on_id_click("reset")).grid(column=10, row=0)
    tk.Button(mgmt_btn, text="enter", command=lambda: [on_manager_enter(manager_id), manager_id_window.destroy()]).grid(column=11, row=0)
    mgmt_btn.pack()
    tk.Label(manager_id_window, text="Enter Manager ID").pack()
    #this is for getting the manager id number its very similar to the function on_number_click but i had to modify it so I couldn't just use the same function
    def on_id_click(value):
        global manager_id
        if value == "reset":
            manager_id = ""
        else:
            manager_id = manager_id + value
        manager_box.delete("1.0", tk.END)
        manager_box.insert(tk.END, manager_id)
#manager option for approving a transaction
def on_approve_click():
    global approval
    approval = True
#this screen is for actual manager options on the till 
def manager_screen():
    nomore_red_lines = 1 + 1
    manager_screen = tk.Toplevel()
    manager_screen.title("Manager")
    manager_screen.geometry("800x600")
    frame = tk.Frame(manager_screen)
    #buttons for manager options
    tk.Button(frame, text="Check Drawer", command=lambda: on_check_drawer_click()).grid(column=0, row=0)
    tk.Button(frame, text="Close Till", command=lambda: on_close_till_click()).grid(column=1, row=0)
    tk.Button(frame, text="New Till", command=lambda: on_new_till_click()).grid(column=2, row=0)
    tk.Button(frame, text="Exit", command=manager_screen.destroy).grid(column=3, row=0)
    tk.Button(frame, text="add employee", command=lambda: add_user()).grid(column=4, row=0)
    tk.Button(frame, text="add manager" , command=lambda: add_manager()).grid(column=5, row=0)
    tk.Button(frame, text="approve order", command=lambda: on_approve_click()).grid(column=6, row=0)
    frame.pack()

#function for adding an employee to the till does not actually create a user account incase i decide to add that in later this is just for the name on till
def on_new_till_click():
    global cash_in_till
    cash_in_till = 0
    #creates a window for entering the employee id
    employee_enter_window = tk.Toplevel()
    employee_enter_window.title("Employee")
    employee_enter_window.geometry("800x600")
    frame = tk.Frame(employee_enter_window)
    employee_enter_box = tk.Text(frame, width=20)
    employee_enter_box.pack()
    frame.pack()
    employee_btn = tk.Frame(employee_enter_window, padx=10)
    tk.Button(employee_btn, text="1" , command=lambda: on_employee_number_click("1")).grid(column=0, row=0)
    tk.Button(employee_btn, text="2" , command=lambda: on_employee_number_click("2")).grid(column=1, row=0)
    tk.Button(employee_btn, text="3" , command=lambda: on_employee_number_click("3")).grid(column=2, row=0)
    tk.Button(employee_btn, text="4" , command=lambda: on_employee_number_click("4")).grid(column=3, row=0)
    tk.Button(employee_btn, text="5" , command=lambda: on_employee_number_click("5")).grid(column=4, row=0)
    tk.Button(employee_btn, text="6" , command=lambda: on_employee_number_click("6")).grid(column=5, row=0)
    tk.Button(employee_btn, text="7" , command=lambda: on_employee_number_click("7")).grid(column=6, row=0)
    tk.Button(employee_btn, text="8" , command=lambda: on_employee_number_click("8")).grid(column=7, row=0)
    tk.Button(employee_btn, text="9" , command=lambda: on_employee_number_click("9")).grid(column=8, row=0)
    tk.Button(employee_btn, text="0" , command=lambda: on_employee_number_click("0")).grid(column=9, row=0)
    tk.Button(employee_btn, text="Enter" , command=lambda: employee_enter(emp_id)).grid(column=10, row=0)
    tk.Button(employee_btn, text="Exit", command=employee_enter_window.destroy).grid(column=11, row=0)
    tk.Button(employee_btn, text="Reset", command=lambda: on_employee_number_click("reset", employee_enter_box)).grid(column=12, row=0)
    employee_btn.pack()
    #function for adding in the employee id number its very similar to the function on_number_click 
    def on_employee_number_click(value):
        nomore_red_lines = 1 + 1
        global emp_id
        if value == "reset":
            emp_id = ""
        else:
            emp_id = emp_id + value
        employee_enter_box.delete("1.0", tk.END)
        employee_enter_box.insert(tk.END, emp_id)
    def employee_enter(emp_id):
        nomore_red_lines = 1 + 1
        global emp_name
        #gets the employee name from the ID 
        #opens the passwd file the format is emp_id:emp_name
        with open("passwd") as p:
            for line in p:
                id = line.split(":")[0]
                name = line.split(":")[1]
                if id == emp_id:
                    emp_name = name
                    lbl_emp_name.config(text=f"This till is in {emp_name}'s name")           
                    employee_enter_window.destroy()

#this function allows the manager to close the till and print out a reciept with the total amount of cash in the till
def print_drawer_receipt(cash_in_till):
    nomore_red_lines = 1 + 1
    #gets the date
    now = datetime.datetime.now()
    today = now.strftime("%m-%d-%Y")
    #looks for and creates directories for the year/month/day
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    if not os.path.exists("drawer_totals"):
        os.mkdir("drawer_totals")
    if not os.path.exists("drawer_totals/" + year):
        os.mkdir("drawer_totals/" + year)
    if not os.path.exists("drawer_totals/" + year + "/" + month):
        os.mkdir("drawer_totals/" + year + "/" + month)
    if not os.path.exists("drawer_totals/" + year + "/" + month + "/" + day):
        os.mkdir("drawer_totals/" + year + "/" + month + "/" + day)
    path_to_file = "drawer_totals/" + year + "/" + month + "/" + day
    #creates a file name based on the employee name and the time
    file_name = path_to_file + "/" + emp_name.strip() + now.strftime("%H-%M-%S") + ".txt"
    #creates a file and writes the reciept to it
    with open(file_name, "w") as file:
        global manager_id
        file.write("Drawer Total\n")
        file.write("Date: " + today + "\n")
        file.write("Time: " + now.strftime("%H:%M:%S") + "\n")
        file.write("Cash in till: ${:.2f}\n".format(cash_in_till))
        file.write("\n")
        file.write("Have a nice day!")
        file.close()
    cash_in_till = 0.0
#this function allows the manager to close the till and print out a reciept with the total amount of cash in the till
def on_close_till_click():
    nomore_red_lines = 1 + 1
    global cash_in_till
    lbl_emp_name = tk.Label(manager_screen, text=f"This till is in {emp_name}'s name")

    #print out a receipt and save the total to a file for auditing purposes
    print_drawer_receipt(cash_in_till)
#this function allows the manager to check to see how much cash is in the till

def on_check_drawer_click():
    nomore_red_lines = 1 + 1
    global cash_in_till
    check_drawer_window = tk.Toplevel()
    check_drawer_window.title("Drawer")
    check_drawer_window.geometry("800x600")
    frame = tk.Frame(check_drawer_window)
    check_drawer_box = tk.Text(frame, width=20)
    frame.pack()
    check_drawer_box.pack()
    check_drawer_box.delete("1.0", tk.END)
    check_drawer_box.insert(tk.END, "Cash in till: ${:.2f}\n".format(cash_in_till))
    tk.Button(frame, text="Exit", command=check_drawer_window.destroy).pack()    




#this function is for paying with a card and will be added in later but it might not get added since I cant really test it or anything but ill look into it
def on_card_click():
    nomoreredlines = 1 + 1
    #gets the last line that contains the total and splits it out of the string
    last_line = total_box.get("end-2l", "end-1l")
    last_line = last_line.split("$")
    last_line = float(last_line[1])
    final_total = last_line
    #start of the card processing
    #puts in my test key
    stripe.api_key = ""
    #creates a product for the card processing
    product = stripe.Product.create(
        name="Movie theater ticket", 
        description="consessions"
    )
    #creates a price for the card processing
    price = stripe.Price.create(
        #problems with this being an int?
        unit_amount=int(final_total * 100),
        currency="usd",
        product=product["id"],
    )
    #and it looks like thats as far as I can go since it looks like the only way you can take a payment like this is with a card reader 
    #since it looks like they don't want you to insert the card number into the program and then process it that way unless you are doing in online
    #or maybe not?
    stripe.PaymentIntent.create(
    amount = int(final_total * 100),
    currency = "usd",
    payment_method_types = ['card_present'],
    capture_method = 'manual',
    )


    stripe.Charge.create(
        amount = int(final_total * 100),
        currency = "usd",
        
    )
#this function resets the running total and the cash tendered
def on_reset_click():
    nomoreredlines = 1 + 1
    global running_total 
    global cash_tendered
    cash_tendered = 0.0
    running_total = 0
    running_total_box.delete("1.0", tk.END)
    #enable and disable the total box so it can be edited
    total_box.config(state="normal")
    total_box.delete("1.0", tk.END)
    total_box.config(state="disabled")
    quantity_box.delete("1.0", tk.END)
    quantity_box.insert(tk.END, "1")
#this function creates the cash handling screen it also calls some other functions that are related to the cash handling screen
def on_total_click():
    nomoreredlines = 1 + 1
    global emp_name
    #creates a new window that keeps the text boxes on the left side of the screen and will add in some cash and cashless payment options 
    total_window = tk.Toplevel()
    total_window.title("Total")
    total_window.geometry("800x600")
    frame = tk.Frame(total_window)
    running_total_box_screen2 = tk.Text(frame, width=20)
    running_total_box_screen2.grid(column=0, row=0)
    #disables the total box so it cant be edited since its actually used to calculate the total and if someone could edit it then they could just type in whatever they wanted
    total_box_screen2 = tk.Text(frame, width=20, state="disabled")
    total_box_screen2.grid(column=0, row=1)
    frame.pack(side="left", fill="y")
    running_total_box_screen2.insert(tk.END, running_total_box.get("1.0", tk.END))
    #going to enable the total box to be edited and then disable it after i write to it since if someone 
    #had a keyboard on the screen they could just type in whatever they wanted and since this actally gets used to calculate the total it would be bad
    total_box_screen2.config(state="normal")
    total_box_screen2.insert(tk.END, total_box.get("1.0", tk.END))
    total_box_screen2.config(state="disabled")
    #adds in text box to show cash amount
    #going to disable the cash box so it can't be edited and then enable when its needed 
    cash_box = tk.Text(total_window, height=2, width=20, state="disabled")
    cash_box.pack()
    #adds in numbers to select cash amount
    num_btn = tk.Frame(total_window, padx=10)
    tk.Button(num_btn, text="1", command=lambda: on_float_click("1")).grid(column=0, row=0)
    tk.Button(num_btn, text="2", command=lambda: on_float_click("2")).grid(column=1, row=0)
    tk.Button(num_btn, text="3", command=lambda: on_float_click("3")).grid(column=2, row=0)
    tk.Button(num_btn, text="4", command=lambda: on_float_click("4")).grid(column=3, row=0)
    tk.Button(num_btn, text="5", command=lambda: on_float_click("5")).grid(column=4, row=0)
    tk.Button(num_btn, text="6", command=lambda: on_float_click("6")).grid(column=5, row=0)
    tk.Button(num_btn, text="7", command=lambda: on_float_click("7")).grid(column=6, row=0)
    tk.Button(num_btn, text="8", command=lambda: on_float_click("8")).grid(column=7, row=0)
    tk.Button(num_btn, text="9", command=lambda: on_float_click("9")).grid(column=8, row=0)
    tk.Button(num_btn, text="0", command=lambda: on_float_click("0")).grid(column=9, row=0)
    tk.Button(num_btn, text="reset", command=lambda: on_float_click("reset")).grid(column=10, row=0)
    tk.Button(num_btn, text="cash out", command=lambda: on_cashout_click("enter")).grid(column=11, row=0)
    tk.Button(num_btn, text="Cardless", command=lambda: on_card_click("enter")).grid(column=12, row=0)
    num_btn.pack()
    
    def check_drawer_change(cash):
        nomoreredlines = 1 + 1
        if cash_in_till > 1000:
            drawer_change_window = tk.Toplevel()
            drawer_change_window.title("Drawer Change")
            drawer_change_window.geometry("800x600")
            frame = tk.Frame(drawer_change_window)

            drawer_change_box = tk.Text(frame, width=20) 
            drawer_change_box.pack()
            drawer_change_box.config(state="normal")
            drawer_change_box.insert(tk.END, "This till has more than the allowed amount in it. Please contact a manager\n")
            frame.pack(side="left", fill="y")
            cash_box.delete("1.0", tk.END)
            btb_exit = tk.Button(drawer_change_window, text="Exit", command=drawer_change_window.destroy)
        #this function is for getting the cash amount from the customer.
    def on_float_click(value):
        global cash_tendered
        #enables the cash box so it can be edited and then disables it after it writes to it
        cash_box.config(state="normal")
        cash_box.insert(tk.END, cash_tendered)
        cash_box.config(state="disabled")
        if value == "reset":
            cash_tendered = 0.0
            #enables the cash box so it can be edited and then disables it after it writes to it
            cash_box.config(state="normal")
            cash_box.delete("1.0", tk.END)
            cash_box.insert(tk.END, cash_tendered)
            cash_box.config(state="disabled")
        else:
            value = int(value)
            cash_tendered = (cash_tendered * 10) + (value / 100)
            cash_tendered = round(cash_tendered, 2)
            #enables the cash box so it can be edited and then disables it after it writes to it
            cash_box.config(state="normal")
            cash_box.delete("1.0", tk.END)
            cash_box.insert(tk.END, cash_tendered)
            cash_box.config(state="disabled")
        #this function allows for the user to enter the amount of money that the customer gave them and then it calculates the change and pulls up a new window
    def on_cashout_click(value):
            nomoreredlines = 1 + 1
            global cash_in_till
            cash_tendered = float(cash_box.get("1.0", tk.END))
            #gets the last line that contains the total and splits it out of the string
            last_line = total_box.get("end-2l", "end-1l")
            last_line = last_line.split("$")
            last_line = float(last_line[1])
            change = cash_tendered - last_line
            change_window = tk.Toplevel()
            change_window.title("Change")
            change_window.geometry("800x600")
            frame = tk.Frame(change_window)
            #disables the change box 
            change_box = tk.Text(frame, width=20, state="disabled")
            change_box.pack()
            frame.pack(side="left", fill="y")
            #enables the change box so it can be edited and then disables it after it writes to it
            change_box.config(state="normal")
            change_box.insert(tk.END, "Change: ${:.2f}\n".format(change))
            change_box.config(state="disabled")
            #call reciept function here
            print_reciept(cash_tendered, change)
            cash_in_till += cash_tendered - change
            btb_exit = tk.Button(change_window, text="Exit", command=change_window.destroy)
            btb_exit.pack()
            check_drawer_change(cash_in_till)
            on_reset_click()
            #saves cash_in_till and employee name to a /tmp file incase the till crashes or something
            #suppose I should make sure there is a /tmp directory
            if not os.path.exists("tmp"):
                os.mkdir("tmp")

            with open("tmp/cash_in_till", "w") as file:
                file.write(f"{cash_in_till:.2f}:{emp_name}")
                
                file.close()
            total_window.destroy()
#this functions "prints" the reciept and resets the running total and cash tendered
#by print I mean it creates a file and writes the reciept to it
def print_reciept(cash_tendered, change):
    nomore_redlines = 1 + 1
    
    #gets the date and time
    now = datetime.datetime.now()
    today = now.strftime("%m-%d-%Y")
    #looks for and creates directories for the year/month/day
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    if not os.path.exists(year):
        os.mkdir(year)
    if not os.path.exists(year + "/" + month):
        os.mkdir(year + "/" + month)
    if not os.path.exists(year + "/" + month + "/" + day):
        os.mkdir(year + "/" + month + "/" + day)
    path_to_file = year + "/" + month + "/" + day
    #creates a file name based on the time
    current_time = now.strftime("%H-%M-%S")
    file_name = path_to_file + "/" + current_time + ".txt"
    #creates a file and writes the reciept to it
    with open(file_name, "w") as file:
        file.write("Reciept\n")
        file.write("Date: " + today + "\n")
        file.write("Time: " + now.strftime("%H:%M:%S") + "\n")
        file.write(running_total_box.get("1.0", tk.END))
        file.write(total_box.get("1.0", tk.END))
        file.write("\n")
        file.write("Cash Tendered: ${:.2f}\n".format(cash_tendered))
        file.write("Change: ${:.2f}\n".format(change))
        file.write("\n")
        file.write(f"You were served by {emp_name}\n")
        file.write("Have a nice day!")
        file.close()
    #resets the cash tendered and the running total
    running_total = 0.0
    cash_tendered = 0.0

    #lbl_emp_name.config(text=current_time)
# gets the quantiy using the number buttons used a couple of different places so its not just for the quanity box but now that 
#i think about it I think that this could be the only place that it is used since for the other things I had to modify it to work 
def on_number_click(value, output_box):
    quantity_str = output_box.get("1.0", tk.END).strip()
    if quantity_str == "":
        quantity = 0
    else:
        quantity = int(quantity_str)
    
    if value == "reset":
        quantity = 0
    else:
        quantity = quantity * 10 + int(value)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, quantity)


#controls for if the running order is over 100 dollars or over 15 items
def seek_approval(quantity, running_total):
    global approval
    approval = False
    
    if running_total > 100 or quantity > 15:
        excess_window = tk.Toplevel()
        excess_window.title("Excess")
        excess_window.geometry("800x600")
        frame = tk.Frame(excess_window)
        excess_box = tk.Text(frame, width=20)
        excess_box.pack()
        frame.pack()
        excess_box.insert(tk.END, "this order is over 100 dollars or has too many items get approval")
        #gives 20 seconds for the manager to enter their password
        on_manager_click()
        tk.Button(excess_window, text="acknowledge", command=lambda: (excess_window.destroy())).pack()
        while excess_window.winfo_exists():
            excess_window.update()

        return 1
        
        
    else:
        approval = True

    
#this function gets the selected menu item and quantity and adds it to the running total box
def on_menu_click(text, price):
    no_more_red_lines = 1 + 1   
    global running_total
    global approval
    quantity = int(quantity_box.get("1.0", tk.END))
    total = float(price) * int(quantity)
    running_total += float(total)
    seek_approval(quantity, running_total)
    if approval == True:
        outline = f"{quantity} {text} ${total:.2f}\n"
        running_total_box.insert(tk.END, outline)
        quantity_box.delete("1.0", tk.END)
        quantity_box.insert(tk.END, "1")
        total_box.delete("1.0", tk.END)
        tax_total = running_total * .075
        final_total = running_total + tax_total
        #disables the total box so it can be edited and then disables it after it writes to it
        total_box.config(state="normal")
        total_box.delete("1.0", tk.END)
        total_box.insert(tk.END, "Total: ${:.2f}\n".format(running_total))
        total_box.insert(tk.END, "Tax: ${:.2f}\n".format(tax_total))
        total_box.insert(tk.END, "Final Total: ${:.2f}\n".format(final_total))
        total_box.config(state="disabled")
        approval = False
    else:
        total_box.config(state="normal")
        total_box.insert(tk.END, "it didn't work dummy")
        total_box.config(state="disabled")

#this function is for adding a new user to the system
def add_user():
    nomore_redlines = 1 + 1
    employee_enter_window = tk.Toplevel()
    employee_enter_window.title("Employee")
    employee_enter_window.geometry("800x600")
    frame = tk.Frame(employee_enter_window)
    employee_enter_box = tk.Text(frame, width=20)
    employee_enter_box.pack()
    frame.pack()
    btn_name = tk.Frame(employee_enter_window, padx=10)
    #makes a virtual keyboard for the user to enter their name
    tk.Button(btn_name, text="q", command=lambda: on_letter_click("q")).grid(column=0, row=0) 
    tk.Button(btn_name, text="w", command=lambda: on_letter_click("w")).grid(column=1, row=0)
    tk.Button(btn_name, text="e", command=lambda: on_letter_click("e")).grid(column=2, row=0)
    tk.Button(btn_name, text="r", command=lambda: on_letter_click("r")).grid(column=3, row=0)
    tk.Button(btn_name, text="t", command=lambda: on_letter_click("t")).grid(column=4, row=0)
    tk.Button(btn_name, text="y", command=lambda: on_letter_click("y")).grid(column=5, row=0)
    tk.Button(btn_name, text="u", command=lambda: on_letter_click("u")).grid(column=6, row=0)
    tk.Button(btn_name, text="i", command=lambda: on_letter_click("i")).grid(column=7, row=0)
    tk.Button(btn_name, text="o", command=lambda: on_letter_click("o")).grid(column=8, row=0)
    tk.Button(btn_name, text="p", command=lambda: on_letter_click("p")).grid(column=9, row=0)
    tk.Button(btn_name, text="a", command=lambda: on_letter_click("a")).grid(column=0, row=1)
    tk.Button(btn_name, text="s", command=lambda: on_letter_click("s")).grid(column=1, row=1)
    tk.Button(btn_name, text="d", command=lambda: on_letter_click("d")).grid(column=2, row=1)
    tk.Button(btn_name, text="f", command=lambda: on_letter_click("f")).grid(column=3, row=1)
    tk.Button(btn_name, text="g", command=lambda: on_letter_click("g")).grid(column=4, row=1)
    tk.Button(btn_name, text="h", command=lambda: on_letter_click("h")).grid(column=5, row=1)
    tk.Button(btn_name, text="j", command=lambda: on_letter_click("j")).grid(column=6, row=1)
    tk.Button(btn_name, text="k", command=lambda: on_letter_click("k")).grid(column=7, row=1)
    tk.Button(btn_name, text="l", command=lambda: on_letter_click("l")).grid(column=8, row=1)
    tk.Button(btn_name, text="z", command=lambda: on_letter_click("z")).grid(column=1, row=2)
    tk.Button(btn_name, text="x", command=lambda: on_letter_click("x")).grid(column=2, row=2)
    tk.Button(btn_name, text="c", command=lambda: on_letter_click("c")).grid(column=3, row=2)
    tk.Button(btn_name, text="v", command=lambda: on_letter_click("v")).grid(column=4, row=2)
    tk.Button(btn_name, text="b", command=lambda: on_letter_click("b")).grid(column=5, row=2)
    tk.Button(btn_name, text="n", command=lambda: on_letter_click("n")).grid(column=6, row=2)
    tk.Button(btn_name, text="m", command=lambda: on_letter_click("m")).grid(column=7, row=2)
    tk.Button(btn_name, text=" ", command=lambda: on_letter_click(" ")).grid(column=8, row=2)
    tk.Button(btn_name, text="backspace", command=lambda: on_letter_click("backspace")).grid(column=9, row=2)
    tk.Button(btn_name, text="Enter", command=lambda: (on_enter_click(), employee_enter_window.destroy())).grid(column=10, row=2)
    btn_name.pack()
    def on_letter_click(value):
        nomore_redlines = 1 + 1
        global employee_name
        if value == "backspace":
            employee_enter_box.delete("end-2c", tk.END)
            employee_name = ""
        else:
            employee_name += value
            employee_enter_box.delete("1.0", tk.END)
            employee_enter_box.insert(tk.END, employee_name)
    def on_enter_click():
        nomore_redlines = 1 + 1
        global employee_name
        #opens the passwd file and enters the employee name
        counter = 1
        with open("passwd", "r") as file:
            for line in file:
            #gets the index of the last line 
                if line:
                    counter += 1
            file.close()
        with open("passwd", "a") as file:
            file.write(f"{counter}:{employee_name}\n")
            file.close()
        employee_name = ""
#this functions adds a new manager to the system
def add_manager():
    manager_id_window = tk.Toplevel()
    manager_id_window.title("Manager")
    manager_id_window.geometry("800x600")
    frame = tk.Frame(manager_id_window)
    manager_box = tk.Text(frame, height=2, width=20)
    manager_box.pack()
    frame.pack()
    #buttons for the manager id
    mgmt_btn = tk.Frame(manager_id_window, padx=10)
    tk.Button(mgmt_btn, text="1", command=lambda: on_id_click("1")).grid(column=0, row=0)
    tk.Button(mgmt_btn, text="2", command=lambda: on_id_click("2")).grid(column=1, row=0)
    tk.Button(mgmt_btn, text="3", command=lambda: on_id_click("3")).grid(column=2, row=0)
    tk.Button(mgmt_btn, text="4", command=lambda: on_id_click("4")).grid(column=3, row=0)
    tk.Button(mgmt_btn, text="5", command=lambda: on_id_click("5")).grid(column=4, row=0)
    tk.Button(mgmt_btn, text="6", command=lambda: on_id_click("6")).grid(column=5, row=0)
    tk.Button(mgmt_btn, text="7", command=lambda: on_id_click("7")).grid(column=6, row=0)
    tk.Button(mgmt_btn, text="8", command=lambda: on_id_click("8")).grid(column=7, row=0)
    tk.Button(mgmt_btn, text="9", command=lambda: on_id_click("9")).grid(column=8, row=0)
    tk.Button(mgmt_btn, text="0", command=lambda: on_id_click("0")).grid(column=9, row=0)
    tk.Button(mgmt_btn, text="reset", command=lambda: on_id_click("reset")).grid(column=10, row=0)
    tk.Button(mgmt_btn, text="enter", command=lambda: [pass_stuff(), manager_id_window.destroy()]).grid(column=11, row=0)
    mgmt_btn.pack()

    def on_id_click(value):
        global manager_id
        nomoreredlines = 1 + 1
        if value == "reset":
            manager_id = ""
        else:
            manager_id = manager_id + value
        manager_box.delete("1.0", tk.END)
        manager_box.insert(tk.END, manager_id)
    def pass_stuff():
        manager_pass_window = tk.Toplevel()
        manager_pass_window.title("Manager")
        manager_pass_window.geometry("800x600")
        frame = tk.Frame(manager_pass_window)
        manager_pass_box = tk.Text(frame, height=2, width=20)
        manager_pass_box.pack()
        frame.pack()
        #buttons for the manager password
        mgmt_pass_btn = tk.Frame(manager_pass_window, padx=10)
        tk.Button(mgmt_pass_btn, text="1", command=lambda: on_manager_pass_click("1")).grid(column=0, row=0)
        tk.Button(mgmt_pass_btn, text="2", command=lambda: on_manager_pass_click("2")).grid(column=1, row=0)
        tk.Button(mgmt_pass_btn, text="3", command=lambda: on_manager_pass_click("3")).grid(column=2, row=0)
        tk.Button(mgmt_pass_btn, text="4", command=lambda: on_manager_pass_click("4")).grid(column=3, row=0)
        tk.Button(mgmt_pass_btn, text="5", command=lambda: on_manager_pass_click("5")).grid(column=4, row=0)
        tk.Button(mgmt_pass_btn, text="6", command=lambda: on_manager_pass_click("6")).grid(column=5, row=0)
        tk.Button(mgmt_pass_btn, text="7", command=lambda: on_manager_pass_click("7")).grid(column=6, row=0)
        tk.Button(mgmt_pass_btn, text="8", command=lambda: on_manager_pass_click("8")).grid(column=7, row=0)
        tk.Button(mgmt_pass_btn, text="9", command=lambda: on_manager_pass_click("9")).grid(column=8, row=0)
        tk.Button(mgmt_pass_btn, text="0", command=lambda: on_manager_pass_click("0")).grid(column=9, row=0)
        tk.Button(mgmt_pass_btn, text="reset", command=lambda: on_manager_pass_click("reset")).grid(column=10, row=0)
        tk.Button(mgmt_pass_btn, text="enter", command=lambda: (on_passcheck(), manager_pass_window.destroy())).grid(column=11, row=0)
        mgmt_pass_btn.pack()
        tk.Label(manager_pass_window, text="Manager password enter").pack()


        #this is for getting the manager password
        def on_manager_pass_click(value):
            nomoreredlines = 1 + 1
            global manager_password
            if value == "reset":
                manager_password = ""
            else:
                manager_password = manager_password + value
            manager_pass_box.delete("1.0", tk.END)
            #probably want to change this to a * so that the password is hidden
            manager_pass_box.insert(tk.END, "*" * len(manager_password))

    #this takes the id and hashes the password and then checks it against the shadow file
    def on_passcheck():
        global manager_password
        global manager_id
        hashed_password = hashlib.sha256(manager_password.encode()).hexdigest()
        #opens the shadow file and writes the manager id and hashed password to the last line
        with open("shadow", "a") as f:
            f.write(f"{manager_id}:{hashed_password}\n")
        manager_id = ""
        manager_password = ""

root = tk.Tk()
# Set the size of the main window to be 800x600 pixels
root.geometry("800x600")

# Create a frame to hold the Text widget and the quanity amount and the total amount
frame = tk.Frame(root)
quantity_box = tk.Text(frame, height=5, width=20)
quantity_box.grid(column=0, row=0)
running_total_box = tk.Text(frame, width=20)
running_total_box.grid(column=0, row=1)
#disables the total box so that the user cant type in it 
total_box = tk.Text(frame, width=20 , state="disabled")
total_box.grid(column=0, row=2)
quantity_box.insert(tk.END, "0")
frame.pack(side="left", fill="y")

#creating buttons for the quantity
num_btn = tk.Frame(root, padx=10)
tk.Button(num_btn, text="1", command=lambda: on_number_click("1", quantity_box)).grid(column=0, row=0)
tk.Button(num_btn, text="2", command=lambda: on_number_click("2", quantity_box)).grid(column=1, row=0)
tk.Button(num_btn, text="3", command=lambda: on_number_click("3", quantity_box)).grid(column=2, row=0)
tk.Button(num_btn, text="4", command=lambda: on_number_click("4", quantity_box)).grid(column=3, row=0)
tk.Button(num_btn, text="5", command=lambda: on_number_click("5", quantity_box)).grid(column=4, row=0)
tk.Button(num_btn, text="6", command=lambda: on_number_click("6", quantity_box)).grid(column=5, row=0)
tk.Button(num_btn, text="7", command=lambda: on_number_click("7", quantity_box)).grid(column=6, row=0)
tk.Button(num_btn, text="8", command=lambda: on_number_click("8", quantity_box)).grid(column=7, row=0)
tk.Button(num_btn, text="9", command=lambda: on_number_click("9", quantity_box)).grid(column=8, row=0)
tk.Button(num_btn, text="0", command=lambda: on_number_click("0", quantity_box)).grid(column=9, row=0)
tk.Button(num_btn, text="reset", command=lambda: on_number_click("reset", quantity_box)).grid(column=10, row=0)
num_btn.pack()

# creating menu item buttons Im going to be descriping in detail what I want so that hopefully github copilot can just auto generate some of this for me. I want a small, medium and large size for popcorn, sodas, and candy. 
menu_btn = tk.Frame(root, padx=10)
tk.Button(menu_btn, text="L Popcorn", command=lambda text="L Popcorn", price="10.99": on_menu_click(text, price)).grid(column=0, row=0)
tk.Button(menu_btn, text="M Popcorn", command=lambda text="M Popcorn", price="9.99": on_menu_click(text, price)).grid(column=1, row=0)
tk.Button(menu_btn, text="S Popcorn", command=lambda text="S Popcorn", price="7.99": on_menu_click(text, price)).grid(column=2, row=0)
tk.Button(menu_btn, text="L Soda", command=lambda text="L Soda", price="5.50": on_menu_click(text, price)).grid(column=3, row=0)
tk.Button(menu_btn, text="M Soda", command=lambda text="M Soda", price="4.99": on_menu_click(text, price)).grid(column=4, row=0)
tk.Button(menu_btn, text="S Soda", command=lambda text="S Soda", price="3.99": on_menu_click(text, price)).grid(column=0, row=1)
tk.Button(menu_btn, text="L Candy", command=lambda text="L Candy", price="5.50": on_menu_click(text, price)).grid(column=1, row=1)
tk.Button(menu_btn, text="M Candy", command=lambda text="M Candy", price="4.99": on_menu_click(text, price)).grid(column=2, row=1)
tk.Button(menu_btn, text="S Candy", command=lambda text="S Candy", price="3.99": on_menu_click(text, price)).grid(column=3, row=1)
tk.Button(menu_btn, text="L Combo", command=lambda text="L Combo", price="14.99": on_menu_click(text, price)).grid(column=4, row=1)
tk.Button(menu_btn, text="M Combo", command=lambda text="M Combo", price="12.99": on_menu_click(text, price)).grid(column=0, row=2)
tk.Button(menu_btn, text="S Combo", command=lambda text="S Combo", price="10.99": on_menu_click(text, price)).grid(column=1, row=2)
tk.Button(menu_btn, text="Chislic", command=lambda text="Chislic", price="12.99": on_menu_click(text, price)).grid(column=2, row=2)
tk.Button(menu_btn, text="shake", command=lambda text="shake", price="7.99": on_menu_click(text, price)).grid(column=3, row=2)
tk.Button(menu_btn, text="family pack", command=lambda text="family pack", price="50.00": on_menu_click(text, price)).grid(column=4, row=2)
menu_btn.pack() 

#adds in the reset button for the entire order as well as a total button
order_btn = tk.Frame(root, padx=10)
tk.Button(order_btn, text="Reset", command=lambda: on_reset_click()).grid(column=0, row=0)
tk.Button(order_btn, text="Total", command=lambda: on_total_click()).grid(column=1, row=0)
order_btn.pack()
manager_btn = tk.Frame(root, padx=10)
tk.Button(manager_btn, text="Manager", command=lambda: on_manager_click()).grid(column=0, row=0)
manager_btn.pack()
lbl_emp_name = tk.Label(root, text=f"This till is in {emp_name}'s name")
lbl_emp_name.pack()
root.mainloop()

