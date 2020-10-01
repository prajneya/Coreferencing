# Coreferencing

This is the codebase for the Computational Linguistics - 1: Course Project and is maintained by Prajneya Kumar and Jayant Panwar. Our primary aim in this project is to analyse the notion of Corelation relations in spoken languages versus written text and we intend to do so by analysing transcripts of certain video lectures and some online news articles, which will be our general domain for written text. 

## Usage

To run the code, certain dependencies need to be installed, which are listed below:

* Spacy - Instructions to install [here](https://spacy.io/usage)
* Stanford CoreNLP - Instructions to install [here](https://stanfordnlp.github.io/CoreNLP/)
* NLTK - Instructions to install [here](https://www.nltk.org/install.html)

**pos.py** annotates POS tags for the spoken text domain, which is AI and Chemistry for our case. <br>
**news_pos.py** annotates POS tags for the written text domain, which is General NEWS for our case. <br> <br>
**tag.py** annotates Penn TreeBank tags and calculates pronoun distribution in the spoken genre. <br>
**news_tags.py** annotates Penn TreeBank tags and calculates pronoun distribution in the written genre. <br> <br>
**coref.py** runs a coreferencing model on our data, make sure to put the Stanford's CoreNLP Suite in this subdirectory before running, which can be downloaded from [here](https://stanfordnlp.github.io/CoreNLP/). <br> <br>

Outputs of each of the domains are stored in their respective folders.

## Manual CoreNLP Server

To run the CoreNLP Server for manual checking, all the jar files in the CoreNLP Suite are run using the following command: <br>
` java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000 1 `
