import unittest
from main import app, vector_store, embeddings

def get_embedding_dimension(embeddings):
    # Generate a test embedding and return its length
    test_embedding = embeddings.embed_query('test')
    return len(test_embedding)

class RAGApplicationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the RAG Application', response.data)

    def test_get_embedding_dimension(self):
        dimension = get_embedding_dimension(embeddings)
        self.assertIsInstance(dimension, int)
        self.assertGreater(dimension, 0)

    def test_vector_store_add_and_query(self):
        test_text = "This is a test document."
        vector_store.add_texts([test_text])
        results = vector_store.similarity_search("test document")
        self.assertGreater(len(results), 0)
        
        # Debug print to inspect attributes of the Document object
        print(vars(results[0]))

        self.assertIn(test_text, results[0].page_content)

if __name__ == '__main__':
    unittest.main()
