from flask import Flask, render_template, request
import pickle




app=Flask(__name__)
#load the model
model=pickle.load(open('savedmodel.sav', 'rb'))

@app.route('/')
def home():
    result=''
    return render_template('index.html', **locals())

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    
    tmpGender=request.form['Gender']
    
    if tmpGender=="Male":
        tmpGender=1

    
    else:
        tmpGender=0
    
    Gender=float(tmpGender)

    tmpPython_exp=request.form['Python_exp']

    if tmpPython_exp=="Yes":
        tmpPython_exp=1

    
    else:
        tmpPython_exp=0
    Python_exp=float(tmpPython_exp)

    Experience_Years=float(request.form['Experience_Years'])


    tmpEducation=request.form['Education']

    if tmpEducation=="Graduate":
        tmpEducation=1

    
    else:
        tmpEducation=0
    Education=float(tmpEducation)
    
    tmpInternship=request.form['Internship']
    if tmpInternship=="Yes":
        tmpInternship=1

    
    else:
        tmpInternship=0
    Internship=float(tmpInternship)



    Score=float(request.form['Score'])
    Salary=float(request.form['Salary'])
    Offer_History =float(request.form['Offer_History '])
    tmpLocation=request.form['Location']

    if tmpLocation=="Urban":
        tmpLocation=3

    
    elif tmpLocation=="Semiurban":
        tmpLocation=2
    else:
        tmpLocation=2
    Location=float(tmpLocation)
    
    result=model.predict([[Gender, Python_exp, Experience_Years, Education,  Internship, Score, Salary, Offer_History , Location]])[0]
    return render_template('index.html', **locals())

if __name__=="__main__":
    app.run(debug=True)