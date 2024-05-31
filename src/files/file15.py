Re, Gr, Wh, Ye= '\033[1;31m', '\033[1;32m', '\033[1;37m', '\033[1;33m'
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

def main():
    # INPUT NUMBER PHONE
    User_phone = input(f"\n {Wh}Enter number target {Gr}Ex +39xxxx {Wh}: {Gr}")
    default_region = "TO"  
    # VARIABLE PHONENUMBERS
    parsed_number = phonenumbers.parse(User_phone, default_region) 
    region_code = phonenumbers.region_code_for_number(parsed_number)
    jenis_provider = carrier.name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "to")
    is_valid_number = phonenumbers.is_valid_number(parsed_number)
    is_possible_number = phonenumbers.is_possible_number(parsed_number)
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(
        parsed_number, default_region,with_formatting=True)
    number_type = phonenumbers.number_type(parsed_number)
    timezone1 = timezone.time_zones_for_number(parsed_number)
    timezoneF = ', '.join(timezone1)
    print(f"\n{Gr} SHOW INFORMATION PHONE NUMBERS\n")
    print(f" {Wh}Region Code     :{Gr} {region_code}")
    print(f" {Wh}Operator        :{Gr} {jenis_provider}")
    print(f" {Wh}Valid number    :{Gr} {is_valid_number}")
    print(f" {Wh}Possible number :{Gr} {is_possible_number}")
    print(f" {Wh}International   :{Gr} {formatted_number}")
    print(f" {Wh}Country code    :{Gr} {parsed_number.country_code}")
    print(f" {Wh}Local number    :{Gr} {parsed_number.national_number}")
    if number_type == phonenumbers.PhoneNumberType.MOBILE:
        print(f" {Wh}Type            :{Gr} mobile number")
    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        print(f" {Wh}Type            :{Gr} fixed-line number")
    else:
        print(f" {Wh}Type            :{Gr} unknown")