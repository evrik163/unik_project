from google_trans_new import google_translator  
from deep_translator import GoogleTranslator
#translator = Translator(service_urls=['translate.googleapis.com'])

def translate(string, dest='ru'):
    translator = GoogleTranslator(source='auto', target=dest)
    result = translator.translate(string) 
    return result
