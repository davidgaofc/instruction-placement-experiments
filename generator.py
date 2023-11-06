import os
import openai
openai.api_key = "YOUR_API_KEY"

def get_prompt(prompt):
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": prompt}
      ]
    )

    return completion.choices[0].message.content, completion.usage.completion_tokens

def generate_all_prompts():
    for folder in os.listdir("prompts"):
        print(f"Folder: {folder}")
        for file in os.listdir(f"prompts/{folder}"):
            print(f"File: {file}")
            filename = file.split(".")[0] + ".py"
            with open(f"prompts/{folder}/{file}", "r") as f:
                prompt = f.read()
                if (not os.path.exists(f"responses/{folder}/{filename}")):
                    print("Generating response")
                    response, token_r = get_prompt(prompt)
                    print("writing response")
                    with open(f"responses/{folder}/{filename}", "w") as f:
                        f.write(response)
                        f.write("\n\n tokens:"+ str(token_r))

def main():
    generate_all_prompts()

main()