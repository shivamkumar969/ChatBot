# que=input("Enter Your Question :")
# cb_knownledgebas=pd.read_excel("CB_KnowledgeBase.xlsx")
# # filter=df[df["col_name"]condition]
# match=cb_knownledgebas[cb_knownledgebas["Question"].str.contains(que)]
# print(match)
# if not match.empty:
#     print(match["Answer1"].values[0])
# else:
#     print("Sorry, next Question.")

import pandas as pd
import numpy as np
import random
import datetime # Import the datetime module for timestamps
def search_knowledge(query):
    fpath="static/knowledge_base"
    knowledge_df=pd.read_excel(fpath+"/CB_KnowledgeBase.xlsx")
    unanswered_df=fpath+"/CB_Unanswered.xlsx"
    # filter=df[df["col_name"]condition]
    match=knowledge_df[knowledge_df["Question"].str.lower().str.contains(query.lower())]
    # blow  commented line will print all matching data
    # print(match)
    if not match.empty:
        # generating random index to pic random answer from 3 answers--
        ans_count=len(match)
        rand_index=random.randint(0,ans_count-1)
        # Updating frequency count of current search question
        cur_ques=match["Question"].values[rand_index]
        knowledge_df["Frequency"]=np.where(knowledge_df["Question"]==cur_ques,knowledge_df["Frequency"]+1,knowledge_df["Frequency"])
        knowledge_df.to_excel(fpath+"/CB_KnowledgeBase.xlsx",index=False)
        return match["Answer1"].values[rand_index]
    else:
        try:
            # Try to read the existing log file
            unanswere_df = pd.read_excel(unanswered_df)
        except FileNotFoundError:
            # If the file doesn't exist, create a new DataFrame
            unanswere_df = pd.DataFrame(columns=["Question", "Timestamp"])
        # Create a new entry with the query and the current time
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_question = pd.DataFrame([{"Question": query, "Timestamp": timestamp}])
        # Add the new entry to the DataFrame
        unanswere_df = pd.concat([unanswere_df, new_question], ignore_index=True)
        
        # Save the updated log file
        unanswere_df.to_excel(unanswered_df, index=False)
        return "Sorry, I could not understand. Please ask another question."