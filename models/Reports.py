from .db import DatabaseManager,DatabaseError
from utility import Dates

class Reports:
    @staticmethod
    def get_service_count_income(db:DatabaseManager,service_id,start_date,end_date):
        query = f"""
                SELECT 
                    COUNT(*) AS services_count,
                    SUM(price) AS total_income
                FROM 
                    MedicalRecords
                WHERE 
                    service = {service_id}
                    AND greg_date BETWEEN '{start_date}' AND '{end_date}';
                """
        try:
            return db.fetchone(query)
        except DatabaseError as e:
            raise e
        
    @staticmethod
    def get_most_sold_service_dates(db:DatabaseManager,service_id,start_date,end_date):
        query = f"""
                SELECT jalali_date, COUNT(*) as sold_count
                FROM MedicalRecords
                WHERE service = {service_id} 
                AND greg_date BETWEEN '{start_date}' AND '{end_date}'
                GROUP BY greg_date
                ORDER BY sold_count DESC
                LIMIT 4;
                """

        try:
            return db.fetchall(query)
        except DatabaseError as e:
            raise e
        
    @staticmethod
    def get_current_month_service_income_by_days(db:DatabaseManager,service_id):
        start_date,end_date = Dates.get_jalali_current_month_interval_based_on_greg()

        query = f"""
                SELECT jalali_date, SUM(price) AS income
                FROM MedicalRecords
                WHERE service = {service_id} 
                AND greg_date BETWEEN '{start_date}' AND '{end_date}'
                GROUP BY greg_date
                ORDER BY greg_date DESC
                """

        try:
            return db.fetchall(query)
        except DatabaseError as e:
            raise e

    def get_monthly_service_income(db: DatabaseManager, service_id, start_date,end_date):
        query = f"""
                SELECT 
                    COUNT(*) AS services_count,
                    SUM(price) AS total_income
                FROM 
                    MedicalRecords
                WHERE 
                    service = {service_id}
                    AND greg_date BETWEEN '{start_date}' AND '{end_date}';
                """
        try:
            return db.fetchone(query)
        except DatabaseError as e:
            raise e
