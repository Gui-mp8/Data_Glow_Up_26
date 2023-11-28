from database.tables import DataBase
# from etl.load import PostegresqlLoad
# from etl.transformation import PostgresqlTransformation
# from etl.extraction import PostgresqlExtraction
# from utils.config import load_config

def main():
    db = DataBase()
    db.conn = "postgresql://olist:postgresql@localhost:5432/olist"
    # db.conn = "postgresql://sicredi:postgresql@postgres/sicredi_data_challenge"
    print("Droping tables..")
    db.drop_table()
    print("Tables dropped!!! \nCreating Tables...")
    db.create_table()
    print("Tables Created!")

if __name__ == "__main__":
    main()