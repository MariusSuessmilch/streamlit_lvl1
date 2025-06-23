from openai import OpenAI
import os
from dotenv import load_dotenv

# Lade Umgebungsvariablen aus der .env-Datei
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def chat_gpt(user_prompt, system_prompt, model="gpt-4o-mini"):
    """Sendet eine Anfrage an die OpenAI API und gibt eine Streaming-Antwort zurück.
    
    Diese Funktion ermöglicht die Kommunikation mit ChatGPT. Der user_prompt ist die Frage eines Benutzers,
    der system_prompt ist die Systemanweisung, die das Verhalten des Modells steuert (z.B. "Du bist Mathe-Lehrer").
    Die Funktion gibt die Antgwot von ChatGPT als String aus.

    Parameter:
    -----------
    user_prompt : str
        Die Eingabe des Benutzers, der an das Modell gesendet wird.
    system_prompt : str
        Die Systemanweisung, die das Verhalten des Modells steuert.
    model : str, optional
        Das zu verwendende Sprachmodell (Standard: "gpt-4o-mini").
        Andere mögliche Werte sind z.B. "gpt-4", "gpt-3.5-turbo", etc.
        
    Rückgabewert:
    ------------
    Die Antwort des Modells
        
    Beispiel:
    --------
    >>> antwort = st.write(chat_gpt("Wie geht's dir?", "Du bist ein hilfreicher Assistent."))
    """
    client = OpenAI(api_key=OPENAI_API_KEY)
    completion = client.chat.completions.create(
        model=model,
        store=True,
        messages=[
            {"role": "system", "content": f"{system_prompt}"},
            {"role": "user", "content": f"{user_prompt}"}
        ],
        stream=True
    )
    return completion