import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('web-tests-60e15-firebase-adminsdk-hdgfk-58b66a5e39.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://web-tests-60e15-default-rtdb.firebaseio.com"
})

ref = db.reference("/accounts")
ref.push().set(
	{
		"email": "sk@gaaajkkas.com",
        "proxy": "34141315"
	}
)
print(ref.get())