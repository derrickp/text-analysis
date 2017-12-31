import time
from textanalysis import process

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

@app.route("/text", methods=["POST"])
@cross_origin()
def post_text():
    request_json = request.get_json(force=True)
    start_time = time.time()
    output = process.process_text(request_json["text"])
    end_time = time.time()
    total = end_time - start_time
    output["totalTime"] = "Total time (s): " + str(total)
    return jsonify(output)

# Uncomment below if wanting to run flask from just "python app.py"
# if __name__ == "__main__":
#     print("starting flask server")
#     app.run()
