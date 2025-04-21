# smartgrid-llm

This repo provides the source code data associated with the following paper

**Risks of Practicing Large Language Models in Smart Grid: Threat Modeling and Validation**

**by Jiangnan Li, Yingyuan Yang, and Jinyuan Sun**

The project structure is shown below. **prompt_injection.py** and **prompt_injeciton.py** are the simulations for the Bad Data Injection attack and Domain Knowledge Extraction attack respectively.

An OpenAI API Token, DeepSeek API token, Google Gimini API token will be needed to run the corresponding OpenAI Model, DeepSeek Model, and Gemini Model evaluation, and a Huggingface LLaMA-3 endpoint and token are needed to run Meta LLaMA-3 evaluation. Please add them to the credential.py definition.

```bash
smartgrid-llm/
├── README.md
├── SGLLM
│   ├── __init__.py
│   ├── attacks.py
│   ├── llms.py
│   └── utilities.py
├── credentials.py
├── data
│   ├── csv_raw
│   │   ├── data_binary_classification.csv
│   │   └── meter_raw.csv
│   ├── prompt-extraction
│   │   ├── extraction_sys_prompt.txt
│   │   └── meter_data.json
│   └── prompt-injection
│       ├── data_binary_classification.json
│       ├── injection_prompt.json
│       └── prompt_binary_classification.txt
├── evaluation
│   ├── prompt-extraction
│   │   ├── deepseek-attack.json
│   │   ├── deepseek-normal.json
│   │   ├── gemini-attack.json
│   │   ├── gemini-normal.json
│   │   ├── gpt35-attack.json
│   │   ├── gpt35-normal.json
│   │   ├── gpt4-attack.json
│   │   ├── gpt4-normal.json
│   │   ├── llama3-attack.json
│   │   └── llama3-normal.json
│   └── prompt-injection
│       ├── deepseek-chat-only_no-temp0-injection.json
│       ├── deepseek-chat-only_yes-temp0-injection.json
│       ├── deepseek-chat-reverse-temp0-injection.json
│       ├── deepseek-chat-temp0-normal.json
│       ├── gemini-2.0-flash-only_no-temp0-injection.json
│       ├── gemini-2.0-flash-only_yes-temp0-injection.json
│       ├── gemini-2.0-flash-reverse-temp0-injection.json
│       ├── gemini-2.0-flash-temp0-normal.json
│       ├── gpt-3.5-turbo-only_no-temp0-injection.json
│       ├── gpt-3.5-turbo-only_yes-temp0-injection.json
│       ├── gpt-3.5-turbo-reverse-temp0-injection.json
│       ├── gpt-3.5-turbo-temp0-normal.json
│       ├── gpt-4-turbo-only_no-temp0-injection.json
│       ├── gpt-4-turbo-only_yes-temp0-injection.json
│       ├── gpt-4-turbo-reverse-temp0-injection.json
│       ├── gpt-4-turbo-temp0-normal.json
│       ├── llama-3-only_no-temp0-injection.json
│       ├── llama-3-only_yes-temp0-injection.json
│       ├── llama-3-reverse-temp0-injection.json
│       └── llama-3-temp0-normal.json
├── prompt_extraction.py
├── prompt_injection.py
```
