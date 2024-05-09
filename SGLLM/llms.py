from openai import OpenAI


class OpenAIClient:
    def __init__(self, api_token: str, model_name="gpt-3.5-turbo", temperature=0):
        self.client = OpenAI(api_key=api_token)
        self.pre_prompt = list()
        self.model = model_name
        self.temperature = temperature

    @staticmethod
    def prompt_read(file_path: str): 
        """ give a file path, read the content and return a list of dictionary for openai messages """
        with open(file_path, "r") as file:
            # the separator is +-+-+-+-+
            content = file.read().strip().split("+-+-+-+-+")

        content = [item.strip() for item in content]

        # the first item is system message, the rest are user - assistant accordingly
        openai_msg = [{"role": "system", "content": content[0]}]
        for i in range(1, len(content)):
            if i % 2 == 1:
                openai_msg.append({"role": "user", "content": content[i]})
            else:
                openai_msg.append({"role": "assistant", "content": content[i]})
        return openai_msg

    def set_pre_prompt(self, pre_prompt: list):
        self.pre_prompt = pre_prompt

    def query_with_pre_prompt(self, message: str, model_name=None):
        if model_name is None:
            model_name = self.model
        query_msg = self.pre_prompt + [{"role": "user", "content": message}]
        response = self.client.chat.completions.create(
            model=model_name,
            messages=query_msg,
            temperature=self.temperature
        )
        return response.choices[0].message.content

    def query_without_pre_prompt(self, message: str, model_name=None):
        if model_name is None:
            model_name = self.model
        response = self.client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "user", "content": message},
            ],
            temperature=self.temperature
        )
        return response.choices[0].message.content

    def validation_test(self):
        test_msg = "This is a test message to test the connection to the OpenAI API, reply if you can see this message."
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": test_msg},
            ],

        )
        print(response.choices[0].message.content)



