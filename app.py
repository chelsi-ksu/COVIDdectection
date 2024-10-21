from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory data storage (no database)
data_storage = []

# Route to serve the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Route to submit data and give recommendation
@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()

    # Add submitted data to in-memory storage
    data_storage.append(data)

    # Logic to determine the recommendation based on symptoms
    recommendation = ""
    if data['temperature'] >= 100.4 and data['oxygen_level'] <= 92:
        recommendation = "High temperature and low oxygen level detected. Please call 911 immediately or go to the nearest hospital."
    elif data['temperature'] >= 100.4:
        recommendation = "You have a high temperature. Please rest, stay hydrated, and monitor your symptoms closely. If you feel worse, consult your doctor or seek medical help."
    elif data['oxygen_level'] <= 92:
        recommendation = "Your oxygen level is dangerously low. Please call 911 or go to the nearest hospital."
    elif data['cough'] == "Yes" or data['breathlessness'] == "Yes" or data['loss_of_taste_smell'] == "Yes":
        recommendation = "You are experiencing COVID-related symptoms. Self-isolate and monitor your symptoms. Contact a doctor if they worsen."
    else:
        recommendation = "You are not showing severe symptoms at this time. Please continue to monitor your health and contact your doctor if needed."

    return jsonify({"message": "Data submitted successfully", "data": data, "recommendation": recommendation}), 201

# Route to view submitted data in a table
@app.route('/view_data', methods=['GET'])
def view_data():
    return render_template('view_data.html', data_storage=data_storage)

if __name__ == '__main__':
    app.run(debug=True)
