from sentence_transformers import SentenceTransformer


class PARSE:
    def __init__(self):
        # BGE_model_path=config.BGE_model_path
        self.model = SentenceTransformer('BAAI/bge-small-zh-v1.5')


    def parse(self,content):
        vector = self.model.encode(content, normalize_embeddings=True)
        return vector
