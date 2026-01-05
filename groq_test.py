from dotenv import load_dotenv
import utils

load_dotenv()

if __name__ == "__main__":
    try:
        groq_client = utils.get_groq_client()
        print(groq_client)
    except Exception as e:
        print(e)
    finally:
        print("finally block executed")
    print("execution completed!!")

    chat_completion = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
             {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "why should we use Deep Learning?"
            }
        ]
    )   
    print(chat_completion.choices[0].message.content)