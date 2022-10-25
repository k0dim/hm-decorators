import datetime
import os

# Декоратор №1
def decorators_text(old_function):
    START_DIRECTIRY = os.getcwd()
    NAME_FILE = 'log.log'
    PATH = os.path.join(START_DIRECTIRY, NAME_FILE)
    def new_function(*args, **kwargs):
        old_date = datetime.datetime.today()
        result = old_function(*args, **kwargs)
        now_date = datetime.datetime.today()
        # print(f'{datetime.today()} => {old_function} => {args}')
        with open(PATH, 'a') as img_file:
            img_file.write(f'{datetime.datetime.today()} -- {now_date-old_date} -- {old_function} -- {args} -- {old_function(*args, **kwargs)}\n')
        return result
    return new_function

# Декоратор №2
def decorators_params(parameter):
    def decorators_text(old_function):
        def new_function(*args, **kwargs):
            old_date = datetime.datetime.today()
            result = old_function(*args, **kwargs)
            now_date = datetime.datetime.today()
            # print(f'{datetime.today()} => {old_function} => {args}')
            with open(parameter, 'a') as img_file:
                img_file.write(f'{datetime.datetime.today()} -- {now_date-old_date} -- {old_function} -- {args} -- {old_function(*args, **kwargs)}\n')
            return result
        return new_function
    return decorators_text