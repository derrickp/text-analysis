import spacy
import en_core_web_md

nlp = en_core_web_md.load()

en_doc = nlp(u'Hello, world. Here are two sentences')
token = en_doc[0]
sentence = next(en_doc.sents)
assert token is sentence[0]
assert sentence.text == 'Hello, world.'