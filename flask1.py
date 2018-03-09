# -*- coding: cp1252 -*-
from flask import Flask, render_template,request
import wikipedia
app = Flask(__name__)

@app.route('/new',methods=['GET','POST'])
def new():
	try:
		if request.method == 'POST':
			search_word=request.form['word']
			get=wikipedia.summary(search_word,3)
			link=wikipedia.page(search_word)
			return render_template('defi_app.html',get=get,link=link.url,sw=search_word)
	except:
		
		return render_template('defi_app.html',get="Enter a valid query \nYou might be getting this error for\n1.Name error\n2.Name clashes\n3.Illegal word usage\n")


	return render_template('defi_app.html')
    
   

if __name__ == '__main__':
   app.run(debug=True)
