from flask import Flask, request, jsonify

app = Flask(__name__)

userData = {}
userData['01'] = {
    "id" : "01",
    "fullName" : "User 1"
}
userData['02'] = {
    "id" : "02",
    "fullName" : "User 2"
}

@app.route('/users/<string:userId>',methods=['GET'])
def findId(userId):
    for ids in userData:
        if userData[ids]['id'] == userId:
            return jsonify(userData[ids]), 200
    return jsonify({'Status' : 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8080)