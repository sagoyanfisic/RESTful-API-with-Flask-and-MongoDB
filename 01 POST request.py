from flask import Flask,request,jsonify

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
    return jsonify({"id" : userData[userId]['id']}), 200

if __name__ == '__main__':
    app.run(debug=True, port=8080)