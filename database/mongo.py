import dotenv, os
import pymongo


dotenv.load_dotenv(dotenv.find_dotenv())

connect = pymongo.MongoClient(
    f"mongodb+srv://{os.getenv('username')}"
    f":{os.getenv('password')}"
    "@mdb.lfmebjg.mongodb.net/"
    "?retryWrites=true&w=majority"
)

cur = connect.test.stock
