
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

phone_number = phonenumbers.parse("Enter mobile number")

print(geocoder.description_for_number(phone_number, 'en'))

print(carrier.name_for_number(phone_number, 'en'))

print(timezone.time_zones_for_number(phone_number))

print("Final")
print("Final1")
print("Final2")
print("Final3")
print("Final54")