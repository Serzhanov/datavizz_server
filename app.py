from flask import Flask
import pandas as pd
from flask import request
from flask_cors import CORS
from script import cleanUpDataframe 
import json


app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/')
def hello():
    return 'Hello, Flask!'



@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(file)
    df=cleanUpDataframe(df)
    # Perform any desired operations on the DataFrame
    # ...
    
    # Convert DataFrame to JSON object
    json_data = df.to_json(orient='records')#gives me a string

    json_object = json.loads(json_data)

    # Return the JSON response
    return json_object


if __name__ == '__main__':
    app.run()