from flask import Flask,request,jsonify,g
import sqlite3

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

conn = sqlite3.connect('users.db')
c = conn.cursor()

userData = {}
userData['1'] = {
    "id" : "1",
    "firstName" : "User",
    "lastName" : "1",
    "password" : "11"
}
userData['2'] = {
    "id" : "2",
    "firstName" : "User",
    "lastName" : "2",
    "password" : "22"
}

print(type(userData))

@app.route('/users', methods=['POST'])
def addOne():
    size = len(userData) + 1
    userId = str(size)
    userData[userId] = {
        "id" : userId,
        "firstName" : request.json['firstName'],
        "lastName" : request.json['lastName'],
        "password" : request.json['password']
    }

    if "" == request.json['firstName'] or "" == request.json['lastName'] or "" == request.json['password']:
        return jsonify({"Status" : "Not Acceptable"}), 406
    return jsonify({"id" : userData[userId]['id']}), 201

c.close()
conn.close()

if __name__ == '__main__':
    app.run(debug=True, port=8080)