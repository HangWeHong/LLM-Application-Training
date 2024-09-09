from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader=WebBaseLoader("https://www.geeksforgeeks.org/htm-web-page-format/")
#print(loader.load())

text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(loader.load)
print(all_splits)

oembed = OllamaEmbeddings(base_url="http://localhost:11434", model="nomic-embed-text")
vectorstore = Chroma.from_documents(documents=all_splits, embedding=oembed)