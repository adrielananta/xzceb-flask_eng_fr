"""
English to French and French to English translator
"""
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-03-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    English to French translator
    Takes one String input
    """
    try:
        response = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        french_text = response.get("translations")[0].get("translation")
        return french_text
    except (ApiException, ValueError) as ex:
        return type(ex).__name__

def french_to_english(french_text):
    """
    French to English Translator
    Takes one String input
    """
    try:
        response = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        english_text = response.get("translations")[0].get("translation")
        return english_text
    except (ApiException, ValueError) as ex:
        return type(ex).__name__
