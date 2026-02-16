import logging
import os

def get_logger(name):

    os.makedirs("reports", exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        # 콘솔 출력
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # 파일 저장
        file_handler = logging.FileHandler("reports/test.log")
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
