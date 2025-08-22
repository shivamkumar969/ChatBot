# Create a Captcha image
from captcha.image import ImageCaptcha
from flask import session
import random
import string
def get_random_code():
    # all_chars=string.ascii_letters+string.digits # this line generate captcha mix of alphanumeric
    all_chars=string.digits
    length=random.randint(3,5)
    random_code="".join(random.sample(all_chars,length))
    return random_code


def create_captcha():
    img=ImageCaptcha()
    code=get_random_code()
    fcode=get_random_code()
    # print(code)
    # Store captcha session
    session["code"]=code
    pic_name=fcode+"_captcha.png"
    # code to generate randum charector
    img.write(code,"static/captcha_file/"+pic_name)
    return pic_name
