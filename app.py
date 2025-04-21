from flask import Flask, render_template, request , redirect, url_for , session
import joblib
import numpy as np
import pandas as pd
#import pickle

app = Flask(__name__)
app.secret_key = 'your_secret_key_here' 

 #Load trained model
loaded_pipe = joblib.load('pipeline_LinearRegression.pkl')

USERID = "admin"
PASSWORD = "1234"





@app.route('/', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        user = request.form.get('userid')
        pw = request.form.get('password')
        print(f'User: {user}, Password: {pw}')
        if user == USERID and pw == PASSWORD:
            session['userid'] = user
            print("login successful")
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')


#@app.route('/index', methods=['GET', 'POST'])
#def index():
 #   return render_template("index.html")
   

@app.route('/index' , methods = ['GET', 'POST']) 
def index():
    if 'userid' not in session:
        return redirect(url_for('login'))


    prediction = None
    form_data = {}
    if request.method == 'POST':
        # Get form data
        form_data = {
            'year': request.form.get('year'),
            'make': request.form.get('make'),
            'model': request.form.get('model'),
            'trim': request.form.get('trim'),
            'body': request.form.get('body'),
            'transmission': request.form.get('transmission'),
            'condition': request.form.get('condition'),
            'odometer': request.form.get('odometer'),
            'color': request.form.get('color'),
            'interior': request.form.get('interior'),
            'mmr': request.form.get('mmr'),
            'day': request.form.get('day'),
            'day_name': request.form.get('day_name'),
            'month_name': request.form.get('month_name'),
            'year1': request.form.get('year1')
            }
        
        try:
                    
            year = int(form_data['year'])
            make = form_data['make']
            model= form_data['model']
            trim = form_data['trim']
            body = form_data['body']
            transmission = form_data['transmission']
            condition = int(form_data['condition'])
            odometer = int(form_data['odometer'])
            color = form_data['color']
            interior = form_data['interior']
            mmr = int(form_data['mmr'])
            day = int(form_data['day'])
            day_name = form_data['day_name']
            month_name = form_data['month_name']
            year1 = int(form_data['year1'])

            columns = ['year', 'make', 'model', 'trim', 'body', 'transmission',
                       'condition', 'odometer', 'color', 'interior', 'mmr',
                       'day', 'day_name', 'month_name', 'year1']
            
            input_data = pd.DataFrame([[
                year, make, model, trim, body, transmission, condition,
                odometer, color, interior, mmr, day, day_name, month_name, year1
            ]], columns=columns)

            
            #input = np.array([[year, make , model,trim,body, transmission, condition, odometer, color, interior, mmr, day, day_name, month_name,year1]])
            prediction = loaded_pipe.predict(input_data)[0]
            prediction = round(prediction, 2)
            

        except Exception as e:
             prediction = f"Error: {str(e)}"


            
    return render_template('index.html', prediction=prediction, form_data=form_data)

@app.route('/logout')
def logout():
     session.pop('userid', None)
     return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)




