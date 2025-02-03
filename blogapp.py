from flask import Flask, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():

    email = "muhiugikonyo@gmail.com"

    current_datetime = datetime.now(pytz.utc).isoformat()
 
    github_url = "https://github.com/Benson-Gikonyo/publicapi"

    # JSON response
    response = {
        "email": email,
        "current_datetime": current_datetime,
        "github_url": github_url
    }

    return jsonify(response)

if __name__ == '__main__':
    # Enable CORS
    from flask_cors import CORS
    CORS(app)

    app.run(debug=True, host='0.0.0.0', port=5000)
