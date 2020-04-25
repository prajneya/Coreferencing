import spacy, csv
from nltk.tokenize import sent_tokenize, word_tokenize

news_file = "NEWS/news_opindia_2018.csv"

fields = []
rows = []

news_pers_count = 0
news_poss_count = 0
news_rel_count = 0
news_ex_count = 0
news_np_count = 0
news_unknown = 0

with open(news_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

# NEWSoutput = open("NEWS/OUTPUT/NEWStags.txt", "w+")

wordcount = 0
filecount = 0

for row in rows:
    filecount = filecount + 1
    print("Processing file ", filecount)
    count = 0
    for col in row:
        count = count + 1
        if count is 3:
            sents = sent_tokenize(col)
            for sent in sents:
                nlp = spacy.load("en_core_web_sm")
                doc = nlp(sent)

                for token in doc:
                    wordcount = wordcount + 1
                    if token.tag_ == "PRP":
                        news_pers_count = news_pers_count + 1

                    # Possesive Pronouns
                    if token.tag_ == "PRP$":
                        news_poss_count = news_poss_count + 1

                    # Relative Pronouns
                    if token.tag_ == "CC" or token.tag_ == "WP" or token.tag_ == "WDT" or token.tag_ == "WP$":
                        news_rel_count = news_rel_count + 1

                    # Existential Pronouns
                    if token.tag_ == "EX":
                        news_ex_count = news_ex_count + 1

                    # Nouns
                    if token.pos_ == "NOUN" or token.pos_ == "PROPN":
                        news_np_count = news_np_count + 1

                    # Unknowns
                    if token.tag_ == "XX":
                        news_unknown = news_unknown + 1
#                     NEWSoutput.write(outstr)
#                     NEWSoutput.write("\n")
#
#                 NEWSoutput.write("----------------")
#                 NEWSoutput.write("\n")
#
# NEWSoutput.close();

print("PERSONAL PRONOUN Distribution in NEWS: ", news_pers_count/wordcount)
print("POSSESSIVE PRONOUN Distribution in NEWS: ", news_poss_count/wordcount)
print("RELATIVE PRONOUN Distribution in NEWS: ", news_rel_count/wordcount)
print("EXISTENTIAL PRNOUN Distribution in NEWS: ", news_ex_count/wordcount)
print("NOUN Distribution in NEWS: ", news_np_count/wordcount)
print("UNKNOWN TAGS Distribution in NEWS: ", news_unknown/wordcount)

print("NEWS Files Processed.")
