from flask import Flask, request, jsonify
import re

app = Flask(__name__)

userData = {}
userData['1'] = {
    "id" : "1",
    "name" : "User 1",
    "tags": [
        "html",
        "body",
        "head"
    ]
}
userData['2'] = {
    "id" : "2",
    "name" : "User 2",
    "tags": [
        "html",
        "body"
    ]
}
userData['3'] = {
    "id" : "3",
    "name" : "User 3",
    "tags": [
        "html",
        "body"
    ]
}

@app.route('/users', methods=['GET'])
def findUsers():
    if 'tags' in request.args:
        tags = request.args.get('tags', default=None, type=str)
        tagList = re.sub("[^\w]", " ", tags).split()

        users = {}
        for i in userData:
            if set(userData[i]['tags']) == set(tagList):
                users[userData[i]['id']] = {
                    "id" : userData[i]['id'],
                    "name" : userData[i]['name'],
                    "tags": userData[i]['tags']
                }

        return jsonify({"Users" : users}),200
    else:
        return jsonify({"Status" : "Field not found"}),404

if __name__ == '__main__':
    app.run(debug=True,port=8080)