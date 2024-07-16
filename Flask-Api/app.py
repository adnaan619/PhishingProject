from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('logistic_regression_model.joblib')

# Selected columns for feature extraction
selected_columns = [
    'qty_slash_directory', 'qty_equal_directory', 'qty_exclamation_directory',
    'qty_at_file', 'qty_and_file', 'qty_dot_file', 'qty_exclamation_file', 'qty_dollar_directory',
    'qty_space_directory', 'qty_plus_file'
]

def extract_features(url):
    # Initialize feature counts
    qty_slash_directory = url.count('/')
    qty_equal_directory = url.count('=')
    qty_exclamation_directory = url.count('!')
    qty_at_file = url.count('@')
    qty_and_file = url.count('&')
    qty_dot_file = url.count('.')
    qty_exclamation_file = url.count('!')
    qty_dollar_directory = url.count('$')
    qty_space_directory = url.count(' ')
    qty_plus_file = url.count('+')
    
    # Return features as a list
    features = [
        qty_slash_directory,
        qty_equal_directory,
        qty_exclamation_directory,
        qty_at_file,
        qty_and_file,
        qty_dot_file,
        qty_exclamation_file,
        qty_dollar_directory,
        qty_space_directory,
        qty_plus_file
    ]
    
    # Ensure features length matches the model's expectation (10 features)
    assert len(features) == 10
    
    return features

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    url = data['url']
    features = extract_features(url)
    prediction = model.predict([features])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(port=5000)
