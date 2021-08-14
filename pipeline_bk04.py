# -*- coding: iso-8859-15 -*-
import os, sys
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torchaudio
#from speaking import speak

# globals
context = ""
qa = pipeline("question-answering")  # set up the model pipeline once

queries = { # set up dictioanry to hold questions
    "Question01": "How old are the Albuquerque volcanoes?",
    "Question02": "Where does andesitic compositions exist?",
    "Question03": "What is Tephrochronology?",
    "Question04": "Do volcanoes exist on other planets?",
    "Question05": "What type of volcano is Cerro Verde?",
    "Question06": "How old is the oldest rock in Albuqueruqe?",
    "Question07": "What does the gradual weathering of the loose cinders create?",
    "Question08": "What causes fissure eruption of the Albuquerque Volcanoes?",
    "Question09": "What is the name of the composite volcanoe that is 2.5 million years old?",
    "Question10": "What are the gas bubble in basalt called?",
    "Question11": "What do rocks in the Palomas Volcanic Field consist of?",
    "Question12": "What are the volcanic features of the Palomas Volcanic Field?",
    "Question13": "Where is the ZUNI-BANDERA FIELD AND MCCARTY'S LAVA FLOW located?",
    "Question14": "What surface is fairly common to many pahoehoe flows?",
    "Question15": "How far does the The Navajo Dine volcanic field extend?",
    "Question16": "How was the Valles Caldera formed?",
    "Question17": "What is the largest volcanic field within the Rio Grande rift?",
    "Question18": "What geologic feature is located in the central part of Charette Mesa, northwest of Wagon Mound?",
    "Question19": "Where did the most recent volcictivity occur in New Mexico?",
    "Question20": "what are the floors of the Jornada caves covered with?"
    }

def query(question):
    # Generating an answer to the question in context
    # qa = pipeline("question-answering")
    answer = qa(question=question, context=context)

    # Print the answer
    #print(f"{0}: {1}", question, answer)
    print("{0}: ".format(question))
    print(f"Answer: '{answer['answer']}' with score {answer['score']}")

def main():
    global qa, context

    # get the volcano corpus
    with open('volcanic.corpus', encoding="utf8") as file:
        context = file.read().replace('\n', '')

    # set up the pipeline
    #qa = pipeline("question-answering")

    # process each query
    for value in queries.values():
        #answer = qa(question=value, context=context)
        answer = query(value)

if __name__ == "__main__":
    main()
