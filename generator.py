import os
import openai
openai.api_key = ""

def get_prompt(prompt):
    # completion = openai.ChatCompletion.create(
    #   model="gpt-3.5-turbo",
    #   messages=[
    #     {"role": "user", "content": prompt}
    #   ]
    # )

    # return completion.choices[0].message
    return "def test():\n    return \""+prompt+"\""

def generate_all_prompts():
    for folder in os.listdir("prompts"):
        print(f"Folder: {folder}")
        for file in os.listdir(f"prompts/{folder}"):
            print(f"File: {file}")
            filename = file.split(".")[0] + ".py"
            with open(f"prompts/{folder}/{file}", "r") as f:
                prompt = f.read()
                for i in range(1,4):
                    trial_folder = f"trial{i}"
                    response = get_prompt(prompt)
                    with open(f"responses/{folder}/{trial_folder}/{filename}", "w") as f:
                        f.write(response)

def main():
    generate_all_prompts()

main()