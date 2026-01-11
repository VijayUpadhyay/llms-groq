from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

if __name__ == "__main__":
    try:
        model_name = "gemini-2.5-flash"
        prompt = "what is the distance between EGL Domlur in Bangalore, India and Devanahalli in bangalore? \
        How long will it take to travel by car and bus?"

        llm = ChatGoogleGenerativeAI(model=model_name, temperature=0.2)
        response = llm.invoke(prompt)
        print("response received:")
        print(response.content)

    except Exception as e:
        print(e)
    finally:
        print("finally block executed")
    print("execution completed!!")
