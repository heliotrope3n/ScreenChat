from flask import Flask, render_template, request

#testing
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/chat", methods=['POST'])
def chat():
    input = request.form['userInput']
    print(input)
    return render_template('chat.html', input=input)

@app.route("/about")
def about():
    return render_template('about.html')
    
if __name__ == "__main__":
    app.run()
