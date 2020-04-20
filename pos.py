import spacy
from nltk.tokenize import sent_tokenize, word_tokenize

AIfilenames = ["AI/W2_AI_MOdule_5.txt", "AI/W2_AI_MOdule_6.txt", "AI/W3_AI_MOdule_7.txt", "AI/W3_AI_MOdule_8.txt", "AI/W4_AI_MOdule_9.txt", "AI/W4_AI_MOdule_10.txt", "AI/W4_AI_MOdule_11-Eng-Transcription.txt", "AI/W5_AI_MOdule_12-Eng-Transcription.txt", "AI/W5_AI_MOdule_13-Eng-Transcription.txt", "AI/W5_AI_MOdule_14-Eng-Transcription.txt", "AI/W5_AI_MOdule_15-Eng-Transcription.txt"]
CHEMfilenames = ["CHEMISTRY/FMFS_Module_1_Verified_Post_Verbatim_TScript.txt", "CHEMISTRY/FMFS_Module_2_Verified_Post_Verbatim_TScript.txt", "CHEMISTRY/FMFS_Module_4_Verified_Post_Verbatim_TScript.txt", "CHEMISTRY/FMFS_Module_5_Verified_Post_Verbatim_TScript.txt", "CHEMISTRY/FMFS_Module_6_Verified_Post_Verbatim_TScript.txt", "CHEMISTRY/FMFS_Module_7_Verified_Post_Verbatim_TScript.txt", "CHEMISTRY/FMFS_Module_8_Verified_Post_Verbatim_TScript.txt"]

filecount = 0
wordcount = 0

ai_pron_count = 0
chem_pron_count = 0

AIoutput = open("AIoutput.txt", "w+")
AI_pron_output = open("AI_pron_output.txt", "w+")

for filename in AIfilenames:
    filecount = filecount + 1
    text = open(filename, "r").read()
    sents = sent_tokenize(text)
    print("Processing file ", filecount,  "...")
    for sent in sents:
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(sent)

        for token in doc:
            wordcount = wordcount + 1
            if token.pos_ == "PRON":
                ai_pron_count = ai_pron_count + 1
                outstr = token.text + " " + token.pos_
                AI_pron_output.write(outstr)
                AI_pron_output.write("\n")

            outstr = token.text + " " + token.pos_
            AIoutput.write(outstr)
            AIoutput.write("\n")

        AIoutput.write("----------------")
        AIoutput.write("\n")
        AI_pron_output.write("----------------")
        AI_pron_output.write("\n")


AIoutput.close()
AI_pron_output.close()

AI_pron_distribution = ai_pron_count/wordcount

print("PRONOUN Distribution in AI: ", AI_pron_distribution)

print("AI Files Processed.")

CHEMoutput = open("CHEMoutput.txt", "w+")
CHEM_pron_output = open("CHEM_pron_output.txt", "w+")

filecount = 0
wordcount = 0

for filename in CHEMfilenames:
    filecount = filecount + 1
    text = open(filename, "r").read()
    sents = sent_tokenize(text)
    print("Processing file ", filecount,  "...")
    for sent in sents:
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(sent)

        for token in doc:
            wordcount = wordcount + 1
            if token.pos_ == "PRON":
               chem_pron_count = chem_pron_count + 1
               outstr = token.text + " " + token.pos_
               CHEM_pron_output.write(outstr)
               CHEM_pron_output.write("\n")

            outstr = token.text + " " + token.pos_
            CHEMoutput.write(outstr)
            CHEMoutput.write("\n")

        CHEMoutput.write("----------------")
        CHEMoutput.write("\n")
        CHEM_pron_output.write("----------------")
        CHEM_pron_output.write("\n")


CHEMoutput.close()
CHEM_pron_output.close()

CHEM_pron_distribution = chem_pron_count/wordcount
print("PRONOUN Distribution in CHEM: ", CHEM_pron_distribution)
print("CHEM Files Processed.")
