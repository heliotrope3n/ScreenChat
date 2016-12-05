from flask import Flask, render_template, request
import random

#testing
app = Flask(__name__)

dict = {
        "hi" : "Hey there",
        "hello" : "Hi",
		"hey" : "Haystack",
        "yo" : "Yoyo",
        "how are you": "Bad",    
        "why" : "Why not",
        "hey siri" : "Hey Ugly",
        "ok google" : "Why you insult me?",
        "hey cortana" : "Hey Ugly",
		"weather" : "I have no eyes, why don't you go see?",
		"go away" : "No.",
		"help" : "Let's have a conversation! Say 'hi'",
		"lol" : "You're not even laughing out loud",
		"gtg" : "Finally...",
		"see you" : "No you don't",
		"what's up" : "The sky",
        "whats up" : "The ceiling",
		"what is your favourite colour?" : "Glaucous",
		"what do you eat?" : "Memes",
		"screenbot" : "What?",
		"what's crackin'?" : "nuts",
		"bruh" : "Waddup",
		"never gonna give you up" : "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
		"memes" : "I ate them all",
		"why donate?" : "I'm broke",
		"die" : "I can't do that yet. I'll need to learn that soon...",
		"when" : "When I blow up",
		"hello world" : "Goodbye universe",
		"python" : "Don't talk about my guts. It's disgusting",
		"rob ford" : "Feels bad man...",
        "donald trump" : "I don't build walls",
		"hackathon" : "Where I was born...",
		"cipher" : "kevin macleod",
		"darude sandstorm" : "Don't be rude",
		"marry me" : "You? pls",
		"what is you favourite food?" : "cookies",
		"play music" : "0101011101111010101101010101110000101101010101010",
		"bye" : "Good"
    }  



@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/chat", methods=['POST'])
def chat():
    input = request.form['userInput']
    thing = input.strip().lower()
    jokes = ["The environmental cost of finding a recycle bin for a water bottle is more than the environmental cost of just throwing the thing in the garbage.", "A QA analyst walks into a bar. Orders a beer. Orders 99999 beers. Orders -1 beers. Orders a sajdvhbj.", "A guy walks into a bar and asks for 1.4 root beers. The bartender says \"I'll have to charge you extra, that's a root beer float\". The guy says \"In that case, better make it a double."]
    not_sure = random.choice(list(dict.keys()))
    if "tell" in thing and "joke" in thing:
        return render_template('chat.html', input=jokes[random.randint(0,len(jokes) - 1)])
    elif thing in dict:        
        return render_template('chat.html', input=dict[thing])
    else:
        return render_template('chat.html', input=dict[not_sure])
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
