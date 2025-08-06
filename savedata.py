# import pandas as pd
# from flask import session
# def saved_enquiry():
#     epath="static/data_base/enquiry_data"
#     result_df=pd.read_excel(epath+"/Enquiry_Data_Base.xlsx")
#     # print(result_df)
#     new_row={"Name":session.get("enname"),"Email":session.get("enemail"),"Mobile":session.get("enmobile"),"Course":session.get("encourse"),"State":session.get("enstate"),"City":session.get("encity")}
#     new_row_df=pd.DataFrame([new_row])

#     new_row_df=pd.concat([result_df,new_row_df],ignore_index=True)

#     result_df.to_excel(epath+"/Enquiry_Data_Base.xlsx",index=False)
    
#     session.pop("enname",None)
#     session.pop("enemail",None)
#     session.pop("enmobile",None)
#     session.pop("encourse",None)
#     session.pop("enstate",None)
#     session.pop("encity",None)



import pandas as pd
from flask import session

def saved_enquiry():
    epath = "static/data_base/enquiry_data"
    file_path = f"{epath}/Enquiry_Data_Base.xlsx"
    
    try:
        result_df = pd.read_excel(file_path)
        
        new_row = {
            "Name": session.get("enname"),
            "Email_Id": session.get("enemail"),
            "Mobile": session.get("enmobile"),
            "Course": session.get("encourse"),
            "State": session.get("enstate"),
            "City": session.get("encity")
        }
        new_row_df = pd.DataFrame([new_row])

        # Combine the old and new data into a new DataFrame
        updated_df = pd.concat([result_df, new_row_df], ignore_index=True)

        # Save the UPDATED DataFrame to the excel file
        updated_df.to_excel(file_path, index=False)
        
        # Clear the session variables
        session.pop("enname", None)
        session.pop("enemail", None)
        session.pop("enmobile", None)
        session.pop("encourse", None)
        session.pop("enstate", None)
        session.pop("encity", None)
        
    except FileNotFoundError:
        print(f"ERROR: File not found at {file_path}. Please ensure the directory and file exist.")
    except Exception as e:
        print(f"An error occurred: {e}")