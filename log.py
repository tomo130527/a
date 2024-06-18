import logging

def setup_logger():
    # Create a custom logger
    logger = logging.getLogger(__name__)

    # Set the default log level (DEBUG will capture all levels of logging)
    logger.setLevel(logging.DEBUG)
    
    # Create a file handler
    handler = logging.FileHandler('log.log')
    handler.setLevel(logging.DEBUG)
    
    # Create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    # Add the file handler to the logger
    logger.addHandler(handler)
    
    return logger

# # Example usage:
# logger = setup_logger()
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')

# setup_logger().error("ErrMsg")
