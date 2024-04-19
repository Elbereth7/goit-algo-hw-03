from random import sample

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
# Generating {quantity} random unique numbers from (min, max) range
    try:
        if min < 1:
            raise ValueError(f"Invalid min value: {min}. Value can't be smaller then 1.")
        if max > 1000:
            raise ValueError(f"Invalid min value: {max}. Value can't be bigger then 1000.")
        
        result = sample(range(min, max), quantity)
        return sorted(result)
    except TypeError: # In case if any of the argument is entered in the incorrect format
        print('Invalid argument type. \n'
            f'Entered value {min}: required integer number from 1 to 1000, \n'
            f'entered value {max}: required integer number from 1 to 1000, \n'
            f'entered value {quantity}: required integer number.')
    except ValueError as ve: 
    # In case if argument format is correct, but value does not fullfull
    # the conditions. Customised value conditions:
    # - min must be an integer number not smaller then 1
    # - max must be an integer number not bigger then 1
    # Generic function conditions:
    # - max can't be smaller then min
        print(ve)

if __name__ == '__main__':
    lottery_numbers = get_numbers_ticket(12, 76, 6)
    print("Ваші лотерейні числа:", lottery_numbers)
