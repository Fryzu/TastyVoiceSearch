import time
import speech_recognition as sr
from utils import recognize_speech


def get_ingredients():
    device_index = len(sr.Microphone.list_microphone_names()) - 1
    recognizer = sr.Recognizer()
    microphone = sr.Microphone(device_index=device_index)
    start_phrase = "Please input ingredients: "
    phrase_time_limit = 5
    ingredients = []
    print('Get ready!')
    time.sleep(1)
    while 1:
        input_text = recognize_speech.recognize_speech_from_mic(
            recognizer, microphone, start_phrase, phrase_time_limit)
        if not input_text["success"]:
            break
        if input_text["error"]:
            print("ERROR: {}".format(input_text["error"]))
            break

        print(f"Ingredients: {input_text['transcription'].lower().split(' ')}")
        print("Are this right? (y/n)")
        if input() == 'n':
            continue
        ingredients += input_text["transcription"].lower().split(' ')

        print("Do you want to input more ingredients? (y/n)")
        if input() == 'n':
            break

    # remove duplicate ingredients
    final_ingredients = list(set(ingredients))
    print(f"Final ingredients are: {final_ingredients}")
    return final_ingredients
