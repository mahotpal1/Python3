from flask import Flask, render_template, request, jsonify

#object of a flask class. Responsible to handle request and response.
app = Flask(__name__)
#with the help of 'app' object now i can create url/api which will help to reach the program.

#route function is used to create a path for particular function.

#to render homepage get/post whatever is called for.
@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    #render template just returns the page passed inside.
    #note : templates and static name should be proper while creating pages.
    return render_template('index.html')

@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    #checks for the type of request
    if (request.method=='POST'):
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        #request for rendering a templates with passing a value, this will be retrieved 
        #at html side.
        return render_template('results.html',result=result)

@app.route('/via_postman', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    #checks for the type of request
    if (request.method=='POST'):
        operation=request.json['operation']
        #json returns the value for the passed key. Here key is 'operation'.
        num1=int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
    return jsonify(result)
    #jsonify converts the datatype into json format.


if __name__ == '__main__':
    app.run()

#Run app.py and get the ip, which can be used in postman to check the parameteers,
