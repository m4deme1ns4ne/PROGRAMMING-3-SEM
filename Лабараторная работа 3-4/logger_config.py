# logger_config.py

import logging

# Create custom logger
logger = logging.getLogger

main_logger = logging.getLogger('main')
gen_bin_tree_logger = logging.getLogger('gen_bin_tree')

# Set the log level
main_logger.setLevel(logging.DEBUG)
gen_bin_tree_logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('app.log')
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

# Create formatters and add it to handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the loggers
main_logger.addHandler(console_handler)
main_logger.addHandler(file_handler)
gen_bin_tree_logger.addHandler(console_handler)
gen_bin_tree_logger.addHandler(file_handler)
