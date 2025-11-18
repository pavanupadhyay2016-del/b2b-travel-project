from flask import Flask, jsonify, send_from_directory
import json
from flask_cors import CORS # We will need this later

# 1. Create the Flask app
app = Flask(__name__)

# 2. Add CORS support (CRITICAL for connecting frontend to backend)
# This allows your frontend (on a different "port") to get data from your backend.
CORS(app) 

# 3. Define your API "endpoint"
@app.route("/api/packages")
def get_packages():
    # This is the function that runs when someone visits "/api/packages"
    
    # Open and read the database.json file
    with open('database.json', 'r') as f:
        data = json.load(f)
    
    # Return the data as a JSON response
    return jsonify(data)

# 4. This runs the app
if __name__ == "__main__":
    # We set debug=True so the server reloads automatically when you save
    app.run(debug=True, port=5000)