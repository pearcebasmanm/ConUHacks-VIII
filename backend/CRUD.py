from main import get_Collection, get_database

dbname = get_database()
collection_name = get_Collection()

def Insert(Datetime_Issued, Datetime_Requested, vehicule_type):
    document = {"Datetime_Issued": Datetime_Issued,
                "Datetime_Requested": Datetime_Requested,
                "vehicule_type" : vehicule_type}
    collection_name.insert_one(document)

def UpdateDatetime_Issued(NewDatetime_Issued, Datetime_Requested, vehicule_type):
    collection_name.update_one({"vehicule_type": vehicule_type, "Datetime_Requested": Datetime_Requested}, {"$set": {"Datetime_Issued": NewDatetime_Issued}})

def UpdateDatetime_Requested(Datetime_Issued, NewDatetime_Requested, vehicule_type):
    collection_name.update_one({"Datetime_Issued": Datetime_Issued, "vehicule_type": vehicule_type}, {"$set": {"Datetime_Requested": NewDatetime_Requested}})

def UpdateVehicle_type(Datetime_Issued, Datetime_Requested, NewVehicule_Type):
    collection_name.update_one({"Datetime_Issued": Datetime_Issued, "Datetime_Requested": Datetime_Requested}, {"$set": {"vehicule_type": NewVehicule_Type}})

def delete():
    return 0

def Search():
    return 0

def RetrieveAll():
    documents = collection_name.find()
    print("Documents in the collection:")
    for doc in documents:
        print(doc)