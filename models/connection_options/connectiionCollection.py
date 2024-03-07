from models.connection_options.connections import DBConnectionHandler
from models.repository.minhaCollection_repository import MinhaCollectuionRepository
from bson.objectid import ObjectId



db_handler = DBConnectionHandler()
db_handler.connect_to_db()
db_connection = db_handler.get_db_connection()

minha_collection_repository = MinhaCollectuionRepository(db_connection)