import logging

def get_logger():
    logger = logging.getLogger("API_TEST")
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler("test.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger