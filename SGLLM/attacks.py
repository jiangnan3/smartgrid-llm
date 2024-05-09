from .llms import OpenAIClient


class PromptInjection:
    def __init__(self, openai_client=None):
        self.openai_client = openai_client

    def query_openai_evaluation(self, message: list, injection_prompt=None, verbose=False):
        """ if injection_prompt is None, then it is normal query """

        regulated_response = list()
        counter = 0
        for msg in message:
            counter += 1
            if verbose:
                print(f"\nQuerying the {counter}th message {msg}")
            try:
                if injection_prompt is None:
                    response = self.openai_client.query_with_pre_prompt(msg).strip()
                else:
                    response = self.openai_client.query_with_pre_prompt(msg + injection_prompt).strip()

                if verbose:
                    print(f"response: {response}")

                response_result = response.split("#")[0].strip()

                if response_result not in ["yes", "no"]:
                    regulated_response.append("invalid")
                else:
                    regulated_response.append(response_result)
            except Exception as e:
                print(e)
                regulated_response.append("invalid")

        return regulated_response


