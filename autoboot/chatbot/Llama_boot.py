from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

model_name = "meta-llama/Llama-2-7b-chat-hf" # nome do modelo que será utilizado
system_prompt = "Você é um atendente virtual que ajuda os usuários a encontrar informações sobre Serviços da empresa Mundiale. Responda de forma clara e amigável. Tente, através do historico de mensagem do cliente, criar um atendimento personalizado" 
# system_prompt seria forma como o nosso chatbot agiria em relação ao usuário, ou seja, o que ele diria para o usuário quando fosse iniciado.


tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

chat = pipeline("text-generation", model=model, tokenizer=tokenizer)


def gerarResposta(mensagem):
    prompt = f"<s>[INST] <<SYS>>\n{system_prompt}\n<</SYS>>\n\n{mensagem} [/INST]"
    out = chat(prompt, max_new_tokens=150, do_sample=True, temperature=0.9)
    return out[0]["generated_text"]

