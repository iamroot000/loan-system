from .utils.postgresql import Database

class DBController:

    def __init__(self):
        self.db = Database('loansystemdb', 'postgres', '1234', 'localhost', '5432')

    def update_all_days_left(self,days_left, loan_id):
        try:
            self.db.connect()
            update_query = "UPDATE loan_loan_table SET days_left = %s WHERE loan_id = %s"
            self.db.cursor.execute(update_query, (days_left, loan_id))
            if self.db.cursor.rowcount != 0:
                self.db.conn.commit()
                self.db.close()
                return True
            self.db.conn.commit()
            self.db.close()
            return False
        except Exception as e:
            print(e)
            self.db.close()
            return False
        
    
    def get_all_data(self):
        
        self.db.connect()
        self.db.cursor.execute("SELECT * from loan_loan_table ")
        loan_table_list = self.db.cursor.fetchall()
        self.db.close()
        return loan_table_list
    
if __name__=="__main__":
    U = DBController()
    print(U.get_all_data())
    print(U.update_all_days_left(19, 692492))
    # print(U.update_all_days_left(19, 123444))