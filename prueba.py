from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    api_key=os.getenv("GOOGLE_API_KEY")
)

vector = embeddings.embed_query("Hola mundo")

print("Dimensiones:", len(vector))
print(vector[:5])