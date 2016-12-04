import pyrebase

config = {
  "apiKey": "AIzaSyAwV9FXEvHaDjTr16yOfcoK14d0GrrGfRQ",
  "authDomain": "dronephone-a53c9.firebaseio.com",
  "databaseURL": "https://dronephone-a53c9.firebaseio.com",
  "storageBucket": "dronephone-a53c9.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()






# printing out an example 

print(db.child("x").get().val())

