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
        except Exception as e:
            error_msg = f"""
                واکشی اطلاعات گزارش قیمت و تعداد سرویس با خطا مواجه شده است.
                {str(e)}
            """      
            raise DatabaseError(error_msg)

        
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
        except Exception as e:
            error_msg = f"""
                واکشی پرفروش‌‌ترین سرویس‌ها با خطا مواجه شده است.
                {str(e)}
            """      
            raise DatabaseError(error_msg)

        
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
        except Exception as e:
            error_msg = f"""
                واکشی درآمد ماه جاری سرویس‌ با خطا مواجه شده است.
                {str(e)}
            """   
            raise DatabaseError(error_msg)

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
        except Exception as e:
            error_msg = f"""
                واکشی درآمد ماهانه سرویس‌ با خطا مواجه شده است.
                {str(e)}
            """   
            raise DatabaseError(error_msg)

    def get_financial_summary(db: DatabaseManager, start_date, end_date):
        query = f"""
                SELECT 
                    COALESCE((SELECT SUM(price) FROM MedicalRecords WHERE greg_date BETWEEN '{start_date}' AND '{end_date}'), 0) AS total_income,
                    COALESCE((SELECT SUM(price) FROM Expense WHERE greg_date BETWEEN '{start_date}' AND '{end_date}'), 0) AS total_expense,
                    COALESCE((SELECT SUM(price) FROM MedicalRecords WHERE greg_date BETWEEN '{start_date}' AND '{end_date}'), 0) -
                    COALESCE((SELECT SUM(price) FROM Expense WHERE greg_date BETWEEN '{start_date}' AND '{end_date}'), 0) AS profit 
                """
        try:
            return db.fetchone(query)
        except Exception as e:
            error_msg = f"""
                واکشی اطلاعات مالی با خطا مواجه شده است.
                {str(e)}
            """   
            raise DatabaseError(error_msg)

    def get_financial_summary_by_days(db: DatabaseManager, start_date, end_date):
        query = f"""
                SELECT 
                    dates.jalali_date,
                    COALESCE(SUM(MedicalRecords.price), 0) AS total_income,
                    COALESCE((SELECT SUM(price) FROM Expense WHERE greg_date = dates.greg_date), 0) AS total_expense,
                    COALESCE(SUM(MedicalRecords.price), 0) - 
                    COALESCE((SELECT SUM(price) FROM Expense WHERE greg_date = dates.greg_date), 0) AS profit
                FROM 
                    (SELECT jalali_date, greg_date FROM MedicalRecords
                    UNION
                    SELECT jalali_date, greg_date FROM Expense) as dates
                LEFT JOIN MedicalRecords ON MedicalRecords.greg_date = dates.greg_date
                WHERE dates.greg_date BETWEEN '{start_date}' AND '{end_date}'
                GROUP BY dates.greg_date
                ORDER BY dates.greg_date DESC
                """
        try:
            return db.fetchall(query)
        except Exception as e:
            error_msg = f"""
                واکشی اطلاعات مالی روزهای ماه با خطا مواجه شده است.
                {str(e)}
            """   
            raise DatabaseError(error_msg)

    @staticmethod    
    def get_service_usage_and_expenses_summary(db: DatabaseManager, start_date, end_date):
        query = f"""
                SELECT * FROM (
                    SELECT 
                        'service' AS type,
                        s.name AS name,
                        COUNT(m.service) AS rank
                    FROM 
                        MedicalRecords m
                    JOIN 
                        Service s ON m.service = s.id
                    WHERE 
                        m.greg_date BETWEEN '{start_date}' AND '{end_date}'
                    GROUP BY 
                        s.name
                    ORDER BY 
                        rank DESC
                    LIMIT 4
                ) 
                UNION ALL
                SELECT * FROM (
                    SELECT 
                        'expense' AS type,
                        e.name,
                        e.price AS rank
                    FROM 
                        Expense e
                    WHERE 
                        e.greg_date BETWEEN '{start_date}' AND '{end_date}'
                    ORDER BY 
                        rank DESC
                    LIMIT 4
                );
                """
        try:
            return db.fetchall(query)
        except Exception as e:
            error_msg = f"""
                واکشی پرفروش‌ترین خدمات و بالاترین‌ هزینه‌ها با خطا مواجه شده است.
                {str(e)}
            """   
            raise DatabaseError(error_msg)