#pip install randfacts

import randfacts as rf 

def fact():
    x = rf.get_fact()
    info = "Did you know that " + x
    return info
