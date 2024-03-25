import google.generativeai as genai

from config import API_KEY_GENAI


class Gemini:
    def __init__(self):
        self.client = genai.configure(api_key=API_KEY_GENAI)
        self.model = genai.GenerativeModel('gemini-pro')

    def generate_feedback(self, content: str):
        response = self.model.generate_content(
            "Give me short feedback to the written factual information and provide links for detailed information."
            "The provided feedback must be like this: "
            "Feedback: provided feedback text must max length=300.\n"
            "Useful links: \n\n"
            f"Information: {content}"
        )

        return response.text