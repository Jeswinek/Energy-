from firebase import firebase 

firebase = firebase.FirebaseApplication("https://energy-meter-project-c13ac.firebaseio.com/",None)
data = { 'Name': 'John Doe','RollNo': 3,'Percentage':70.02 }
result = firebase.post('/energy-meter-project-c13ac/students/',data)
print(result)

