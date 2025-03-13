from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def index():
    return render_template('Calculator.html')

def loan_payoff(principal, rate, months):
    #loan payoff calculation
    monthly_payment = (principal * rate / 100) / months
    total_payment = monthly_payment * months
    return {"monthly_payment": monthly_payment, "total_payment": total_payment}

def home_affordability(income, debt, interest_rate, years):
    #home affordability calculation
    max_loan = (income - debt) * 3.5 * 12
    return {"max_loan": max_loan}

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    calculation_type = data.get('calculation_type')

    if calculation_type == 'loan_payoff':
        principal = float(data.get('principal'))
        rate = float(data.get('rate'))
        months = int(data.get('months'))
        result = loan_payoff(principal, rate, months)
        return jsonify(result)

    elif calculation_type == 'home_affordability':
        income = float(data.get('income'))
        debt = float(data.get('debt'))
        interest_rate = float(data.get('interest_rate'))
        years = int(data.get('years'))
        result = home_affordability(income, debt, interest_rate, years)
        return jsonify(result)

    return jsonify({"error": "Invalid calculation type"}), 400

if __name__ == '__main__':
    app.run(debug=True)