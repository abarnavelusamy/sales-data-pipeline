from config import OUTPUT_FILE
from logger import logger


def load_data(df):

    logger.info("Writing output file")

    df.to_csv(OUTPUT_FILE, index=False)

    logger.info(f"Output written to {OUTPUT_FILE}")