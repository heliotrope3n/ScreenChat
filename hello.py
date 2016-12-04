from flask import Flask, render_template, request

#testing
app = Flask(__name__)


dict = {
    "joke" : "You are the joke",
    "hi" : "Hey there",
    "hello" : "Hi",
    "How are": "Bad",    
}

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/chat", methods=['POST'])
def chat():
    input = request.form['userInput']
    thing = input.strip().lower()
    if thing in dict:
        return render_template('chat.html', input=dict[thing])
    else:
        return render_template('chat.html', input="I can't do that yet")

@app.route("/about")
def about():
    return render_template('about.html')
    
if __name__ == "__main__":
    app.run()
