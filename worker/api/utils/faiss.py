import pickle

import faiss
import numpy as np
from django.conf import settings


def load_index(dimension):
    """
    Load or init FAISS index
    """
    try:
        index = faiss.read_index(str(settings.FAISS_INDEX_PATH))
        with open(str(settings.PRODUCT_IDS_PATH), "rb") as f:
            index.product_ids = pickle.load(f)
    except RuntimeError:
        index = faiss.IndexFlatL2(dimension)
        index.product_ids = []
    return index


def save_index(index):
    faiss.write_index(index, str(settings.FAISS_INDEX_PATH))
    with open(str(settings.PRODUCT_IDS_PATH), "wb") as f:
        pickle.dump(index.product_ids, f)


def add_to_index(index, feature_vector, product_id):
    feature_vector = np.array([feature_vector], dtype="float32")
    if not hasattr(index, "product_ids"):
        index.product_ids = []
    index.add(feature_vector)
    index.product_ids.append(str(product_id))
    save_index(index)
