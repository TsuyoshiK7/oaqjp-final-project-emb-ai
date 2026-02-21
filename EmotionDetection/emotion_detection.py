import requests
import json

def emotion_detector(text_to_analyse):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=myobj, headers=header)
    if response.status_code == 400:
        json_str = '''{"anger":"None","disgust":"None","fear":"None","joy":"None","sadness":"None","dominant_emotion":"None"}'''
        data = json.loads(json_str)
        return data

    data = json.loads(response.text)
    emotions = data["emotionPredictions"][0]["emotion"]
    emotions['dominant_emotion'] = get_highest_emotion(emotions)
    return emotions

def get_highest_emotion(json_input):
    highest_label = max(json_input, key=json_input.get)
    return highest_label