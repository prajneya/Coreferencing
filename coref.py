import json
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'./stanford-corenlp-full-2020-04-20', quiet=False)
props = {'annotators': 'coref', 'pipelineLanguage': 'en'}

AIfilenames = ["AI/W2_AI_MOdule_5.txt", "AI/W2_AI_MOdule_6.txt", "AI/W3_AI_MOdule_7.txt", "AI/W3_AI_MOdule_8.txt", "AI/W4_AI_MOdule_9.txt", "AI/W4_AI_MOdule_10.txt", "AI/W4_AI_MOdule_11-Eng-Transcription.txt", "AI/W5_AI_MOdule_12-Eng-Transcription.txt", "AI/W5_AI_MOdule_13-Eng-Transcription.txt", "AI/W5_AI_MOdule_14-Eng-Transcription.txt", "AI/W5_AI_MOdule_15-Eng-Transcription.txt"]
CHEMfilenames = ["CHEMISTRY/FMFS_Module_1_Verified_Post_Verbatim_TScript.txt", "CHEMISTRY/FMFS_Module_2_Verified_Post_Verbatim_TScript.txt", "CHEMISTRY/FMFS_Module_4_Verified_Post_Verbatim_TScript.txt", "CHEMISTRY/FMFS_Module_5_Verified_Post_Verbatim_TScript.txt", "CHEMISTRY/FMFS_Module_6_Verified_Post_Verbatim_TScript.txt", "CHEMISTRY/FMFS_Module_7_Verified_Post_Verbatim_TScript.txt", "CHEMISTRY/FMFS_Module_8_Verified_Post_Verbatim_TScript.txt"]

for filename in AIfilenames:

    text = open(filename, "r").read()
    result = json.loads(nlp.annotate(text, properties=props))

    num, mentions = result['corefs'].items()[0]
    for mention in mentions:
        print(mention)

news_file = "NEWS/news_opindia_2018.csv"

fields = []
rows = []

news_pron_count = 0

with open(news_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

for row in rows:
    count = 0
    for col in row:
        count = count + 1
        if count is 3:
            text = col
            result = json.loads(nlp.annotate(text, properties=props))

            num, mentions = result['corefs'].items()[0]
            for mention in mentions:
                print(mention)
