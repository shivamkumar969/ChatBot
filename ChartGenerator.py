import os
import pandas as pd
import matplotlib

# ✅ MUST be before pyplot
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def create_chart():
    try:
        # ✅ Correct absolute path
        base_dir = os.path.dirname(os.path.abspath(__file__))

        file_path = os.path.join(base_dir, "static", "knowledge_base", "CB_knowledgeBase.xlsx")

        # ✅ Read Excel
        kn_df = pd.read_excel(file_path)

        df = kn_df.groupby(['Category'])['Frequency'].sum().sort_values(ascending=False)

        # ✅ Create chart
        plt.figure(figsize=(6,5))
        df.plot(kind="pie", ylabel="", autopct='%1.1f%%')

        # ✅ Ensure folder exists
        chart_dir = os.path.join(base_dir, "static", "Chart")
        os.makedirs(chart_dir, exist_ok=True)

        save_path = os.path.join(chart_dir, "frequency_pie.png")

        plt.savefig(save_path)
        plt.close()

        return "Chart created successfully"

    except Exception as e:
        return str(e)