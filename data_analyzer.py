import pandas as pd
def analyse(df):
    display(df.shape)
    summary = pd.DataFrame(df.dtypes, columns=["dtypes"]).reset_index()
    summary["Name"] = summary["index"]
    summary = summary[["Name", "dtypes"]]
    summary["Missing"] = df.isnull().sum().values
    summary["Miss_Percent"] = round((summary["Missing"]*100)/df.shape[0],0)
    summary["Unique"] = df.nunique().values
    summary["First Value"] = df.iloc[0].values
    summary["Second Value"] = df.iloc[1].values
    summary["Third Value"] = df.iloc[2].values
 
    return summary