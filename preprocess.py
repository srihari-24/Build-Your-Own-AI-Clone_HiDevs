from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

text = load_text('faq.txt')
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.create_documents([text])

print(f"Loaded {len(chunks)} chunks")
print("Example chunk:", chunks[0].page_content)
