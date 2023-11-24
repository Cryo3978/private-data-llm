from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores import ChromaVectorStore
from llama_index.storage.storage_context import StorageContext
import docx2txt
import PyPDF2
import logging
import sys
import numpy as np
import chromadb
# 运行检验
# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


# load some documents
documents = SimpleDirectoryReader("./data").load_data()

# initialize client, setting path to save data
db = chromadb.PersistentClient(path="./chroma_db")

# create collection
chroma_collection = db.get_or_create_collection("quickstart")

# assign chroma as the vector_store to the context
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)



# # 从Vector_store读取旧的embedding
# index = VectorStoreIndex.from_vector_store(
#     vector_store, storage_context=storage_context
# )

# 训练一个新的embedding，要用这个.
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context
)



# Test: create a query engine and query
#Query your data
query_engine = index.as_query_engine()
question1="Who will hold a birthday party?"
print("Q1:"+question1)
response = query_engine.query(question1)
print("A1:")
print(response)

#Storing your index as json
index.storage_context.persist()
import os.path
from llama_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

# check if storage already exists
if not os.path.exists("./storage"):
    # load the documents and create the index
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    # 获取所有文档的嵌入向量

    # store it for later
    index.storage_context.persist()
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context)


# # either way we can now query the index
# query_engine = index.as_query_engine()
# question2="Who will be invited by Tom to his party?"
# print("Q2:"+question2)
# response = query_engine.query(question2)
# print("A2:")
# print(response)

# # 查询数据
# query_engine_loaded = loaded_index.as_query_engine()
# question3 = "What are the main achievements of Shuheng Chen?"
# print("Q3:" + question3)
# response3 = query_engine_loaded.query(question3)
# print("A3:")
# print(response3)

