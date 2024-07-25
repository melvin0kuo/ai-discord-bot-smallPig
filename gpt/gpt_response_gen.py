from transformers import AutoTokenizer, AutoModelForCausalLM, TextIteratorStreamer
import torch
from threading import Thread

global_model = None
global_tokenizer = None

def get_model_and_tokenizer():
    global global_model, global_tokenizer
    return global_model, global_tokenizer

def set_model_and_tokenizer(model, tokenizer):
    global global_model, global_tokenizer
    global_model = model
    global_tokenizer = tokenizer
    return model, tokenizer
async def generate_response(inst, system_prompt, dialogue_history=None):
    global global_model, global_tokenizer
    
    model, tokenizer = get_model_and_tokenizer()
    if model is None or tokenizer is None:
        raise ValueError("Model or tokenizer is not set. Please load the model first.")

    # 增加系統提示與用戶指令到對話模板
    messages = [{'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': inst}]
    if dialogue_history is not None:
        messages = [{'role': 'system', 'content': system_prompt}]+dialogue_history+[{'role': 'user', 'content': inst}]    
    
    streamer = TextIteratorStreamer(tokenizer, skip_prompt=True)
    input_ids = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)

    attention_mask = (input_ids != tokenizer.pad_token_id).long()

    generation_kwargs = dict(
        inputs=input_ids,
        attention_mask=attention_mask,
        pad_token_id=tokenizer.pad_token_id,
        streamer=streamer,
        max_new_tokens=8192,
        do_sample=True,
        temperature=0.1,
        top_p=0.9,
    )
    
    thread = Thread(target=model.generate, kwargs=generation_kwargs)
    thread.start()  # 启动线程
    return thread, streamer