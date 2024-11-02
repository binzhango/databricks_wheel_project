import pytest
from pyspark.sql import SparkSession

@pytest.fixture
def init_spark():
    spark = (
        SparkSession.builder.master("local[*]")
        .appName("demo")
        .getOrCreate()
    )
    yield spark