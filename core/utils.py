import random
import string

def rand_str(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))
