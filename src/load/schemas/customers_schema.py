from pyspark.sql.types import StringType, StructField, StructType


class CustomersSchema:
    def schema(self):
        return StructType(
            [
                StructField(name="customer_id", dataType=StringType()),
                StructField(name="customer_unique_id", dataType=StringType()),
                StructField(name="customer_zip_code_prefix", dataType=StringType()),
                StructField(name="customer_city", dataType=StringType()),
                StructField(name="customer_state", dataType=StringType()),
            ]
        )
