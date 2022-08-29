import re
patron1 = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)

mail = "3.3"
print(patron1.search(mail))




