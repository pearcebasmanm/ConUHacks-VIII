from ConectingDB import get_Collection, get_database
from bson.objectid import ObjectId

dbname = get_database()
collection_name = get_Collection()

def Insert(Datetime_Issued, Datetime_Requested, vehicule_type):
    document = {"Datetime_Issued": Datetime_Issued,
                "Datetime_Requested": Datetime_Requested,
                "vehicule_type" : vehicule_type}
    collection_name.insert_one(document)

def UpdateDatetime_Issued(ID, NewDatetime_Issued):
    collection_name.update_one({"_id": ID}, {"$set": {"Datetime_Issued": NewDatetime_Issued}})

def UpdateDatetime_Requested(ID, NewDatetime_Requested):
    collection_name.update_one({"_id": ID}, {"$set": {"Datetime_Requested": NewDatetime_Requested}})

def UpdateVehicle_type(ID, NewVehicule_Type):
    collection_name.update_one({"_id": ID}, {"$set": {"vehicule_type": NewVehicule_Type}})

def delete(ID):
    collection_name.delete_one({"_id": ID})
    
def SearchAllvehicule_type(vehicule_type):
    return collection_name.find({vehicule_type: vehicule_type})

def SearchbyID(ID):
    return collection_name.find_one({"_id": ID})

def RetrieveAll():
    documents = collection_name.find()
    print("Documents in the collection:")
    for doc in documents:
        print(doc)

if __name__ == "__main__":
    print(SearchbyID(ObjectId('65ac17d1d6e44d000ea4c295')))
    