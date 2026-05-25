# import torch
#
# print("Torch:", torch.__version__)
# print("CUDA available:", torch.cuda.is_available())
# print("CUDA version:", torch.version.cuda)
# print("GPU:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else None)
#
# from sentence_transformers import SentenceTransformer
#
# embedding_model = SentenceTransformer(
#     "sentence-transformers/all-MiniLM-L6-v2",
#     device="cuda",
#     local_files_only=True
# )
#
# print(embedding_model.device)
#
# sentences = ["This is a test sentence."]
# embeddings = embedding_model.encode(sentences)
#
# print(embeddings.shape)

import sys
import torch

print("Executable:", sys.executable)
print("Prefix:", sys.prefix)
print("Torch file:", torch.__file__)
print("Torch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("CUDA version:", torch.version.cuda)