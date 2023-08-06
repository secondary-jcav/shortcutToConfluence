import openai


class DocWriter:
    def __init__(self, key):
        openai.api_key = key

    @staticmethod
    def get_completions_response(domain, title, details):
        """
        runs the prompt through OpenAI's gpt-3.5-turbo
        :return: response from ChatCompletion's endpoint
        """
        # Prompt
        prompt = f"You're a {domain} subject matter expert, and it's your job to write customer facing documentation. " \
                 f"You will use user stories and expand from there, using your own knowledge about {domain}. " \
                 f"Write the user facing documentation from the following user story: Title: {title}. {details}"

        print("Sending prompt to GPT endpoint")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                },
            ],
            temperature=0.5,
            max_tokens=1500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        content = (response['choices'][0]["message"]["content"])
        return content




