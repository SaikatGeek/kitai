from langchain_docling.loader import DoclingLoader

loader = DoclingLoader(file_path="data/document.pdf")

# load all documents
docs  = loader.load()

print(docs[0].page_content)

