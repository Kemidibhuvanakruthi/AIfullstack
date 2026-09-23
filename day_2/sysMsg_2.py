import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
      {
           "role":"system",
 	        "content": "you are teaching to a 5 year old child and Give the answers in 2-3 lines only"   
	  },
      {
           "role":"user",
 	        "content": "what is buffalo?"
     
	  }
        ]
)
print(response["message"]["content"])