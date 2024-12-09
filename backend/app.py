from flask import Flask, request, jsonify, render_template, redirect, url_for
from chains.custom_chains import build_custom_chain
from flask_cors import CORS
import re
import json
import secrets
import time  # Simulate processing time for demonstration

app = Flask(__name__)
CORS(app)

# Global variable to hold results
results_storage = {"distinct_json_objects": []}


# Function to extract distinct JSON objects
def extract_json(data):
    if isinstance(data, list):
        data = " ".join(map(str, data))  # Convert list elements to strings and join them
    elif not isinstance(data, str):
        raise ValueError(f"Expected data to be a string or list, got: {type(data).__name__}")

    json_objects = re.findall(r'```json(.*?)```', data, re.DOTALL)
    parsed_json_objects = []
    seen = set()

    for json_obj in json_objects:
        try:
            json_obj = bytes(json_obj, "utf-8").decode("unicode_escape").strip()
            parsed_json = json.loads(json_obj)
            json_str = json.dumps(parsed_json, sort_keys=True)

            if json_str not in seen:
                seen.add(json_str)
                parsed_json_objects.append(parsed_json)
        except json.JSONDecodeError:
            continue

    return parsed_json_objects


@app.route("/analyze", methods=["POST"])
def analyze():
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "URL is required"}), 400

    # Clear previous results at the start of a new request
    global results_storage
    results_storage["distinct_json_objects"] = []

    chain = build_custom_chain()

    try:
        print("Processing URL:", url)  # Debug: Print URL
        results = chain.invoke({"input": url})
        data = results["intermediate_steps"]

        # Simulate processing time
        time.sleep(5)

        # Extract and save distinct JSON objects
        results_storage["distinct_json_objects"] = extract_json(data)

        return jsonify({"message": "Processing complete, results are available."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/results", methods=["GET"])
def results():
    return render_template("results.html", results=results_storage)


@app.route("/")
def index():
    return redirect(url_for("results"))


@app.route("/status", methods=["GET"])
def status():
    """
    Endpoint to fetch the current processing status.
    """
    global results_storage
    if results_storage["distinct_json_objects"]:
        return jsonify({"status": "complete", "results": results_storage["distinct_json_objects"]}), 200
    else:
        return jsonify({"status": "processing"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


