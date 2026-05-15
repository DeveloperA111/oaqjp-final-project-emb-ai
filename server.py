''' This module enables emotion detection
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    ''' This code receives the text from the HTML interface and 
    runs emotion detection over it using emotion_detector()
    function. The output returned shows the emotions and their 
    scores and dominant emotion for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    serverresponse=emotion_detector(text_to_analyze)
    dominantemotion=serverresponse['dominant_emotion']

    if dominantemotion is None:
        return "Invalid text! Please try again!"

    message = (
        f"For the given statement, the system response is "
        f"'anger': {serverresponse['anger']}, "
        f"'disgust': {serverresponse['disgust']}, "
        f"'fear': {serverresponse['fear']}, "
        f"'joy': {serverresponse['joy']} and "
        f"'sadness': {serverresponse['sadness']}. "
        f"The dominant emotion is {serverresponse['dominant_emotion']}."
    )

    return message

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
    page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
