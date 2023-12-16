from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/h1", methods=["GET"])
def fn_h1():
    return jsonify({
        "payload":"get"
    })

@app.route("/h2", methods=["POST"])
def fn_h2():
    return jsonify({
        "payload":"post"
    })

@app.route("/h3", methods=["PUT"])
def fn_h3():
    return jsonify({
        "payload":"PUT"
    })

@app.route("/h4", methods=["DELETE"])
def fn_h4():
    return jsonify({
        "payload":"delete"
    })

@app.route("/h5", methods=["GET","POST","PUT","DELETE"])
def fn_h5():

    if request.method == "GET":
        return jsonify({
            "payload": "success", "error": False
        })

    else:
        return jsonify({})

@app.route("/h6", methods=["GET","POST","PUT","DELETE"])
def fn_h6():

    if request.method == "GET":
        return jsonify({
            "method":"GET", "payload":"success", "error":False
        })
    
    if request.method == "POST":
        return jsonify({
            "method":"POST", "payload":"success", "error":False
        })
    
    if request.method == "DELETE":
        return jsonify({
            "method":"DELETE", "payload":"success", "error":False
        })

    else:
        return jsonify({})
    
@app.route("/h7", methods=["GET"])
def fn_h7():

    email = request.args.get("correo")
    name = request.args.get("nombre")

    return jsonify({
        "payload":{"email":email, "name":name},
            "error":{"available":False,"err_msg":None},
            "status":200
    })

@app.route("/h8", methods=["POST"])
def fn_h8():

    data = request.get_json()  
    email = data.get('email')
    name = data.get('name')
    
    return jsonify({
        "payload":{"email":email, "name":name},
        "error": {"available": False, "err_msg": None},
        "status": 200
    })

@app.route("/h9", methods=["GET"])
def fn_h9():

    list = ["foo","bar","baz","qux","fred"]
    alias = request.args.get("alias")

    if alias in list:
        return {"payload":alias,
            "error":{"available":False,"err_msg":None},
            "status":200}
    else:
        return {"payload":"not found",
                "error":{"available":False,"err_msg":None},
                "status":404}
    
@app.route("/h10", methods=["POST"])
def fn_h10():
    
    data = request.get_json()
    alias = data.get("alias")
    list = ["foo","bar","baz","qux","fred"]

    if alias in list:
        return jsonify({"payload":alias})
    else:
        return jsonify({"payload":"not found"})


if __name__ == '__main__':
    app.run(debug=True)