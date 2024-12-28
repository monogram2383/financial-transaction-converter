from deep_translator import GoogleTranslator
from tqdm import tqdm

from config import logger

# Initialize the translator once at startup
translator_en = GoogleTranslator(source='auto', target='en')


def translate_to_en(texts: list[str]) -> list[str]:
    logger.info(f"[TRANSLATION] Translating {len(texts)} texts to English:")

    results_en = []
    for text in tqdm(texts, desc="Translating...", leave=True):
        try: # attempt to translate a text
            translated = translator_en.translate(text=text)
        except Exception as e:
            logger.warning(f"[TRANSLATION] Failed to translate a text: {e}")
            translated = text # don't translate if failed

        results_en.append(translated)

    logger.info(f"[TRANSLATION] Message translated successfully.")
    return results_en
