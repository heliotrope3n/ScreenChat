from flask import Flask, render_template, request
import random

#testing
app = Flask(__name__)





@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/chat", methods=['POST'])
def chat():
    input = request.form['userInput']
    thing = input.strip().lower()
    #jokes = ["You are the joke", "A guy walks into a bar and asks for 1.4 root beers. The bartender says \"I'll have to charge you extra, that's a root beer float\". The guy says \"In that case, better make it a double."]
    #i = random.randint(0,)
    dict = {
        "tell me a joke" : "You are the joke",
        "joke": "A guy walks into a bar and asks for 1.4 root beers. The bartender says \"I'll have to charge you extra, that's a root beer float\". The guy says \"In that case, better make it a double.",
        "hi" : "Hey there",
        "hello" : "Hi",
        "how are you": "Bad",    
        "why" : "Why not",
        "hey siri" : "Hey Ugly",
        "ok google" : "Why you insult me?",
        "hey cortana" : "Hey Ugly",   
}   
    if thing in dict:        
        return render_template('chat.html', input=dict[thing])
    else:
        return render_template('chat.html', input="I can't do that yet")
    #for t in dict:        
    #    if dict.key() in thing:
    #        return render_template('chat.html', input=dict[t])
    #else:
    #    return render_template('chat.html', input="I can't do that yet")

@app.route("/about")
def about():
    return render_template('about.html')
    
if __name__ == "__main__":
    app.run()
