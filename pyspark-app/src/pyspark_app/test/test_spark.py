
def test_spark(init_spark):
    spark = init_spark
    df = spark.range(10)
    df.show()