from abc import ABC, abstractmethod

from pyspark.sql import SparkSession
from pyspark.sql import DataFrame

import findspark


class DataLoader(ABC):
    def __init__(self) -> None:
        self.findspark = findspark.init()
        self.spark = (
            SparkSession.builder.appName("load_tables")
            .config("spark.jars", "src/drivers/postgresql-42.5.0.jar")
            .getOrCreate()
        )

    @abstractmethod
    def read_csv(self) -> DataFrame:
        pass

    @abstractmethod
    def load_data(self) -> None:
        pass
