import os

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"status": "ok"})

@app.route("/api/pathfind")
def pathfind():
    ax = float(request.args.get("ax", 0))
    az = float(request.args.get("az", 0))
    bx = float(request.args.get("bx", 1))
    bz = float(request.args.get("bz", 1))

    path = [
        [ax, az],
        [(ax + bx) / 2, (az + bz) / 2],
        [bx, bz]
    ]

    return jsonify({
        "path": path,
        "length": ((bx-ax)**2 + (bz-az)**2) ** 0.5
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)