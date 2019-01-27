# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 16:37:09 2018

@author: ASUS
"""

def leap_year(year):
    # 1700,1800,1900 is divisible by 4 but not a leap year
    if year%4 != 0:
        return False
    elif year%100 != 0:
        return True
    elif year%400 != 0:
        return False
    else:
        return True
 
def day_of_week_jan1(year):
    # a must be from 0 to 6 inclusive.
    a = (1 + 5*((year - 1)%4) + 4*((year - 1)%100) + 6*((year-1)%400))%7
    return(a)

def num_days_in_month(month_num, leap_year):
    # month_num value must be from 1-12 inclusive.
    norm_year = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if leap_year == False:
        return (norm_year[month_num])
    else:
        if month_num == 2:
            return 29
        else:
            return (norm_year[month_num])

def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    result = [month_names[month_num - 1]]
    day_of_the_week = first_day_of_month
    day_of_the_month = 1
    
    week = "   " * first_day_of_month
    
    while day_of_the_month <= num_days_in_month:
        if day_of_the_week <= 6:
            week = week + "{:>3s}".format(str(day_of_the_month))
            day_of_the_month += 1
            day_of_the_week += 1
        else:
            result.append(week)
            week = ""
            day_of_the_week = 0
    result.append(week)
    
    return result
 
def construct_cal_year(year):
    result = [year]
    
    is_leap_year = leap_year(year)
    first_day = day_of_week_jan1(year)
    
    for i in range(1,13):
        num_days = num_days_in_month(i, is_leap_year)
        result.append(construct_cal_month(i, first_day, num_days))
        first_day = (first_day + num_days) % 7
        
    return result
    
def display_calendar(year):
    #format calendar display
    result = ''
    data = construct_cal_year(year)
    data.pop(0)
    #data[0:1] = []
    
    for month in range(12):
        for week in range(len(data[month])):
            result = result + data[month][week] + "\n"
            if week == 0:
                result = result + "  S  M  T  W  T  F  S\n"
        if month != 11:
            result = result + "\n"
    
    return result.strip()

def display_calendar_and_month(year, months = 0):
    if months != 0:
        #format calendar display
        result = ''
        data = construct_cal_year(year)


        for week in range(len(data[months])):
            result = result + data[months][week] + "\n"
            if week == 0:
                result = result + "  S  M  T  W  T  F  S\n"

        return result.strip()
    
    else:
        #format calendar display
        result = ''
        data = construct_cal_year(year)
        data.pop(0)
        #data[0:1] = []
    
        for month in range(12):
            for week in range(len(data[month])):
                result = result + data[month][week] + "\n"
                if week == 0:
                    result = result + "  S  M  T  W  T  F  S\n"
            if month != 11:
                result = result + "\n"
        
        return result.strip()

print(display_calendar_and_month(2100))