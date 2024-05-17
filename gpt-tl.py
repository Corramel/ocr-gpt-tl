from openai import OpenAI

secret_file = open("./api/key.txt", "r")
secret_key = secret_file.readline()

client = OpenAI(api_key=secret_key)

def createResponse(lines):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", 
             "content": "You translate Japanese to English."},
            {"role": "user",
              "content": lines}
        ]
    )
    return {
        "message": response.choices[0].message.content,
        "in_tokens" : response.usage.prompt_tokens,
        "out_tokens" : response.usage.completion_tokens,
        "cost" : (( 5 / 1000000 ) * response.usage.prompt_tokens) + ((15 / 1000000 ) * response.usage.completion_tokens)
        }
text_to_tl = open("tl_text.txt", "r", encoding="utf-8")

jap_text = text_to_tl.read()

tl_txt = createResponse(jap_text)

print('-----------------------------------------TRANSLATED TEXT--------------------------------------------------')
print(tl_txt["message"])

print('---------------------------------------TOKEN COST---------------------------------------------------------')
print(tl_txt["in_tokens"])
print(tl_txt["out_tokens"])

print('-----------------------------------------TOTAL COST---------------------------------------------------------')
print(tl_txt["cost"])