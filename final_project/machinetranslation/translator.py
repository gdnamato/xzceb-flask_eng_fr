"""This module translates text from English to French and vice versa"""


from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """This function translates text from English to French"""
    french_text = MyMemoryTranslator(source="en-GB", target="fr-FR").translate(english_text)
    return french_text

def french_to_english(french_text):
    """This function translates text from French to English"""
    english_text = MyMemoryTranslator(source="fr-FR", target="en-GB").translate(french_text)
    return english_text
