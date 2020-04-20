import spacy, csv
from nltk.tokenize import sent_tokenize, word_tokenize

news_file = "NEWS/news_opindia_2018.csv"

fields = []
rows = []

news_pron_count = 0

with open(news_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

NEWSoutput = open("NEWSoutput.txt", "w+")
NEWS_pron_output = open("NEWS_pron_output.txt", "w+")

wordcount = 0

for row in rows:
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
                    if token.pos_ == "PRON":
                        news_pron_count = news_pron_count + 1
                        outstr = token.text + " " + token.pos_
                        NEWS_pron_output.write(outstr)
                        NEWS_pron_output.write("\n")
                    outstr = token.text + " " + token.pos_
                    NEWSoutput.write(outstr)
                    NEWSoutput.write("\n")

                NEWSoutput.write("----------------")
                NEWSoutput.write("\n")

NEWSoutput.close();

NEWS_pron_distribution = news_pron_count/wordcount
print("PRONOUN Distribution in NEWS: ", NEWS_pron_distribution)
