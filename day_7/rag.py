from sentence_transformers import SentenceTransformer
import chromadb,ollama,streamlit as st
#model=SentenceTransformer("all-MiniLM-L6-v2")
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")
model=load_model()
file_name="sample.txt"
with open(file_name,"r") as file:
    text=file.read()

#chunking
chunks=[]
chunk_size=100
chunk_overlap=20
step=chunk_size-chunk_overlap #100-20=80
for i in range(0,len(text),step):
    chunk=text[i:i+chunk_size] #(0-100)(80-180)(160)
    chunks.append(chunk)
#Embedding
embeddings=model.encode(chunks)
client=chromadb.PersistentClient(path="./chroma_db")
collection=client.get_or_create_collection(name="My_Documents")
ids=[]
for i in range(len(chunks)):
    ids.append(f"{file_name}_{i}")

collection.add(ids=ids,documents=chunks, embeddings=embeddings.tolist())
res=collection.get()
chunk1=collection.get(ids=['sample.txt_0'])
print(chunk1)
#query phase
question=input("ask")
q_embedding=model.encode(question)
top_k=3
results=collection.query(
    query_embeddings=[q_embedding.tolist()],
    n_results=top_k
)
retrieved_chunks=(results['documents'][0])
retrieved_ids=results["ids"][0]
context='\n'.join(retrieved_chunks)
#prompting
prompt=f'''
Answer the question using the context given below only.
Question:{question}
Context:{context}
Answer:
'''

response=ollama.chat(
model="llama3.2:3b",
messages=[{"role":"user",
"content":prompt}])
print(response["message"]["content"])
