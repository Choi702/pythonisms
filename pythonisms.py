from functools import wraps

def i_believe_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_val = func(*args, **kwargs)
        return f'Hitting The I Believe Button: "{original_val}"'
    return wrapper


def hard_being_a_believer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_val = func(*args, **kwargs)
        return f'I Still Have Not Experienced The AHA Moment Yet "{original_val}"'
    return wrapper

@i_believe_decorator
@hard_being_a_believer_decorator
def not_so_sure(txt):
    return txt




if __name__ == "__main__":
    print(not_so_sure('Getting A Little Worried, Not So Sure About The Button Just Yet!!'))
