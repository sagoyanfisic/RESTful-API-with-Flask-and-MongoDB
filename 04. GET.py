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
            if userData[i]['tags'] == tagList:
                users.update(userData[i])

        return jsonify({"tags" : users}),200
    else:
        return jsonify({"Status" : "Field not found"}),404

if __name__ == '__main__':
    app.run(debug=True,port=8080)