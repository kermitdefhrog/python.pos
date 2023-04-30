

this is my point of sale system that I wrote in python. it uses the tkinter library for the gui I am pretty sure that this should run on any system that has python 3.6 or newer installed since i dont think it requires any special libraries since i didn't do card stuff
It uses two differnt files for processing employees and managers the passwd file contains employee ids and their names in the format id:name the shadow file contains manager ids and their password in a sha256 hash format the default password for the first manger account is 1 this program does not currenly allow for any credit card transactions since I do not have the ability to test it this program was designed with the idea that it would be used on a touchscreen device this program was designed with the following typical business day in mind.

    manager starts the day off my logging into the till using their manager id and password and then opening the till using an employees ID
    the manager could add a new manager to the system using the employee id
    the cashier would then take orders from customers and add them to the till
    the cashier would accept payment in the form of cold hard cash and not cards
    the manager would have to authorize all purchases over $100 or with more than 10 items
    the manager could at any point be able to view the current amount of cold hard cash in the till
    the manager can close out the till and print out a receipt with the amount of cold hard cash that should be in the till NOTE: this program does not currently have the ability to print out a receipt and instead just saves them to a file the files for order receipts are saved in a file like year/month/day/hour-minute-second.txt the files for till receipts are saved in a file like drawer_totals/year/month/day/employeenamehours-minutes-seconds.txt NOTE: please do not use the exit buttons that are not in the acutal program window as they will make certain screens have extra characters in the output boxes and then that means that have to hit the reset button before you can actually insert the correct information this wont break the program but it is annoying to have to hit the reset button

