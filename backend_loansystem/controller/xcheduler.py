from dao.loansystemdaoimpl import DBController
import logging
import datetime
import os

class DXcheduler():

    def __init__(self):
        self.__controll = DBController()
    
    def update(self):
        self._logger("INFO", self.__controll.get_all_data())
        for data in self.__controll.get_all_data():
            print(data[8])
        return True

    def _logger(self, level, message):
        logging.basicConfig(filename='logs/xcheduler.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        logger = logging.getLogger(__name__)
        if str(level).upper() == "DEBUG":
            return logger.debug(message)
        elif str(level).upper() == "INFO":
            return logger.info(message)
        elif str(level).upper() == "WARNING":
            return logger.warning(message)
        elif str(level).upper() == "ERROR":
            return logger.error(message)
        elif str(level).upper() == "CRITICAL":
            return logger.critical(message)
        else:
            return "Parameter Error Please Check Required Parameters"
        

    def _check_dir(self):
        log_dir = 'logs'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

if __name__=="__main__":
    X = DXcheduler()
    print(X.update())