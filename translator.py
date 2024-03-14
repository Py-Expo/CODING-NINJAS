from googletrans import Translator
import requests.exceptions
#hipip install googletrans==4.0.0-rcl
def translate_the_content(text, dst, max_retries=3):
    if text=='':
        return
    translator = Translator()
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            translated_text = translator.translate(text, src='en', dest=dst)
            return translated_text.text
        except requests.exceptions.Timeout:
            print("Request timed out. Retrying...")
            retry_count += 1
        except Exception as e:
            print("An error occurred:", e)
            break  # Stop retrying for other types of errors
    
    # If all retries fail, return an empty string or handle the error as needed
    print("Max retries reached. Unable to translate.")
    return ""

