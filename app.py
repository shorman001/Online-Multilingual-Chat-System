
import translate,sentiment,synthesize
from flask import Flask, render_template, request, jsonify, make_response, json
from flask_cors import CORS
from pusher import pusher
import os, requests, uuid, json
import simplejson

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# configure pusher object
pusher = pusher.Pusher(
app_id='PUSHER_APP_ID',
key='PUSHER_APP_KEY',
secret='PUSHER_APP_SECRET',
cluster='PUSHER_APP_CLUSTER',   
ssl=True)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/translate-text', methods=['POST'])
def translate_text():
    data = request.get_json()
    text_input = data['text']
    print(text_input)
    translation_output = data['to']
    print(translation_output)
    response = translate.get_translation(text_input, translation_output)
    print(response)
    return jsonify(response)

@app.route('/sentiment-analysis', methods=['POST'])
def sentiment_analysis():
    data = request.get_json()
    input_text = data['inputText']
    input_lang = data['inputLanguage']
    output_text = data['outputText']
    output_lang =  data['outputLanguage']
    response = sentiment.get_sentiment(input_text, input_lang, output_text, output_lang)
    return jsonify(response)

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.get_json()
    text_input = data['text']
    print(text_input)
    voice_font = data['voice']
    tts = synthesize.TextToSpeech(text_input, voice_font)
    tts.get_token()
    audio_response = tts.save_audio()
    return audio_response










@app.route('/new/guest', methods=['POST'])
def guestUser():
        data = request.json
        pusher.trigger(u'general-channel', u'new-guest-details', {
            'name' : data['name'],
            'email' : data['email']
            })
        return json.dumps(data)

@app.route("/pusher/auth", methods=['POST'])
def pusher_authentication():
        auth = pusher.authenticate(channel=request.form['channel_name'],socket_id=request.form['socket_id'])

        return json.dumps(auth)

if __name__ == '__main__':
        app.run(host='0.0.0.0:', port=5000, debug=True)
