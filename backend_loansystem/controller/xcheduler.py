from .dao.loansystemdaoimpl import DBController
import logging
import datetime
import os

#add checking of directory for logs
class DXcheduler():

    def __init__(self):
        self.__controll = DBController()
    
    def update(self):
        for data in self.__controll.get_all_data():
            due_date = data[8]
            loan_id = data[1]
            date_now = datetime.datetime.now()
            due_datetime = datetime.datetime.combine(due_date, datetime.time.min)
            days = (due_datetime - date_now).days
            if not (self.__controll.update_days_left(loan_id, days)):
                self._logger("ERROR", f'Failed to Update days_left field for loan_id={loan_id} please check!')
            self._logger("INFO", f'Successfully updated days_left field for loan_id={loan_id} to {days}.')
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