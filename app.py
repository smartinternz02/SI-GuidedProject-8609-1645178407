import numpy as np #used for numerical analysis
from flask import Flask,render_template,request #Flask is a application used to run/serve our aplication
# request is used to access the file which is uploaded by the user in our application
#render_template is used for rendering the html pages
from tensorflow.keras.models import load_model #we are loading our model from keras
import pickle


app = Flask(__name__) #our flask app
#scaler=pickle.load(open("Scaler_forecast.pkl","rb"))
model = load_model('forcast_sales.h5') #loading the model in the flask app


@app.route('/') #rendering html template
def home():
    return render_template("home.html") #rendering html template
@app.route('/intro')
def home1():
    return render_template("intro.html") #rendering html template
@app.route('/predict')
def home2():
    return render_template("web.html") #rendering html template

@app.route('/login',methods = ['POST']) #route for our prediction
def login():
    i = str(request.form['year'])
    a = [[float(c) for c in i.split(',')]]
    print(i)
    print(a)
    output = model.predict(a)

    
    return render_template("web.html",showcase = 'The next day predicted value is:'+str(output))
    #return str(x)
    
if __name__ == '__main__' :
    app.run(debug = False,port=5000)

"""x_input = str(request.form['year'])  # requesting the file
x_input = x_input.split(',')
print(x_input)
for i in range(0, len(x_input)):
    x_input[i] = float(x_input[i])
print(x_input)
x_input = np.array(x_input).reshape(1, -1)
temp_input = list(x_input)
temp_input = temp_input[0].tolist()
lst_output = []
n_steps = 10
i = 0
while (i < 10):

    if (len(temp_input) >= 10):
        # print("temp_input",temp_input)
        x_input = np.array(temp_input[0:])
        print("{} day input {}".format(i, x_input))
        x_input = np.expand_dims(x_input, axis=0)
        x_input = scaler.transform(x_input)
        # x_input=x_input.reshape(1,-1)
        x_input = x_input.reshape((1, n_steps, 1))
        # print("x_input.....",x_input)
        yhat = model.predict(x_input, verbose=0)

        yhat = scaler.inverse_transform(yhat)
        print("{} day output {}".format(i, yhat))
        temp_input.extend(yhat[0].tolist())
        temp_input = temp_input[1:]
        # print(temp_input)
        lst_output.extend(yhat.tolist())
        i = i + 1
    else:
        print("Please give 10 number of inputs")"""