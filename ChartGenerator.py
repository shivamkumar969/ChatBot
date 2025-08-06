import pandas as pd
import matplotlib.pyplot as plt
def create_chart():
    fpath="static/knowledge_base"
    kn_df=pd.read_excel(fpath+"/CB_knowledgeBase.xlsx")
    df=(kn_df.groupby(['Category'])['Frequency'].sum().sort_values(ascending=False))
    # print(df)
    plt.figure(figsize=(6,5),facecolor='pink')
    df.plot(kind="pie",ylabel="",autopct='%1.1f%%')
    plt.savefig("static/Chart/frequency_pie.png")