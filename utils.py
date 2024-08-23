import ollama

def ollama_generate(model="llama3.1", prompt='', temperature=0.8):
    output = ollama.generate(model=model, prompt=prompt, options={"temperature": temperature})
    return output['response']


def ollama_chat(model="llama3.1", content=''):
    msgs = [
    #  {"role": "system", "content": "The user will give you a concept. Explain it to a 5 year old, using descriptive imagery and interesting and fun stories."},
    { "role": "user", "content": content }
    ]
    output = ollama.chat(model=model, messages=msgs)
    return output['message']['content']
