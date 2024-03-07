from pymongo import  MongoClient
from .mongo_db_config import mongo_db_infos

class DBConnectionHandler:
  def __init__(self) -> None:
    self.__connection_string = f'mongodb://{mongo_db_infos["HOST"]}:{mongo_db_infos["PORT"]}/'
    self.__db_name = mongo_db_infos["DB_NAME"]
    self.__client = None
    self.__db_connection = None  

  def connect_to_db(self):
    self.__client =  MongoClient(self.__connection_string)
    self.__db_connection = self.__client[self.__db_name]

  def get_db_connection(self):
    return self.__db_connection

  def get_db_client(self):
    return self.__client

