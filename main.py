
from flask import Flask, request, redirect, url_for, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    # Set the time limit for placing a bid to 30 seconds.
    time_limit = 30
    return render_template('index.html', time_limit=time_limit)

@app.route('/bid', methods=['POST'])
def bid():
    # Get the bid amount and time remaining from the request.
    bid_amount = request.form.get('bid_amount')
    time_remaining = request.form.get('time_remaining')
    
    # Check if the bid is valid (within the time limit and amount is greater than zero).
    if time_remaining > 0 and float(bid_amount) > 0:
        # Save the bid information (for this example, we are using a simple in-memory dictionary).
        bids = {'bid_amount': bid_amount, 'time_remaining': time_remaining}
        
        # Redirect to the success page.
        return redirect(url_for('success'))
    else:
        # Redirect to the failure page.
        return redirect(url_for('failure'))

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/failure')
def failure():
    return render_template('failure.html')

if __name__ == "__main__":
    app.run(debug=True)
