from deep_translator import GoogleTranslator

def translate(string, dest='ru'):
    translator = GoogleTranslator(source='auto', target=dest)
    result = translator.translate(string) 
    return result
