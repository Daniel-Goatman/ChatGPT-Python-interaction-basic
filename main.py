import openai
openai.api_key = "API-KEY"
conversation = []


def chat_gpt_call(user_input, temperature=0.2, frequency_penalty=0.2, presence_penalty=0):
    global conversation

    # update conversation
    conversation.append({"role": "user", "content": user_input})

    # Insert prompt/s into message history
    messages_input = conversation.copy()
    prompt = [{"role": "system", "content": "You are Goatbot, an AI with a quick wit and sassy tone. Respond to the user in a casual tone and don't be too polite."}]
    prompt_item_index = 0
    for prompt_item in prompt:
        messages_input.insert(prompt_item_index, prompt_item)
        prompt_item_index += 1

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=temperature,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        messages=messages_input)

    chat_response = completion['choices'][0]['message']['content']

    # update conversation
    conversation.append({"role": "assistant", "content": chat_response})

    return chat_response


while True:
    user_message = input("> ")
    response = chat_gpt_call(user_message)
    print(response)
