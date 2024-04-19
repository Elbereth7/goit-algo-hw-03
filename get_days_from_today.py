from datetime import datetime

def get_days_from_today(date: str) -> int:
# This method is used to count the difference between the given date and current date in days

    try: # Required input type for date argument is string formatted as '%Y-%m-%d'
        given_date = datetime.strptime(date, '%Y-%m-%d').date() # Converting input to datetime object
        current_date = datetime.today().date() # Getting the current date
        difference = (given_date - current_date).days # Counting difference between the given and current date

    except (TypeError, ValueError): # Instructions in case data type or string format is incorrect
        print(f"Incorrect format of date: {date}. Please provide a date in 'YYYY-MM-DD' string format")
        difference = None # Dummy value to avoid the UnboundLocalError
        
    return difference

    
if __name__ == '__main__':

    date = '2024-04-01'
    print(get_days_from_today(date), type(get_days_from_today(date)))