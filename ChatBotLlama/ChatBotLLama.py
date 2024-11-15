import ollama
import chainlit as cl

@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("chat_history", [])
    cl.user_session.set("chat_history", [{"role": "system",
                      "content": "behave as if you are news reporter."}])

@cl.on_message
async def generate_response(query: cl.Message):
    chat_history = cl.user_session.get("chat_history")
    chat_history.append({"role": "user", "content": query.content})
    
    response = cl.Message(content="")
    answer = ollama.chat(model="llama3.1", messages=chat_history, stream=True) #stream=true to not sending as total message, but as generator to loop thru
    
    complete_answer = ""
    for token_dict in answer:
        token = token_dict["message"]["content"] #keeping the content of the response
        complete_answer += token
        await response.stream_token(token) #display the token as stream on the UI
    
    chat_history.append({"role": "assistant", "content": complete_answer})    
    cl.user_session.set("chat_history", chat_history)

    await response.send()