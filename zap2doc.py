import openai 
from key import OPEN_API_KEY

openai.api_key = OPEN_API_KEY
# FIRST_PROMPT = {"role": "system", "content": "You are a text quality assistant. You will receive a text of a informal conversation and make a document in a formal context"}
FIRST_PROMPT = {"role": "system", "content": "Você é um assistente que garantirá a qualidade dos documentos gerados. Você receberá um texto informal e irá reescreve-lo de maneira formal, como se fosse o trabalho de conclusão de curso de estudante de direito"}
MODEL = "gpt-3.5-turbo-0301"
TEMPERATURA = 0 

def Read_Text(path: str) -> str:
    with open(path) as f:
        return f.read()

def Make_Api_Call(message: list[dict]) -> str:
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
    try:
        response = Make_Api_Call(examples+message)
    except openai.error.InvalidRequestError:
        response = Make_Api_Call(message)
    return response

def Receive_Examples(roles: list[str], contents: list[str]) -> list[dict]:
    return [{"role":role, "content":content} for role, content in zip(roles, contents)]

def main():
    path: str = r"teste.txt"
    roles: str = [""]
    contents: str = [""]

    print(Zap_2_Doc(path, roles, contents))

if __name__ == '__main__':
    main()