from groq import Groq

# PUT YOUR API KEY HERE
client = Groq(api_key="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")


def ask_brain(user_text):

    print("USER:", user_text)

    chat = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_text
            }
        ],
        model="llama-3.1-8b-instant",
    )

    reply = chat.choices[0].message.content

    print("AI:", reply)

    return reply


# test mode
if __name__ == "__main__":

    while True:

        user_input = input("You: ")

        response = ask_brain(user_input)

        print("AI:", response)
