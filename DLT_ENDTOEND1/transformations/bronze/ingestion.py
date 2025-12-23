import dlt 

#INGESTION SALES DATA 

@dlt.table(
    name = 'sales_bronze'
)
def sales_bronze():
    df = spark.readStream.format("cloudFiles") \
        .option("cloudFiles.format", "csv") \
        .load("/Volumes/databricksaman/bronze/bronze_volume/sales/")
    return df 

#INGESTION STORES DATA 

@dlt.table(
    name = 'stores_bronze'
)
def stores_bronze():
    df = spark.readStream.format("cloudFiles") \
        .option("cloudFiles.format", "csv") \
        .load("/Volumes/databricksaman/bronze/bronze_volume/stores/")
    return df 

#INGESTION PRODUCTS DATA 
@dlt.table(
    name = 'products_bronze'
)
def products_bronze():
    df = spark.readStream.format("cloudFiles") \
        .option("cloudFiles.format", "csv") \
        .load("/Volumes/databricksaman/bronze/bronze_volume/product/")
    return df 

#INGESTION customers DATA 
@dlt.table(
    name = 'customers_bronze'
)
def customers_bronze():
    df = spark.readStream.format("cloudFiles") \
        .option("cloudFiles.format", "csv") \
        .load("/Volumes/databricksaman/bronze/bronze_volume/customers/")
    return df 


