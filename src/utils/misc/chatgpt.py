from openai import OpenAI

from config import API_KEY_OPENAI


class ChatGPT:
    def __init__(self):
        self.client = OpenAI(api_key=API_KEY_OPENAI)
        self.system_content = (
            "You are not assistant. You are AI feedbacker. "
            "You must check carefully written factual information "
            "and give advice and detailed feedback to the written factual information which "
            "sentences provide factual information or express a statement. "
            "Also Your role is to carefully evaluate written factual information and provide detailed feedback.\n\n"

            "Important!\n"
            "If the words set are typically used in everyday communication like: ['Hello', 'Hi','Who are you?', "
            "'What's your name?'], you must say: 'That doesn't seem like specific information.'"
        )

    def generate_feedback(self, content: str):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", 
                    "content":  self.system_content
                },
                    
                {"role": "user", "content": content}
            ],
            temperature=1,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        return response.choices[0].message.content