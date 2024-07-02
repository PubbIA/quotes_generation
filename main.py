import os
import uuid
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from langchain_google_genai import ChatGoogleGenerativeAI
import re

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")
PROJECT_NAME = os.getenv("PROJECT_NAME")

def get_random_quote(language:str ) -> str:
    """
    Fetches a random quote about respecting the coastline and picking up litter using Gemini API.

    Returns:
        str: A random quote.
    """
    try:
        # Utilisation du modèle Gemini pour générer une citation
        llm = ChatGoogleGenerativeAI(
            model=MODEL_NAME, google_api_key=GEMINI_API_KEY, project=PROJECT_NAME
        )
        

        # Prompt pour générer une citation sur le respect du littoral et le ramassage des poubelles
        prompt = "**Je suis Bard, un modèle de langage conçu pour vous fournir dans 1 ligne just des petites citations inspirantes sur le respect du littoral et l'importance de ramasser les poubelles. Voici votre citation en anglais :**"
        result = llm.invoke(prompt)
        quote = result.content.strip()
        if language == "francais":
            prompt = f"**je suis un expert en traduction, je peux traduire cette citation en français voila la citation en anglais:{quote}. Voici votre citation en français :**"
            result = llm.invoke(prompt)
            quote = result.content.strip()
        elif language == "arabe":
            prompt = f"**je suis un expert en traduction, je peux traduire cette citation en arabe voila la citation en anglais:{quote}. Voici votre citation en arabe :**"
            result = llm.invoke(prompt)
            quote = result.content.strip()

        else:
            quote = quote

        return quote    

    except Exception as e:
        return f"An error occurred while fetching the quote: {e}"

def display_random_quote():
    """
    Displays a random quote about respecting the coastline and picking up litter.
    """
    quote = get_random_quote(language="arabe")
    print(f"{quote}")

# Appel de la fonction pour afficher une citation
display_random_quote()
