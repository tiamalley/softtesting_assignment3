from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = ''
    category = ''

    if request.method == 'POST' and 'weight' in request.form:
        weightLB = float(request.form.get('weight'))
        heightIn = float(request.form.get('heightIn'))
        heightFt = float(request.form.get('heightFt'))        

        heightInches = (heightFt * 12) + heightIn

        bmi = float(calc_bmi(heightInches, weightLB))
        category = categoryBMI(bmi)

    return render_template("index.html",
	                        bmi=bmi,
                            category=category
                            )

def calc_bmi(heightIN, weightLB):
    weight = weightLB * .45

    height = heightIN * .025

    calc = height * height

    cal_bmi = (weight/calc)

    return round(cal_bmi, 1)

def categoryBMI(bmi):
    if(bmi < 18.5):
        return('Underweight')
    
    elif((bmi >= 18.5) and (bmi < 25.0)):
        return('Normal Weight')

    elif((bmi >= 25.0) and (bmi < 30.0)):
        return('Overweight')

    elif(bmi >= 30.0):
        return('Obese')

if __name__ == '__main__':
    app.run()
