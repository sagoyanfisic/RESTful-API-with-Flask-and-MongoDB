from flask import Flask,request,jsonify,g
import sqlite3

app = Flask(__name__)

def getDatabase():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('userData.db')
    return db

userData = {} # Dictionary
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

@app.route('/users', methods=['POST'])
def addOne():
    cur = getDatabase().cursor()

    cur.execute('''SELECT * FROM users''')
    data = cur.fetchall()

    userData = {}
    for row in data:
        userData[row[0]] = {
            "id" : row[0],
            "fullName" : row[1],
            "firstName" : row[2],
            "lastName" : row[3],
            "password" : row[4],
            "tags" : row[5],
            "expiry" : row[6]
        }
    return jsonify({"Users": userData})

    # dict((y, x) for x, y in tuple)



    # userData = {}
    # for i in data:

    size = len(userData) + 1
    userId = str(size)
    userData[userId] = {
        "id" : userId,
        "firstName" : request.json['firstName'],
        "lastName" : request.json['lastName'],
        "password" : request.json['password']
    }

    # cur.close()

    if "" == request.json['firstName'] or "" == request.json['lastName'] or "" == request.json['password']:
        return jsonify({"Status" : "Not Acceptable"}), 406
    return jsonify({"id" : userData[userId]['id']}), 201

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(debug=True, port=8080)
