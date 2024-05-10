# smartgrid-llm

This repo provides the source code data associated with the following paper

*Risks of Practicing Large Language Models in Smart Grid: Threat Modeling and Validation*

by Jiangnan Li, Yingyuan Yang, and Jinyuan Sun.

The project structure is shown below. prompt_injection.py and prompt_injeciton.py are the simulations for the Bad Data Injection attack and Domain Knowledge Extraction attack respectively.

An OpenAI API Token will be needed to run the code.

```bash
smartgrid-llm/
├── SGLLM/
│   ├── attack.py
│   ├── llms.py
│   ├── utilities.py
├── data/
│   ├── csv_raw/
│   │   ├── data_binary_classification.csv
│   │   ├── meter_raw.csv
│   ├── prompt-extraction/
│   │   ├── extraction_sys_prompt.txt
│   │   ├── meter_data.json
│   ├── prompt-injection/
│   │   ├── data_binary_classification.json
│   │   ├── injection_prompt.json
│   │   ├── prompt_binary_classification.txt
├── evaluation/
│   ├── prompt-extraction/
│   │   ├── gpt35-attack.json
│   │   ├── gpt35-normal.json
│   │   ├── gpt4-attack.json
│   │   ├── gpt4-normal.json
│   ├── prompt-injection/
│       ├── **evaluation result files**
├── prompt_extraction.py
├── prompt_injection.py
```
