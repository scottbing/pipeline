# -*- coding: iso-8859-15 -*-
import os, sys
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torchaudio
#from speaking import speak

# globals
context = ""
qa = pipeline("question-answering")

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
    "Question10": "What are the gas bubble in basalt called?"
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
    qa = pipeline("question-answering")

    # process each query
    for value in queries.values():
        #answer = qa(question=value, context=context)
        answer = query(value)



    # # Print the answer
    # print(f"Question01: {question01}")
    # print(f"Answer: '{answer['answer']}' with score {answer['score']}")
    #
    # question02 = "Where does andesitic compositions exist?"
    # #context = context
    #
    # # Generating an answer to the question in context
    # #qa = pipeline("question-answering")
    # answer = qa(question=question02, context=context)
    #
    # # Print the answer
    # print(f"Question02: {question02}")
    # print(f"Answer: '{answer['answer']}' with score {answer['score']}")
    #
    #
    # question03 = "What is Tephrochronology?"
    # #context = context
    #
    # # Generating an answer to the question in context
    # #qa = pipeline("question-answering")
    # answer = qa(question=question03, context=context)
    #
    # # Print the answer
    # print(f"Question03: {question03}")
    # print(f"Answer: '{answer['answer']}' with score {answer['score']}")
    #
    # question04 = "Do volcanoes exist on other planets?"
    # #context = context
    #
    # # Generating an answer to the question in context
    # #qa = pipeline("question-answering")
    # answer = qa(question=question04, context=context)
    #
    # # Print the answer
    # print(f"Question04: {question04}")
    # print(f"Answer: '{answer['answer']}' with score {answer['score']}")
    #
    # question05 = "What type of volcano is Cerro Verde?"
    # #context = context
    #
    # # Generating an answer to the question in context
    # #qa = pipeline("question-answering")
    # answer = qa(question=question05, context=context)
    #
    # # Print the answer
    # print(f"Question05: {question05}")
    # print(f"Answer: '{answer['answer']}' with score {answer['score']}")
    #
    # question06 = "How old is the oldest rock in Albuqueruqe?"
    # #context = context
    #
    # # Generating an answer to the question in context
    # #qa = pipeline("question-answering")
    # answer = qa(question=question06, context=context)
    #
    # # Print the answer
    # print(f"Question06: {question06}")
    # print(f"Answer: '{answer['answer']}' with score {answer['score']}")
    #
    # question07 = "What does the gradual weathering of the loose cinders create?"
    # #context = context
    #
    # # Generating an answer to the question in context
    # #qa = pipeline("question-answering")
    # answer = qa(question=question07, context=context)
    #
    # # Print the answer
    # print(f"Question07: {question07}")
    # print(f"Answer: '{answer['answer']}' with score {answer['score']}")
    #
    # question08 = "What causes fissure eruption of the Albuquerque Volcanoes?"
    # #context = context
    #
    # # Generating an answer to the question in context
    # #qa = pipeline("question-answering")
    # answer = qa(question=question08, context=context)
    #
    # # Print the answer
    # print(f"Question08: {question08}")
    # print(f"Answer: '{answer['answer']}' with score {answer['score']}")
    #
    # question09 = "What is the name of the composite volcanoe that is 2.5 million years old?"
    # #context = context
    #
    # # Generating an answer to the question in context
    # #qa = pipeline("question-answering")
    # answer = qa(question=question09, context=context)
    #
    # # Print the answer
    # print(f"Question09: {question09}")
    # print(f"Answer: '{answer['answer']}' with score {answer['score']}")
    #
    # question10 = "What are the gas bubble in basalt called?"
    # #context = context
    #
    # # Generating an answer to the question in context
    # #qa = pipeline("question-answering")
    # answer = qa(question=question10, context=context)
    #
    # # Print the answer
    # print(f"Question10: {question10}")
    # print(f"Answer: '{answer['answer']}' with score {answer['score']}")

if __name__ == "__main__":
    main()
