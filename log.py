import os
import logging
from logging.handlers import RotatingFileHandler
import datetime


class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
            cls._instance._lg_instance = LG(*args, **kwargs)
        return cls._instance

    def log(self, message, level='info'):
        self._lg_instance.log(message, level)


class LG:
    def __init__(self, log_file='log.log', log_dir='logs', max_bytes=10*1024*1024, backup_count=5):
        self.log_dir = log_dir
        self.log_file = f"{self.get_today_date()}_{log_file}"
        self.log_path = os.path.join(self.log_dir, self.log_file)

        # Ensure the directory exists
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        # Set up the logger
        self.logger = logging.getLogger('customLogger')
        self.logger.setLevel(logging.DEBUG)

        # Set up the handler with rotation
        handler = RotatingFileHandler(self.log_path, maxBytes=max_bytes, backupCount=backup_count)
        handler.setLevel(logging.DEBUG)

        # Create a formatter that includes the timestamp
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # Add the handler to the logger
        self.logger.addHandler(handler)
        # self.initPrinting()

    def log(self, message, level='info'):
        if level.lower() == 'debug':
            self.logger.debug(message)
        elif level.lower() == 'info':
            self.logger.info(message)
        elif level.lower() == 'warning':
            self.logger.warning(message)
        elif level.lower() == 'error':
            self.logger.error(message)
        elif level.lower() == 'critical':
            self.logger.critical(message)
        else:
            self.logger.info(message)

    def get_today_date(self,day = 0):
        today = datetime.date.today()
        today = today + datetime.timedelta(days=day)
        return today.strftime("%Y-%m-%d")
    
    def initPrinting(self):
        self.log("This is a debug message.", "debug")
        self.log("This is an info message.", "info")
        self.log("This is a warning message.", "warning")
        self.log("This is an error message.", "error")
        self.log("This is a critical message.", "critical")



# # Example usage
# if __name__ == "__main__":
#     logger = Logger()

#     logger.log("This is a debug message.", "debug")
#     logger.log("This is an info message.", "info")
#     logger.log("This is a warning message.", "warning")
#     logger.log("This is an error message.", "error")
#     logger.log("This is a critical message.", "critical")
