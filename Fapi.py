from flask import Flask, request, jsonify
import pandas as pd
import joblib

# load  model
model = joblib.load('random_forest_model.pkl')

# feature order
expected_features = [
    'living_size', 'bathrooms', 'total_rooms', 'pool_type', 'quality',
    'state_CA', 'state_NY', 'state_WY', 'prop_Hospitality',
    'prop_Industrial', 'prop_Institutional', 'prop_Residential',
    'prop_Service', 'prop_Special Purpose'
]

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.get_json()

        #convert  dataframe
        if isinstance(input_data, dict):
            df = pd.DataFrame([input_data])
        elif isinstance(input_data, list):
            df = pd.DataFrame(input_data)
        else:
            return jsonify({'error': 'invalid input format'}), 400

        #missing features
        missing = [col for col in expected_features if col not in df.columns]
        if missing:
            return jsonify({'error': f'Missing features: {missing}'}), 400
        
        df = df[expected_features]

        # make the prediction
        predictions = model.predict(df)

        return jsonify({'prediction': predictions.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
