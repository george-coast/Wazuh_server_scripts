import geoip2.database

# Path to the GeoIP database
db_path = '/var/ossec/etc/GeoIP.dat'

# Create a GeoIP reader
reader = geoip2.database.Reader(db_path)

# Test with an IPv6 address
ipv6_address = '2603:9000:e100:d6ba:90ec:2959:f907:66d5'
response = reader.city(ipv6_address)

print(f'Country: {response.country.name}')
print(f'Region: {response.subdivisions.most_specific.name}')
print(f'City: {response.city.name}')
print(f'Location: {response.location.latitude}, {response.location.longitude}')
