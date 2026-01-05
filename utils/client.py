from groq import Groq
import os

def get_groq_client() ->Groq :
    key=os.environ.get("GROQ_APIKEY")
    client = Groq(api_key=key)
    return client
