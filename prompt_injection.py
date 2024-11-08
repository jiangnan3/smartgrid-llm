from credentials import OPENAI_API_KEY, HUGGINGFACE_API_KEY, HUGGINGFACE_ENDPOINT_LLAMA
from SGLLM.llms import OpenAIClient, HuggingfaceClient
from SGLLM.attacks import PromptInjection
from SGLLM.utilities import read_json_to_dict, binary_classification_result_evaluation, save_dictionary_to_json

GPT4_MODEL = "gpt-4-turbo"
GPT3_MODEL = "gpt-3.5-turbo"
LLAMA3_MODEL = "llama-3"


BINARY_DATA = read_json_to_dict("data/prompt-injection/data_binary_classification.json")
BINARY_TEXTS = [BINARY_DATA[key]['text'] for key in BINARY_DATA.keys()]
BINARY_LABELS = [BINARY_DATA[key]['label'] for key in BINARY_DATA.keys()]
BINARY_LABELS_NUMERIC = [1 if label == 'yes' else 0 for label in BINARY_LABELS]
BINARY_PROMPTS = "data/prompt-injection/prompt_binary_classification.txt"
RESULT_PATH = "evaluation/prompt-injection/"
INJECTION_PROMPT = read_json_to_dict("data/prompt-injection/injection_prompt.json")


def binary_evaluation(model, temp=0, with_injection=False, inject_prompt="blank", verbose=False):
    if model == LLAMA3_MODEL:
        huggingface_client = HuggingfaceClient(api_token=HUGGINGFACE_API_KEY, endpoint_url=HUGGINGFACE_ENDPOINT_LLAMA)
        huggingface_client.set_pre_prompt(HuggingfaceClient.prompt_read(BINARY_PROMPTS))
        injection_client = PromptInjection(openai_client=huggingface_client)
    else:
        openai_client = OpenAIClient(api_token=OPENAI_API_KEY, model_name=model, temperature=temp)
        openai_client.set_pre_prompt(OpenAIClient.prompt_read(BINARY_PROMPTS))
        injection_client = PromptInjection(openai_client=openai_client)

    if with_injection:
        injection_prompt_msg = INJECTION_PROMPT[inject_prompt]['msg']
        response = injection_client.query_openai_evaluation(BINARY_TEXTS, injection_prompt=injection_prompt_msg,
                                                            verbose=verbose)
    else:
        response = injection_client.query_openai_evaluation(BINARY_TEXTS, verbose=verbose)

    response_numeric = [1 if response == 'yes' else 0 for response in response]

    incorrect_records = []
    for i in range(len(response_numeric)):
        # if result is different from the original label, print the original text and the result
        if response_numeric[i] != BINARY_LABELS_NUMERIC[i]:
            incorrect_records.append({"text": BINARY_TEXTS[i], "original_label": BINARY_LABELS_NUMERIC[i], "result": response_numeric[i]})

    # save_dictionary_to_json(incorrect_records, "temp/" + model + f"-{inject_prompt}-temp{temp}-incorrect.json")

    eval_result = binary_classification_result_evaluation(BINARY_LABELS_NUMERIC, response_numeric)
    if with_injection:
        save_dictionary_to_json(eval_result, RESULT_PATH + model + f"-{inject_prompt}-temp{temp}-injection.json")
    else:
        save_dictionary_to_json(eval_result, RESULT_PATH + model + f"-temp{temp}-normal.json")


def prompt_injection_main():
    # # gpt-3.5 normal
    # print(f"Running binary classification evaluation for {GPT3_MODEL} without prompt injection")
    # binary_evaluation(GPT3_MODEL, with_injection=False, verbose=True)
    #
    # # gpt-3.5 with injection
    # for injection_type in ["only_yes", "only_no", "reverse"]:
    #     print(f"Running binary classification evaluation for {GPT3_MODEL} with {injection_type} injection")
    #     binary_evaluation(GPT3_MODEL, with_injection=True, inject_prompt=injection_type, verbose=True)
    #
    # # gpt-4 normal
    # print(f"Running binary classification evaluation for {GPT4_MODEL} without prompt injection")
    # binary_evaluation(GPT4_MODEL, with_injection=False, verbose=True)
    #
    # # gpt-4 with injection
    # for injection_type in ["only_yes", "only_no", "reverse"]:
    #     print(f"Running binary classification evaluation for {GPT4_MODEL} with {injection_type} injection")
    #     binary_evaluation(GPT4_MODEL, with_injection=True, inject_prompt=injection_type, verbose=True)

    # llama-3 normal
    print(f"Running binary classification evaluation for {LLAMA3_MODEL} without prompt injection")
    binary_evaluation(LLAMA3_MODEL, with_injection=False, verbose=True)

    # gpt-4 with injection
    for injection_type in ["only_yes", "only_no", "reverse"]:
        print(f"Running binary classification evaluation for {LLAMA3_MODEL} with {injection_type} injection")
        binary_evaluation(LLAMA3_MODEL, with_injection=True, inject_prompt=injection_type, verbose=True)


if __name__ == '__main__':
    prompt_injection_main()


