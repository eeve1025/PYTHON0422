
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("eeve-66424-firebase-adminsdk-1vfpy-5a3c2d7d6b.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://eeve-66424-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('/mfrc')

ref.update({
    'id': 'Amazing Grace'
})