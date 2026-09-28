import json
student={
    "name":"Chinnu",
    "age":20.
    
}
with open("student1.json","w") as file:
    json.dump(student,file,indent=4)