from flask import Flask, render_template, request, jsonify, session
import secrets
from demo_code_decision_tree import predict_flag

secret_key=secrets.token_hex(32)
app = Flask(__name__)
app.secret_key = secret_key

@app.route('/')
def index():
    return render_template('adding_values_to_predict_with.html')

@app.route('/json_to_predict_with', methods=["POST"])
def json_post():
    if request.method== 'POST':
        json = request.get_json() 
        data_to_predict = [value for key, value in json.items()]
        print(data_to_predict)
        prediction = predict_flag(data_to_predict)
        session['predicted_flag'] = prediction[0]
        return jsonify({'predict': prediction[0]}), 200
    return jsonify({'error':'invalid request method'}), 405

@app.route('/predict', methods=["GET"])
def predict():
    if request.method=="GET":
        predicted_coutry = session['predicted_flag']
        print(predicted_coutry)
        return render_template('predicted_flag_page.html', prediction = predicted_coutry )

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)
#type:ignore