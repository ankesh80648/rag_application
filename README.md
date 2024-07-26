# rag_application
RAG Application
A Flask-based Retrieval-Augmented Generation (RAG) application utilizing LangChain and OpenAI APIs.

#Table of Contents:

Installation
Configuration
Usage
Running Tests
Notes
#Installation
Prerequisites
Python 3.8 or higher
Pip (Python package installer)
Virtualenv 

#Steps
#Cloning the Repository

bash
git clone https://github.com/ankesh80648/rag_application.git
cd rag_application

#Create a Virtual Environment

bash
python -m venv env

#Activate the virtual environment:

bash

.\env\Scripts\activate

#Install Dependencies

bash

pip install -r requirements.txt


bash
pip install flask openai langchain langchain-openai langchain-community faiss-cpu
Configuration
Environment Variables

The application requires the OPENAI_API_KEY environment variable to interact with OpenAI's API.


#Setting the Environment Variable


bash

set OPENAI_API_KEY="sk-proj-9M8jXKoEfbRUYBhpIm6OT3BlbkFJHLujQkczs9PR3Hg9Lym1"


#Directory Structure
The directory structure is as follows:

bash

rag_application/
├── src/
│   ├── main.py
│   ├── tests/
│   │   └── test_app.py
│   └── documents/
├── env/          
├── requirements.txt
└── README.md

#Usage
#Running the Application
#To start the Flask application, use the following command:

bash

python src/main.py
The application will start and be accessible at http://127.0.0.1:5000.

#Accessing the Application
Open a web browser.
Navigate to http://127.0.0.1:5000.

#Uploading Documents
Navigate to the application interface.
Use the file upload form to upload documents.
The uploaded files will be saved in the documents directory.

#Querying
Enter a query into the provided form.
Submit the query to receive a response based on indexed documents.
Running Tests
To run the unit tests, use the following command:

bash
python -m unittest discover -s src/tests

#Test Cases

test_index_page: Verifies that the index page loads successfully.
test_get_embedding_dimension: Checks that the embedding dimension is correctly retrieved.
test_vector_store_add_and_query: Tests the addition and querying of documents in the vector store.


