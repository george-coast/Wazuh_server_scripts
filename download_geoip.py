import requests

# URL to download the GeoLite2 City CSV zip file
url = "https://download.maxmind.com/app/geoip_download_by_token?date=20240927&edition_id=GeoLite2-City-CSV&suffix=zip&token=v2.local.vQfonZ0Vkiiwv_44iWvGLUceoz-_nnRWNqrkvzhuRrarHH4WfGlIeZqP-c77XsEhg2oWzmD0IoPpDj_SNwOlwg2mkG9bjmlPA-be9pFDgQh-fhDilP7Jl86ihtds_6iCmJ6zp4gPoMDoiDFlZQLIMnfrcMlQm2L-DK2SiBjoRo_55upToq2IlrGf69htJkTd5_3aI-g"

# Destination path
destination = "/GeoLite2-City.zip"

# Download the file
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    with open(destination, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded successfully to {destination}")
else:
    print(f"Failed to download: {response.status_code}")
