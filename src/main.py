from flask import Flask, request, render_template, jsonify
import openai
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
import faiss
import os

app = Flask(__name__)

# Ensure the OPENAI_API_KEY environment variable is set
openai.api_key = os.getenv('OPENAI_API_KEY')
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# Initialize LangChain components
embeddings = OpenAIEmbeddings(openai_api_key=openai.api_key)

# Determine embedding dimensions
try:
    # Generate a test embedding and check its length
    test_embedding = embeddings.embed_query('test')
    embedding_dimension = len(test_embedding)  # Length of the list
except Exception as e:
    raise ValueError(f"Could not determine embedding dimensions: {str(e)}")

# Initialize an empty in-memory document store
docstore = InMemoryDocstore()

# Initialize the FAISS index with the correct number of dimensions
index = faiss.IndexFlatL2(embedding_dimension)

# Initialize the FAISS vector store
vector_store = FAISS(embedding_function=embeddings, index=index, docstore=docstore, index_to_docstore_id={})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        filepath = os.path.join('documents', file.filename)
        file.save(filepath)
        # Add document indexing logic here
        return jsonify({'message': 'File uploaded successfully'})
    return jsonify({'message': 'No file uploaded'})

@app.route('/query', methods=['POST'])
def query():
    question = request.form['question']
    # Add document search and OpenAI API query logic here
    response = "Your generated response"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
