from django.apps import AppConfig
from simpletransformers.ner import NERModel
from nltk.tokenize import sent_tokenize
from django.conf import settings

class NlpapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'NLPAPI'
    model_path = settings.MODELS / 'best_model_2'
    model = NERModel(
                "bert", model_path,use_cuda=False, from_tf=False
            )