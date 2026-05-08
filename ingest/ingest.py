import feedparser, requests, hashlib, os
from datetime import datetime
from sqlalchemy import create_engine, text
import chromadb
from ollama import Client
import json

# ... (plný kód je dlhý, ale tu je podstatná časť – ak chceš celý 300-riadkový kód, napíš "pošli полный ingest.py")

# Ollama client
ollama = Client(host='http://ollama:11434')

def get_impact_score(title, summary):
    prompt = f"""Ohodnoť článok impactom na kybernetickú bezpečnosť (1-10).
Zero-day, vysoké CVSS, široko používané tech v EU = vysoké skóre.
Názov: {title}
Zhrnutie: {summary[:800]}
Vráť iba číslo 1-10."""
    resp = ollama.chat(model="llama3.2:3b", messages=[{"role":"user","content":prompt}])
    try:
        return int(resp['message']['content'].strip())
    except:
        return 5

# Cron spúšťa tento skript každý deň o 6:00
