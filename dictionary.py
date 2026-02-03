'''A dictionary represents a real-world object using named fields.
Key → Value
Name → Data

dict[key] = value means:
“Put this value at this key.
If the key is already there → change its value.
If the key is not there → create it.”
Use dict[key] when:
✔ You are sure the key exists
✔ Missing key should be considered a bug

Use dict.get() when:
✔ Key may or may not exist
✔ You want safe access without crashing


'''
marks = {
    "math": 80,
    "science": 45,
    "english": 60,
    "history": 30
}
update={}
for key,value in marks.items():
    if value>=50:
        update[key]=value+5
        
print(update)



