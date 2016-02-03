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
        while True:
                print 'Please Select the operation'
                print 'Select 1. Enter Item'
                print 'Select 2. Delete Item'
                print 'Select 3. Search Item'
                print 'Select 4. Update Item'
                print 'Select 5. Exit'
                num = int(raw_input("Select a number between 1-5: "))

                if num == 1:
                        enterValues()
                elif num == 2:
                        deleteItem()
                elif num == 3:
                        getItem()
                elif num == 4:
                        UpdateItem()
                else :
			print 'Exiting the program...' 
			exit()



def getItem():
	print 'Enter Username/Lastname to search for particular entry'
	getusername = raw_input("Enter the username to get: ")
	getlast_name = raw_input("Enter the lastname to get: ")
	response = table.get_item(
   	 Key={
        	'username': getusername,
		'last_name': getlast_name
    		}
	)
	item = response['Item']
	print(item)
	start()

def UpdateItem():
	r = ''
	print 'I am here and running'
	getusername = raw_input("Enter the username to update: ")
        getlast_name = raw_input("Enter the lastname to update: ")
	getage = int(raw_input("Enter the age that you want to update"))
	table.update_item(
    	Key={
        	'username': getusername,
        	'last_name': getlast_name
    	},
    	UpdateExpression='SET age = :val1',
    	ExpressionAttributeValues={
        ':val1': getage
    		}
	)
	answer = raw_input("Do you want to view this item? Enter Y for yes or N for no: ")
	if answer.upper() == 'Y':
		getItem()
	else:
		start()		


def deleteItem():
	getusername = raw_input("Enter the username to delete: ")
        getlast_name = raw_input("Enter the lastname to delete: ")
	table.delete_item(
   	Key={
        'username': getusername,
        'last_name': getlast_name
    	}
        )
	start()
	
start()
