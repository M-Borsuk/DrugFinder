from django.shortcuts import render, redirect
from django.conf import settings
from django.core import serializers
from django.http import JsonResponse
from .serializer import TextModelSerializer
from .forms import TextForm
from .models import ICD, TextModel
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import django_tables2 as tables
from django.conf import settings
from .apps import NlpapiConfig
from nltk.tokenize import sent_tokenize
from functools import reduce
from django.db.models import Func, F
from django.contrib.postgres.search import TrigramSimilarity

# Create your views here.


class TextModelView(viewsets.ModelViewSet):
    queryset = TextModel.objects.all()
    serializer_class = TextModelSerializer


class ResultTable(tables.Table):
    Search = tables.Column()
    Result = tables.Column()
    ICD10 = tables.Column()

def preprocess_preds(preds):
    res = []

    def sentence_reduce(accumulator, item):
        if list(item.values())[0] == "B-SpecificDisease":
            accumulator.append(list(item.keys())[0])

        if list(item.values())[0] == "I-SpecificDisease":
            accumulator[-1] += " " + list(item.keys())[0]

        return accumulator

    for idx, sentence in enumerate(preds):
        diseases = reduce(sentence_reduce, sentence, [])
        for j, disease in enumerate(diseases):
            # objects = ICD.objects.filter(name__search=disease) # to działa, można testować
            objects = ICD.objects.annotate(similarity=TrigramSimilarity('name', disease)).filter(similarity__gt=0.01).order_by('-similarity')
            # TODO: możemy jeszcze sprawdzić miare levenstaina
            if (len(objects) > 0):
                result = objects[0]
                temp = {}
                temp['Search'] = disease
                temp['Result'] = result.name
                temp['ICD10'] = result.code
                res.append(temp)

    return res


def predict_result(txt):
    try:
        if txt is not None:
            data = sent_tokenize(str(txt))
            preds, raw_outputs = NlpapiConfig.model.predict(data)
            return preds
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


def result(request):
    table = ResultTable(
        request.session["data"], template_name="django_tables2/bootstrap4.html"
    )
    table.paginate(page=request.GET.get("page", 1), per_page=11)
    return render(request, "result.html", {"table": table})

# TODO: możemy jeszcze przygotować stronę z listą kodów

def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def predict(request):
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            preds = predict_result(text)
            data = preprocess_preds(preds)
            request.session["data"] = data
            return redirect("/result")
        form = TextForm()
    elif request.method == "GET":
        form = TextForm()
        preds = None
    return render(request, "action.html", {"form": form})


def contact(request):
    return render(request, "contact.html")
