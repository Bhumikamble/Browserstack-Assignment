# Step 1: Import translation library
from deep_translator import GoogleTranslator

def translate_text(text):
    # Step 2: Try to translate text from Spanish to English
    try:
        # Step 3: Translate text using Google Translator
        translated = GoogleTranslator(source='es', target='en').translate(text)
        # Step 4: Return the translated text
        return translated
    # Step 5: Handle translation errors gracefully
    except Exception as e:
        print("Translation error:", e)
        # Step 6: Return original text if translation fails
        return text