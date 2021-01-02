from pprint import pprint
from allennlp.predictors import Predictor

DEFAULT_NER_MODEL = "https://storage.googleapis.com/allennlp-public-models/ner-model-2020.02.10.tar.gz"


class EntityRecognizer:
    def __init__(self, model_url: str = None):
        model_url = model_url if model_url else DEFAULT_NER_MODEL
        self.predictor = Predictor.from_path(model_url)

    def get_labels(self, sentence: str):
        predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/ner-model-2020.02.10.tar.gz")
        results = predictor.predict(sentence=sentence)
        output = []
        partial = []
        for word, tag in zip(results["words"], results["tags"]):
            if tag == 'O':
                if partial: output.append(" ".join(partial))
                partial.clear()
            else:
                partial.append(word)
        if partial: output.append(" ".join(partial))
        return output
