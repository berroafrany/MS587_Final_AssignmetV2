from flask import Flask, render_template
 
app = Flask(__name__)
 
# Audiobook data

audiobooks = [

    {"title": "Elara and the Heartwood's Song", "filename": "Elara_and_the_Heartwoods_Song.mp3"},

    {"title": "Nuts About Tutus Squeakys Big Leap", "filename": "Nuts_About_Tutus_Squeakys_Big_Leap.mp3"},

    {"title": "Nimbus the Not-So-Cloudy Hat", "filename": "Nimbus_the_Not-So-Cloudy_Hat.mp3"},

    {"title": "Sparkys Scrap Run", "filename": "Sparkys_Scrap_Run.mp3"},

    {"title": "Flickers Unexpected Spark", "filename": "Flickers_Unexpected_Spark.mp3"},

]
 
@app.route("/")

def index():

    return render_template("index.html", audiobooks=audiobooks)
 
if __name__ == "__main__":

    app.run(port=5000, debug=True)




        