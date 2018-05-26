from flask import Flask, request, jsonify
import re
from data.users import users
from data.config import connect_db

app = Flask(__name__)

connect_db()

@app.route('/users', methods = ['POST'])
def addOne():
    data = users()
    data.userId = users.objects().count() + 1
    data.firstName = request.json['firstName']
    data.lastName = request.json['lastName']
    data.fullName = data.firstName + " " + data.lastName
    data.password = request.json['password']
    data.save()

    if "" == data.firstName or "" == data.lastName or "" == data.password:
        return jsonify({"Status": "Not Acceptable"}), 406
    return jsonify({"id": data.userId}), 201

@app.route('/users/<int:userId>', methods = ['GET'])
def findId(userId):
    data = users.objects(userId = userId)

    if data:
        return jsonify({'id': data[0].userId, 'name': data[0].fullName}), 200
    return jsonify({'Status': 'Not found'}), 404

@app.route('/users/<int:userId>/tags', methods = ['POST'])
def addValues(userId):
    data = users.objects(userId = userId)

    if data:
        users.objects(userId = userId).update(push__tags = request.json['tags'])
        users.objects(userId = userId).update(set__expiry = request.json['expiry'])

        return jsonify({'Status': 'Successfully Updated'}), 200
    return jsonify({'Status': 'Not found'}), 404

@app.route('/users', methods = ['GET'])
def findUsers():
    if 'tags' in request.args:
        tags = request.args.get('tags', default = None, type = str)
        tagsList = re.sub("[^\w]", " ", tags).split()

        data = users.objects(tags__all = tagsList)

        userData = []
        for user in data:
            if set(tagsList) == set(user.tags):
                userData.append(
                    {
                        "id": user.userId,
                        "name": user.fullName,
                        "tags": user.tags
                    }
                )

        if len(userData):
            return jsonify({"Users": userData}), 200
        return jsonify({"Status": "No user found"}), 404
    else:
        data = users.objects()

        userData = []
        for user in data:
            userData.append(
                {
                    "id": user.userId,
                    "created": user.created,
                    "full name": user.fullName,
                    "first name": user.firstName,
                    "last name": user.lastName,
                    "password": user.password,
                    "tags": user.tags,
                    "expiry": user.expiry
                }
            )

        return jsonify({"Users": userData}), 200

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 8080)