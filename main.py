
import pyrebase
from datetime import date

today = date.today()

config = {
      'apiKey': "AIzaSyA8ppa2_8a6Bt0eQSzOnBocDb_tBXWPP3U",
      'authDomain': "project-379be.firebaseapp.com",
      'databaseURL': "https://project-379be-default-rtdb.europe-west1.firebasedatabase.app",
      'projectId': "project-379be",
      'storageBucket': "project-379be.appspot.com",
      'messagingSenderId': "517107064834",
      'appId': "1:517107064834:web:02bc809366266ffec6871b",
      'measurementId': "G-F3EY8LMYB0"
}

firebase = pyrebase.initialize_app(config)


firebase=pyrebase.initialize_app(config)
storage=firebase.storage()

filename="test.txt"
cloudfilename="Days/"+str(today)+'.txt'

storage.child(cloudfilename).put(filename)

