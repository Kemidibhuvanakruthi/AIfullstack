import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
         {
           "role":"system",
 	   "content": "you are a technical assistant.give structured,precise,"
	  }
        ]
)
print(response["message"]["content"])