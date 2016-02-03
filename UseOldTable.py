#!/usr/bin/python
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('users')

print(table.creation_date_time)
def enterValues():
        u1 = raw_input("Enter the username: ")
        u2 = raw_input("Enter the firstname: ")
        u3 = raw_input("Enter the lastname: ")
	u4 = int(raw_input("Enter the lastname: "))
	table.put_item(
   	Item={
        	'username': u1,
        	'first_name': u2,
        	'last_name': u3,
        	'age': u4,
        	'account_type': 'standard_user',
    		}
	)


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
			print 'Exiting the program' 
                        flag = False



start()
