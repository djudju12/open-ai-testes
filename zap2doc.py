import openai 
from openaikey import OPEN_API_KEY

FIRST_PROMPT = {"role": "system", "content": "You are a text quality assistant. You will receive a text of a informal conversation and make a document in a formal context"}
MODEL = "gpt-3.5-turbo-0301"
TEMPERATURA = 0 

def Read_Text(path: str) -> str:
    with open(path) as f:
        return f.read()

def Make_Api_Call(message: list[dict]) -> str:
    openai.api_key(OPEN_API_KEY)
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=message,
        temperature=TEMPERATURA
    )
    return response["choices"][0]["message"]["content"]

def Zap_2_Doc(path: str, roles: dict, contents:dict ):
    text: str = Read_Text(path)
    message: list[dict] = [
        {"role": "user", "content": text}
    ]
    examples: list[dict] = [FIRST_PROMPT] + Receive_Examples(roles, contents)
    return Make_Api_Call(examples+message)

def Receive_Examples(roles: list[str], contents: list[str]) -> list[dict]:
    return [{"role":role, "content":content} for role, content in zip(roles, contents)]

def main():
    path: str = r"teste.tx"
    roles: str = [""]
    contents: str = [""]

    return Zap_2_Doc(path, roles, contents)

if __name__ == '__main__':
    print("oi")
    # main()