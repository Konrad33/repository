from src.pred.models.torch_pred import *
from typing import Any


def torch_run_classifier(image: str) -> Any:
    img = load_image(image)  # loading image
    if img is None:
        return None
    input_batch = torch_preprocess(img)  # preprocessing image
    top_labels = torch_predict(input_batch, model=None)  # prediction
    return top_labels[0]


