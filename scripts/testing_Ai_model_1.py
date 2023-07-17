import spacy




english_nlp = spacy.load("C:\\Users\JibrilBanu\Documents\GitHub\CV_Parser\Resume_Parser\Training_AI\JSON Files\Training_JSON\\Name_email_referencesv3\\model-best")




file_path = "C:\\Users\JibrilBanu\Documents\GitHub\\CV_Parser\AIModelShowcase\SpecificModel\\6.txt"



with open(file_path, 'r',encoding='utf-8') as file:

    text = file.read()




spacy_parser = english_nlp(text)




for entity in spacy_parser.ents:

    print(f'Found: {entity.text} of type: {entity.label_}')


