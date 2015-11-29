# Counting Leave

Extend python datetime with excel-like leave count addition/subtraction
            functionality:
        
            COUNT_LEAVE(from_date,to_date,holidays)
        
            Returns the number of whole working days between from_date and
            to_date (inclusive of both from_date and to_date). Working days
            exclude weekends and any dates identified in holidays. Use COUNT_LEAVE
            to calculate employee benefits that accrue based on the number of
            days worked during a specific term.
        
            COUNT_WORKDAY(from_date,days,[holidays])
        
            Returns a number that represents a date that is the indicated number
            of working days before or after a date (the starting date). Working
            days exclude weekends and any dates identified as holidays. Use
            COUNT_WORKDAY to exclude weekends or holidays when you calculate invoice
            due dates, expected delivery times, or the number of days of work
            performed.
        
            This module has similarities with the BusinessHours module - you may
            want to check it out as well to see which one better fits your needs.
