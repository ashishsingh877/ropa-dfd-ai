import pandas as pd

def parse_ropa(file):

    df = pd.read_excel(file)
    text = ""

    for _,row in df.iterrows():
        text += f'''
Process: {row.get("Process Name","")}
Source: {row.get("Source","")}
System: {row.get("System","")}
Recipient: {row.get("Recipient","")}
Purpose: {row.get("Purpose","")}
Data: {row.get("Personal Data","")}
'''
    return text