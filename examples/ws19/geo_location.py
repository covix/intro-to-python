import geoip2.database

reader = geoip2.database.Reader("./data/GeoLite2-City_20191001/GeoLite2-City.mmdb")


def printRecord(ip):
    # rec = gi.record_by_name(ip)
    response = reader.city(ip)

    city = response.city.name
    country = response.country.name
    longitude = response.location.longitude
    lat = response.location.latitude
    print(f"[+] Address: {ip} Geo-located")
    print(f"[+] {city}, {country}")
    print(f"[+] Latitude: {lat}, Longitude: {longitude}")


ip = int(input("Enter the IP: "))  # Enter an IP
printRecord(ip)
