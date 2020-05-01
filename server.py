from flask import Flask, render_template, request, jsonify, url_for, redirect

#liste de test pour affichage des résultats
#list_url=[['univ','https://www.univ-paris13.fr/'],['ent','https://cas.univ-paris13.fr/cas/login?service=https%3A%2F%2Fent.univ-paris13.fr']]

list_url=[]
#création objet app
app = Flask(__name__, template_folder='.')
@app.route('/') #racine
def index():
  search = request.args.get('search')
  return render_template('index.html')

@app.route('/pageResults' , methods = ['GET', 'POST'])
def pageResults():
    search = request.form['search']
    return render_template('pageResults.html', search=search, list_url=list_url)    

if __name__ == '__main__':
    app.run(debug=True)
