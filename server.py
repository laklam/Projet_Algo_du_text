from flask import Flask, render_template, request, jsonify, url_for, redirect


list_url=['univ','hey']

#création objet app
app = Flask(__name__, template_folder='.')
@app.route('/') #racine
def index():
  search = request.args.get('search')
  return render_template('index.html')



@app.route('/pageResults' , methods = ['GET', 'POST'])
def pageResults():
    search = request.form['search']
    if len(search)==0:
      return render_template('index.html')
    return render_template('pageResults.html', search=search, list_url=list_url)    

if __name__ == '__main__':
    app.run(debug=True)
