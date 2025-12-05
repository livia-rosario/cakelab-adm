import psycopg2
import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

class Database:
    def __init__(self):
        self.host = os.getenv("SUPABASE_HOST")
        self.database = os.getenv("SUPABASE_DB")
        self.user = os.getenv("SUPABASE_USER")
        self.password = os.getenv("SUPABASE_PASSWORD")
        self.port = os.getenv("SUPABASE_PORT")
        
        self.connection = None

    def conectar(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port,
                sslmode="require"   
            )
            
            return self.connection
        
        except psycopg2.OperationalError as err:
            print(f"Erro ao conectar: {err}")
            return None
            
    def criar_connection(self):
        return self.conectar()
    
    def get_connection(self):
        return self.conectar()