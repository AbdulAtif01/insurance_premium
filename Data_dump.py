import pymongo
import pandas as pd
import numpy as np
import json

client = pymongo.MongoClient("mongodb+srv://AAtif:Abdul-Atif-01@a.qkdfdsc.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = (r"C:\Users\admin\Insurance_premium\insurance.csv")
DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"


if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    df.reset_index(drop = True, inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)