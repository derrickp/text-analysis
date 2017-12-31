import spacy
import en_core_web_md

nlp = en_core_web_md.load()

def get_doc(text):
    return nlp(text)

def clean_text(text):
    cleaned_text = text.replace("\r\n", "")
    cleaned_text = cleaned_text.replace("\n", "")
    return cleaned_text

def process_text(text):
    cleaned = clean_text(text)
    doc = get_doc(cleaned)
    output = {}
    # nouns = {}
    # verbs = {}
    sentence_count = 0
    stops = 0
    unique_verb_count = 0
    verb_count = 0
    unique_noun_count = 0
    noun_count = 0
    entities = []
    unique_entities = []
    lemma_sentences = []
    words = {}
    for sentence in enumerate(doc.sents):
        lemma_words = []
        sentence_count = sentence_count + 1
        for item in sentence:
            # When you enumerate doc.sents, it first returns the index, then a Span for the sentence
            if isinstance(item, int):
                continue
            # If it isn't an int (the index), then it's a Span, so we can go 
            for word_tuple in enumerate(item):
                word = word_tuple[1]
                if not word.is_stop and not word.is_punct and not word.is_space:
                    if word.lemma_ not in words:
                        words[word.lemma_] = 1
                    else:
                        words[word.lemma_] = words[word.lemma_] + 1
                    lemma_words.append(word.lemma_)
                    # if word.pos_ in ["NOUN", "PROPN"]:
                    #     noun_count = noun_count + 1
                    #     if word.lemma_ not in nouns:
                    #         nouns[word.lemma_] = 1
                    #         unique_noun_count = unique_noun_count + 1
                    #     else:
                    #         nouns[word.lemma_] = nouns[word.lemma_] + 1
                    # if word.pos_ in ["VERB"]:
                    #     verb_count = verb_count + 1
                    #     if word.lemma_ not in verbs:
                    #         unique_verb_count = unique_verb_count + 1
                    #         verbs[word.lemma_] = 1
                    #     else:
                    #         verbs[word.lemma_] = verbs[word.lemma_] + 1
                if word.is_stop:
                    stops = stops + 1
            lemma_sentence = " ".join(lemma_words)
            if lemma_sentence != "":
                lemma_sentences.append(lemma_sentence)
    for num, entity in enumerate(doc.ents):
        key = entity.text + "_" + entity.label_
        if key not in unique_entities:
            unique_entities.append(key)
            entities.append("Entity {}: {} ~ {}".format(num + 1, entity, entity.label_))
    output["nounCount"] = noun_count
    output["uniqueNounCount"] = unique_noun_count
    output["verbCount"] = verb_count
    output["uniqueVerbCount"] = unique_verb_count
    output["sentences"] = sentence_count
    output["entities"] = entities
    output["stopCount"] = stops
    output["words"] = words
    output["lemmaSentences"] = lemma_sentences
    return output
