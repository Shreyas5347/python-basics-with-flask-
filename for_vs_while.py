'''for loop vs while loop -
for loop-You know how many times you want to loop
while loop-You don’t know how many times — depends on a condition

Use for when:
•	Looping a fixed number of times
•	Looping through a list, string, or range
Eg- for i in range(3):
    print("Hello")

Use while when:
•	Loop continues until something happens
•	You don’t know how many iterations in advance 
'''

#Eg- guessing word example 
secret="giraffe"
guess=""
count=3
while guess!=secret and (count>0 and count<=3):
    
    guess=input("enter your guess: ")
    count-=1
if guess==secret:
   print("your guess is correct") 
else:
    print("u lost")

