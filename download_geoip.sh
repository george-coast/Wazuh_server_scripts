#!/bin/bash

# URL to download the GeoLite2 City CSV zip file
URL="https://download.maxmind.com/app/geoip_download_by_token?date=20240927&edition_id=GeoLite2-City-CSV&suffix=zip&token=v2.local.vQfonZ0Vkiiwv_44iWvGLUceoz-_nnRWNqrkvzhuRrarHH4WfGlIeZqP-c77XsEhg2oWzmD0IoPpDj_SNwOlwg2mkG9bjmlPA-be9pFDgQh-fhDilP7Jl86ihtds_6iCmJ6zp4gPoMDoiDFlZQLIMnfrcMlQm2L-DK2SiBjoRo_55upToq2IlrGf69htJkTd5_3aI-g"

# Destination directory
DESTINATION="/"

# Download the file to the specified destination
wget -P "$DESTINATION" "$URL"
