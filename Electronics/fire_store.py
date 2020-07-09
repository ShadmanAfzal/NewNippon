from firebase import Firebase

config = {
    "apiKey": "AIzaSyDxzZy3OaHHPsw-Nsfoo3Bz7smxspTzxIE",
    "authDomain": "newnippon-16451.firebaseapp.com",
    "databaseURL": "https://newnippon-16451.firebaseio.com",
    "projectId": "newnippon-16451",
    "storageBucket": "newnippon-16451.appspot.com",
    "messagingSenderId": "541019972614",
    "appId": "1:541019972614:web:1579e5c9a6bb7686fb8f87",
    "measurementId": "G-YVE4WKCVDB"
}

def put_get_image_url(name, path):
    firebase = Firebase(config)
    storage = firebase.storage()
    storage.child(f"media/{name}.jpg").put(path)
    url = storage.child(f"media/{name}.jpg").get_url(1)
    return url