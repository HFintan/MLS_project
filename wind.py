from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('wind.html')

# Form 
@app.route('/wind', methods = ['POST'])
def wind(sum=sum):
    if request.method == 'POST':
        num1 = request.form['num1']
        operation = request.form['operation']

    #if not isinstance(float(num1), float):
     #   return render_template('app.html',sum="Value must be a float.")
    
    if num1 == '':
        return render_template('wind.html',sum="Please enter a value.")

    if not float(num1) >=0:
        return render_template('wind.html',sum="Wind speed cannot be negative")


    if operation == 'threedegree':
        x = float(num1)
        if x > 24.45:
            return render_template('wind.html',sum="0.\n Turbines turn off to prevent damage.")
        else:
            sum = -0.039245646743791544 * x * x * x + 1.4820312482914098 * x * x -9.626324938316673 * x + 13.944999352467326
            return render_template('wind.html',sum=sum)
    elif operation == 'fourdegree':
        x = float(num1)
        if x > 24.45:
            return render_template('wind.html',sum="0.\n Turbines turn off to prevent damage.")
        else:
            sum = -0.00047024459774190115 * x * x * x * x -0.016092723170890756 * x * x * x + 1.1186246071694117 * x * x -7.691278963376663 * x +11.610280676819825
            return render_template('wind.html',sum=sum)
    elif operation == 'sevendegree':
        x = float(num1)
        if x > 24.45:
            return render_template('wind.html',sum="0.\n Turbines turn off to prevent damage.")
        else:
            sum = -3.941581283061136e-06 * x * x * x * x * x * x * x + 0.0003440770101137519 * x * x * x * x * x * x -0.011534818188543508 * x * x * x * x * x + 0.1838315165430236 * x * x * x * x -1.4091946634530912 * x * x * x + 5.095745633022115 * x * x -7.582268967728165 * x + 5.985976513515224
            return render_template('wind.html',sum=sum)
    else:
        console.log("FAIL")
        return render_template('wind.html')
