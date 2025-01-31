# -*- coding: utf-8 -*-

import json
from transformers import pipeline



def classi_spam(text):
    classifier = pipeline(
      "text-classification",
      model="best_model"
    )
    result = classifier(str(text))
    #print(result)
    return result