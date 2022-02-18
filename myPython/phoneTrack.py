import phonenumbers
from phonenumbers import geocoder,carrier

def Number_detail(name):
    try:
        a=phonenumbers.parse('+91'+name,'CH')
        b=phonenumbers.parse('+91'+name,'RO')
        print('\n',carrier.name_for_number(b,'en'))
        print(geocoder.description_for_number(a,'en'),'\n')
    except Exception:
        print('\n***ENTER ONLY 10-DIGITS!!***\n')
if __name__=='__main__':
    name=input('\nENTER YOUR PHONE NO.:')
    Number_detail(name)
