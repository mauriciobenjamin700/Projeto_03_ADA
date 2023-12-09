from src.database.conection import bike_db
from src.management.add import *
from src.management.edit import *
from src.management.remove import *
from src.management.search import *
from src.utils.menu import *
from src.utils.presentation import *

def main():
    #conexão com o banco de dados
    conn = bike_db

    conn.close()
main()