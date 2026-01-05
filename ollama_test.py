import ollama

if __name__ == "__main__":
    try:
        model_name = "gemma3:1b"
        prompt = "Why should we use Deep Learning?"

        response = ollama.chat(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        print("response received:")
        print(response)
    except Exception as e:
        print(e)
    finally:
        print("finally block executed")
    print("execution completed!!")

    