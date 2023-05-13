import os
import openai

from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'Config', '.env')
load_dotenv(dotenv_path)
openai.api_key = os.getenv('OPENAI_API_KEY')


def generate_text(prompt, model, params):
    response = openai.ChatCompletion.create(
        model=model,
        messages=prompt,
        max_tokens=params["max_new_tokens"],
        n=params["n"],
        temperature=params["temperature"],
        top_p=params["top_p"],
        presence_penalty=params["penalty_alpha"],
        stop=params["stop"],
    )

    reply = response.choices[0].message.content
    return reply
