'''A list is an ordered collection of related items
we use list when we have multiple items to store in a single variable
example: fruits=["apple","banana","cherry"]
print(fruits[0])
output: apple
also when :
1>Order matters
2>Items are of the same “type”
3>You access data by position
'''
list=[1,2,3,4,5,6,7,8]
output=[]
def even():
    for i in range(len(list)):
        if list[i]%2==0:
            output.append(list[i]**2)
even()   
print(output)
#output - [4, 16, 36, 64]
'''
•	•  List → many similar things
•	•  Dict → one thing with properties
•	In list append() adds only 1 item at a time in the list
•	Extend() adds a complete list to another list not a single item


#list comprehension
list=[1,2,3,4,5,6,7,8]
output=[i**2 for i in list if i%2==0]
print(output)
#output - [4, 16, 36, 64]
'''