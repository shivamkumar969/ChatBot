import pandas as pd
from flask import session

def saved_message():
    epath = "static/data_base"
    file_path = f"{epath}/message_data.xlsx"
    
    try:
        result_df = pd.read_excel(file_path)
        
        new_row = {
            "Name": session.get("cname"),
            "Email_Id": session.get("cemail"),
            "Message":session.get("cmessage")
        }
        new_row_df = pd.DataFrame([new_row])

        # Combine the old and new data into a new DataFrame
        updated_df = pd.concat([result_df, new_row_df], ignore_index=True)

        # Save the UPDATED DataFrame to the excel file
        updated_df.to_excel(file_path, index=False)
        
        # Clear the session variables
        session.pop("cname", None)
        session.pop("cemail", None)
        session.pop("cmessage",None)
        
    except FileNotFoundError:
        print(f"ERROR: File not found at {file_path}. Please ensure the directory and file exist.")
    except Exception as e:
        print(f"An error occurred: {e}")