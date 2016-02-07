#!/usr/bin/python


def enterValues():	
	u1 = raw_input("Enter the username: ")
	u2 = raw_input("Enter the username: ")
	u3 = raw_input("Enter the username: ")
	start()

def start():
 	flag = True
        while flag:
                print 'Please Select the operation'
                print 'Select 1. Enter Item'
                print 'Select 2. Delete Item'
                print 'Select 3. Get Item'
                print 'Select 4. Update Item'
                print 'Select 5. Exit'
		num = int(raw_input("Select a number between 1-5 :"))

                if num == 1:
                        enterValues()
		elif num == 2:	
			print 'Select Item to Delete'
		elif num == 3:
			print 'Get an item'
		elif num == 4:
			print 'Update an Item'
		else : 
			flag = false


print 'The program has finished going through the whole code'
start()
