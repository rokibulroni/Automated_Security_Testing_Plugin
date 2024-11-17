
from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)

@app.route('/tamper', methods=['POST'])
def tamper():
    data = request.json
    tampered = {key: value + "_tampered" for key, value in data.items()}
    return jsonify({"original": data, "tampered": tampered})

@app.route('/token/analyze', methods=['POST'])
def analyze_token():
    token = request.json.get("token")
    try:
        decoded = jwt.decode(token, options={"verify_signature": False})
        return jsonify({"decoded": decoded})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
