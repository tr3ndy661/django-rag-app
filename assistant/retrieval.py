# from os import listdir
# from os.path import isfile, join

import os


def find_best_doc(question):
    best_score = -1
    best_file = None
    best_content = ''

    question_words = set(question.lower().split())

    # files = [file for file in listdir('assistant/docs') if isfile (join('assistant/docs', file))]

    # splitFiles = [set(file.open.read.split()) for file in files]
    # return set.intersection(*splitFiles, question) if splitFiles else set()

    directory_path = 'assistant/docs'

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:

                raw_text = f.read()

                file_words = set(raw_text.lower().split())

                common_elements = file_words.intersection(question_words)

                # common_elements = file_words.intersection(set(question).split())

                # common_elements = file_words.intersection(set(question.split()))

                

                score = len(common_elements)

            if score > best_score:
                best_score = score
                best_file = filename
                best_matches = list(common_elements)
                best_content = raw_text


        return best_content
