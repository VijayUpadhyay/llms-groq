try:
    import ollama
except Exception as e:
    raise RuntimeError(
        "Missing dependency 'ollama'. Install it with: python3 -m pip install ollama"
    ) from e

if __name__ == "__main__":
    try:
        model_name = "gemma3:1b"
        prompt = "what is the distance between egl domlur in Bangalore, India and Devanahalli in bangalore? \
        How long will it take to travel by car and bus?"

        response = ollama.chat(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            stream=True,
        )
        print("response received:")
        for chunk in response:
            print(chunk["message"]["content"], end="", flush=True)
    except Exception as e:
        print(e)
    finally:
        print("finally block executed")
    print("execution completed!!")
