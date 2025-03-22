# -*- coding: utf-8 -*-
import json
from transformers import pipeline

#Cargar el modelo una sola vez al iniciar el módulo
classifier = pipeline(
    "text-classification",
    model="best_model"
)

def classi_spam(text):
    result = classifier(str(text))
    return result
