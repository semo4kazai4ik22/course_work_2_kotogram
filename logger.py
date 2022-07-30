import logging

def create_logger():
    logger = logging.getLogger("basic") # создание логера
    logger.setLevel("DEBUG") # установка уровня

    file_handler = logging.FileHandler("basic.txt") # создание хэндлера
    logger.addHandler(file_handler) # добавить хэндлер к логгеру

    formatter = logging.Formatter("%(asctime)s : %(message)s")
    file_handler.setFormatter(formatter)

    return logger