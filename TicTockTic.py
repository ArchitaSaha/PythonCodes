from google.cloud import storage
import os
import pandas as pd
import random
s = os.getcwd()

candidate_list = []
locations = []
activity = []
transport = []

class Candidate:
    name = None
    gender = None
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

def checkBoy(candidate):
    if candidate.gender == "M":
        return True
    return False

def checkGirl(candidate):
    if candidate.gender == "F":
        return True
    return False

def download_data(bucket_name, source_blob_name, destination_file_name,s):
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

def download_data_main():
    bucket_name = "function-bucket-cts02"
    source_blob_name = "Dataset.csv"
    destination_file_name = s+"/dataset.csv"
    download_data(bucket_name, source_blob_name, destination_file_name,s)

def makeDatabase():
    name = input("Enter the first name of the player :- ")
    gender = input("Enter the gender of {} in M/F format :- ".format(name))
    if gender == "M" or gender == "F":
        cand = Candidate(name, gender)
        candidate_list.append(cand)
        key = input("If you want to add more player press 1 else press any key to quit :- ")
        while key == "1":
            name = input("Enter the first name of the player :- ")
            gender = input("Enter the gender of {} in M/F format :- ".format(name))
            if gender == "M" or gender == "F":
                cand = Candidate(name, gender)
                candidate_list.append(cand)
            else:
                print("Invalid Input")
                return
            key = input("If you want to add more player press 1 else press q :- ")
        else:
            print("Invalid Input")
            return

def load_user_data():
    df = pd.read_csv("database.csv")
    l = len(df)
    name = list(df["Name"])
    gender = list(df["Gender"])
    for i in range(l):
        candidate_list.append(Candidate(name[i], gender[i]))

def load_other_data():
    df = pd.read_csv("dataset.csv")
    # print(df.head())
    locations[:] = [x for x in list(df["Locations"]) if x == x]
    activity[:] = [x for x in list(df["Activities"]) if x == x]
    transport[:] = [x for x in list(df["Transport"]) if x== x]

def stringGenerate(player):
    cand1= player
    cand2 = None
    location= locations[random.randint(0, len(locations) - 1)]
    activ= activity[random.randint(0, len(activity) - 1)]
    trans= transport[random.randint(0, len(transport) - 1)]

    if cand1.gender == "M":
        filterArr = list(filter(checkGirl, candidate_list))
        cand2 = filterArr[random.randint(0, len(filterArr) - 1)]
    else:
        filterArr = list(filter(checkBoy, candidate_list))
        cand2 = filterArr[random.randint(0, len(filterArr) - 1)]
    cand1 , cand2 = cand1.name, cand2.name
    
    print("{} and {} went to {} {} and {}.".format(cand1, cand2, location, trans, activ))


if __name__ == "__main__":
    name = input("Please Enter your Name :- ")
    gender = input("Enter your gender in M/F format :- ")
    player = Candidate(name, gender)
    k = input("If you want to create your own database press 1 and if you want to load predefined data press 2 :- ")
    if  k== "1":
        makeDatabase()
    elif k == "2":
        load_user_data()
    load_other_data()
    stringGenerate(player)