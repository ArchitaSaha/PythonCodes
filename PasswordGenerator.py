print(ord('A'), ord('Z'), ord('a'), ord('z'), ord('0'), ord('9'))
# Special Characters(32–47 / 58–64 / 91–96 / 123–126):

import random

upper = chr(random.randint(65, 90))
lower = chr(random.randint(97, 122))
number = chr(random.randint(48, 57))


import base64
print(base64.b64encode("string".encode()))