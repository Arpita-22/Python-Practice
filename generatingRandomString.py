import random
import string

text = "".join(random.choice(string.ascii_letters + string.digits)for _ in range(10))

print(text)