import spacy
from nltk.tokenize import sent_tokenize, word_tokenize

AIfilenames = ["AI/W2_AI_MOdule_5.txt", "AI/W2_AI_MOdule_6.txt", "AI/W3_AI_MOdule_7.txt", "AI/W3_AI_MOdule_8.txt", "AI/W4_AI_MOdule_9.txt", "AI/W4_AI_MOdule_10.txt", "AI/W4_AI_MOdule_11-Eng-Transcription.txt", "AI/W5_AI_MOdule_12-Eng-Transcription.txt", "AI/W5_AI_MOdule_13-Eng-Transcription.txt", "AI/W5_AI_MOdule_14-Eng-Transcription.txt", "AI/W5_AI_MOdule_15-Eng-Transcription.txt"]
CHEMfilenames = ["CHEMISTRY/FMFS_Module_1_Verified_Post_Verbatim_TScript.txt", "CHEMISTRY/FMFS_Module_2_Verified_Post_Verbatim_TScript.txt", "CHEMISTRY/FMFS_Module_4_Verified_Post_Verbatim_TScript.txt", "CHEMISTRY/FMFS_Module_5_Verified_Post_Verbatim_TScript.txt", "CHEMISTRY/FMFS_Module_6_Verified_Post_Verbatim_TScript.txt", "CHEMISTRY/FMFS_Module_7_Verified_Post_Verbatim_TScript.txt", "CHEMISTRY/FMFS_Module_8_Verified_Post_Verbatim_TScript.txt"]

filecount = 0
wordcount = 0

ai_pers_count = 0
ai_poss_count = 0
ai_rel_count = 0
ai_ex_count = 0
ai_np_count = 0
ai_unknown = 0

chem_pers_count = 0
chem_poss_count = 0
chem_rel_count = 0
chem_ex_count = 0
chem_np_count = 0
chem_unknown = 0

print("Hello, Mr. Kumar. Running your python script on secure server ...")

# AIoutput = open("AI/OUTPUT/AItags.txt", "w+")

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
            # Personal Pronouns
            if token.tag_ == "PRP":
                ai_pers_count = ai_pers_count + 1

            # Possesive Pronouns
            if token.tag_ == "PRP$":
                ai_poss_count = ai_poss_count + 1

            # Relative Pronouns
            if token.tag_ == "WP" or token.tag_ == "WDT" or token.tag_ == "WP$":
                ai_rel_count = ai_rel_count + 1

            # Existential Pronouns
            if token.tag_ == "EX":
                ai_ex_count = ai_ex_count + 1

            # Nouns
            if token.pos_ == "NOUN" or token.pos_ == "PROPN":
                ai_np_count = ai_np_count + 1

            # Unknowns
            if token.tag_ == "XX":
                ai_unknown = ai_unknown + 1

        #     outstr = token.text + " " + token.tag_
        #     AIoutput.write(outstr)
        #     AIoutput.write("\n")
        #
        # AIoutput.write("----------------")
        # AIoutput.write("\n")


# AIoutput.close()

print("PERSONAL PRONOUN Distribution in AI: ", ai_pers_count/wordcount)
print("POSSESSIVE PRONOUN Distribution in AI: ", ai_poss_count/wordcount)
print("RELATIVE PRONOUN Distribution in AI: ", ai_rel_count/wordcount)
print("EXISTENTIAL PRNOUN Distribution in AI: ", ai_ex_count/wordcount)
print("NOUN Distribution in AI: ", ai_np_count/wordcount)
print("UNKNOWN TAGS Distribution in AI: ", ai_unknown/wordcount)

print("AI Files Processed.")

# CHEMoutput = open("CHEMISTRY/OUTPUT/CHEMtags.txt", "w+")

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
            # Personal Pronouns
            if token.tag_ == "PRP":
                chem_pers_count = chem_pers_count + 1

            # Possesive Pronouns
            if token.tag_ == "PRP$":
                chem_poss_count = chem_poss_count + 1

            # Relative Pronouns
            if token.tag_ == "CC" or token.tag_ == "WP" or token.tag_ == "WDT" or token.tag_ == "WP$":
                chem_rel_count = chem_rel_count + 1

            # Existential Pronouns
            if token.tag_ == "EX":
                chem_ex_count = chem_ex_count + 1

            # Noun Phrases
            if token.pos_ == "NOUN" or token.pos_ == "PROPN":
                chem_np_count = chem_np_count + 1

            # Unknowns
            if token.tag_ == "XX":
                chem_unknown = chem_unknown + 1

#             outstr = token.text + " " + token.tag_
#             CHEMoutput.write(outstr)
#             CHEMoutput.write("\n")
#
#         CHEMoutput.write("----------------")
#         CHEMoutput.write("\n")
#
#
# CHEMoutput.close()

print("PERSONAL PRONOUN Distribution in CHEM: ", chem_pers_count/wordcount)
print("POSSESSIVE PRONOUN Distribution in CHEM: ", chem_poss_count/wordcount)
print("RELATIVE PRONOUN Distribution in CHEM: ", chem_rel_count/wordcount)
print("EXISTENTIAL PRNOUN Distribution in CHEM: ", chem_ex_count/wordcount)
print("NOUN Distribution in CHEM: ", chem_np_count/wordcount)
print("UNKNOWN TAGS Distribution in CHEM: ", chem_unknown/wordcount)

print("CHEM Files Processed.")
