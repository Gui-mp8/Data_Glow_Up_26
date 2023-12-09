from load.tables_spark import Customers


def main():
    Customers().load_data()


if __name__ == "__main__":
    main()
