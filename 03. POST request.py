from flask import Flask, request, jsonify

app = Flask(__name__)

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

@app.route('/users/<string:userId>/tags',methods=['POST'])
def addValues(userId):
    flag = 0
    for ids in userData:
        if userData[ids]['id'] == userId:
            flag = 1
    if flag == 0:
        return jsonify({'Status' : 'ID Not found'}), 404
    
    temp = {
        'tags' : request.json['tags'],
        'expiry' : request.json['expiry']
    }
    userData[userId].update(temp)
    return jsonify({'Status' : 'OK'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=8080)