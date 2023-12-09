# import time
from pyspark.sql import DataFrame
from abstraction.data_load import DataLoader
from load.schemas.customers_schema import CustomersSchema

# start_time = time.time()


class Customers(DataLoader):
    def read_csv(self) -> DataFrame:
        return (
            self.spark.read.format("csv")
            .option("header", "true")
            .option("delimiter", ",")
            .schema(CustomersSchema().schema())
            .load("data/olist/olist_customers_dataset.csv")
        )

    def transform_data(self) -> DataFrame:
        df = self.read_csv()
        df = df.withColumn(
            colName="customer_zip_code_prefix",
            col=df["customer_zip_code_prefix"].cast("string"),
        )

        return df

    def load_data(self) -> None:
        return (
            self.transform_data()
            .write.format("jdbc")
            .option("url", "jdbc:postgresql://localhost:5432/olist")
            .option("driver", "org.postgresql.Driver")
            .option("dbtable", "customer")
            .option("user", "olist")
            .option("password", "postgresql")
            .mode("overwrite")
            .save()
        )


# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"Program execution time: {elapsed_time} seconds")
