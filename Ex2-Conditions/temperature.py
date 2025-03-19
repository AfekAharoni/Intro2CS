#################################################################
# FILE : temperature.py
# WRITER : Afek Aharoni , afek.aharoni , 214143414
# EXERCISE : intro2cs ex2 2025
# DESCRIPTION: In this file there is one function that checks if at least 2 numbers are bigger than a treshold number
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES: None
#################################################################

def is_vormir_safe(treshold_temp, day1_temp, day2_temp, day3_temp):
    """
    This function check if at least 2 of these temperatures: day1_temp, day2_temp day3_temp
    are higher than treshold_temp, if so - the function returns True
    else - the function returns False
    The function doesn't use sort function
    """
    if (
        (day1_temp > treshold_temp and day2_temp > treshold_temp) or 
        (day1_temp > treshold_temp and day3_temp > treshold_temp) or
        (day2_temp > treshold_temp and day3_temp > treshold_temp)
    ):
        return True
    return False

