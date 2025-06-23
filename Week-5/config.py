from dotenv import load_dotenv
import os

load_dotenv()  

SOURCE_DB = {
    'user': os.getenv('SOURCE_USER'),
    'password': os.getenv('SOURCE_PASSWORD'),
    'host': os.getenv('SOURCE_HOST'),
    'port': int(os.getenv('SOURCE_PORT')),
    'database': os.getenv('SOURCE_DATABASE')
}

DEST_DB = {
    'user': os.getenv('DEST_USER'),
    'password': os.getenv('DEST_PASSWORD'),
    'host': os.getenv('DEST_HOST'),
    'port': int(os.getenv('DEST_PORT')),
    'database': os.getenv('DEST_DATABASE')
}
