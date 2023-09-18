from Chicken_Disease_Classification import logger
from Chicken_Disease_Classification.pipeline.pipeline import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f" >>>> Running stage: {STAGE_NAME} started ...")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> Stage Name: {STAGE_NAME} >>>> completed!\n\nx ========= x")
except Exception as e:
    logger.exception(e)
    raise e

logger.info("Welconme to my custom log")

