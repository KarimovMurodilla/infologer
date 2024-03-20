import google.generativeai as genai

from config import API_KEY_GENAI


class Gemini:
    def __init__(self):
        self.client = genai.configure(api_key=API_KEY_GENAI)
        self.model = genai.GenerativeModel('gemini-pro')
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
        response = self.model.generate_content(
            "Give me short feedback to the written factual information. max_length=300. "
            "Do'nt use markdown. Don't add headers like: 'Feedback:'. "
            f"Information: {content}"
        )

        return response.text