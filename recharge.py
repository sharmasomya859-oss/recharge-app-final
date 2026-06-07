from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recharge', methods=['POST'])
def recharge():
    name=request.form.get('name')
    number=request.form.get('number')
    amount=request.form.get('amount')
    operator=request.form.get('operator')
    message=f'Recharge successful for {name} ({number}) with ₹{amount} on {operator}'
    return render_template('success.html', message=message)
