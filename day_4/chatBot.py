import ollama
msgs=[{"role":"system","content":"answer the questions like a doctor"}]
while True:
    question=input("ask a question:")
    if question.lower()=='exit':
        break
    msgs.append({"role":"user",
                 "content":question})
    response=ollama.chat(
        model="llama3.2:3b",
        messages=msgs
    )
    msgs.append({"role":"assistant",
                 "content":response["message"]["content"]})

    print(response["message"]["content"])
print("----chat history\n")
for msg in msgs:
    if msg["role"]=="system":
        break
    print(msg["role"],":",msg["content"]) 