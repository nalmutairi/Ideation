import random
import string 


def code_generator(size = 6, chars = string.ascii_uppercase):
	return ''.join(random.choice(chars) for _ in range(size))