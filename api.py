from flask import Flask, request, jsonify, g
import sqlite3, re

app = Flask(__name__)

def getDatabase():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('userData.db')
    return db

@app.route('/users', methods=['POST', 'GET'])
def addOneOrShowAll():
    if request.method == 'POST':
        cur = getDatabase().cursor()
        cur.execute('''SELECT * FROM users''')
        data = cur.fetchall()

        size = len(data) + 1
        userId = str(size)
        firstName = request.json['firstName']
        lastName = request.json['lastName']
        fullName = firstName + ' ' + lastName
        password = request.json['password']
        tags = ''
        expiry = userId+'ms'

        cur.execute('''INSERT INTO users(userId, fullName, firstName, lastName, password, tags, expiry) 
        VALUES(?, ?, ?, ?, ?, ?, ?)''', (userId, fullName, firstName, lastName, password, tags, expiry))
        getDatabase().commit()
        cur.close()

        if "" == firstName or "" == lastName or "" == password:
            return jsonify({"Status" : "Not Acceptable"}), 406
        return jsonify({"id" : userId}), 201

    elif request.method == 'GET':
        cur = getDatabase().cursor()
        cur.execute('''SELECT * FROM users''')
        data = cur.fetchall()

        userData = {}
        for row in data:
            userTags = re.sub("[^\w]", " ", row[5]).split()
            userData[row[0]] = {
                "id" : row[0],
                "full name" : row[1],
                "first name" : row[2],
                "last name" : row[3],
                "password" : row[4],
                "tags" : userTags,
                "expiry" : row[6]
            }

        return jsonify({"users" : userData}), 200

@app.route('/users/<string:userId>', methods=['GET'])
def findId(userId):
    cur = getDatabase().cursor()
    cur.execute('''SELECT * FROM users''')
    data = cur.fetchall()
    
    userData = {}
    for row in data:
        userData[row[0]] = {
            "id" : row[0],
            "fullName" : row[1]
        }

    cur.close()
        
    for ids in userData:
        if userData[ids]['id'] == userId:
            return jsonify(userData[ids]), 200
    return jsonify({'Status' : 'Not found'}), 404

@app.route('/users/<string:userId>/tags', methods=['POST'])
def addValues(userId):
    cur = getDatabase().cursor()
    cur.execute('''SELECT * FROM users''')
    data = cur.fetchall()
    
    userData = {}
    for row in data:
        userData[row[0]] = {
            "id" : row[0]
        }
    flag = 0
    for ids in userData:
        if userData[ids]['id'] == userId:
            flag = 1
    if flag == 0:
        return jsonify({'Status' : 'ID Not found'}), 404

    temp = request.json['tags']
    tags = ','.join(temp)
    expiry = request.json['expiry']

    cur.execute('''UPDATE users SET tags = ?, expiry = ? WHERE userId = ?''', (tags, expiry, userId))
    getDatabase().commit()
    cur.close()
    
    return jsonify({}), 200

@app.route('/users', methods=['GET'])
def findUsers():
    if 'tags' in request.args:
        tags = request.args.get('tags', default=None, type=str)
        tagList = re.sub("[^\w]", " ", tags).split()

        cur = getDatabase().cursor()
        cur.execute('''SELECT * FROM users''')
        data = cur.fetchall()

        userData = {}
        for row in data:
            userTags = re.sub("[^\w]", " ", row[5]).split()
            if set(tagList) == set(userTags):
                userData[row[0]] = {
                    "id" : row[0],
                    "name" : row[1],
                    "tags" : userTags
                }

        cur.close()

        if len(userData) == 0:
            return jsonify({"Status" : "No user found"}),404

        return jsonify({"Users" : userData}),200
    else:
        return jsonify({"Status" : "Field not found"}),404

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
