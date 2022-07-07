import requests

proxies = {
   'http': 'http://127.0.0.1:8080',
   'https': 'http://127.0.0.1:8080',
}

# SOAP request URL
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

#read file
file = open("./soap.file", "r")

#read the contents of the file, this is the SOAP envelope
payload = file.read()

#close the file
file.close()

print(payload)

# structured XML
#payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
#            <soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
#                <soap:Body>
#                    <CountryIntPhoneCode xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
#                        <sCountryISOCode>IN</sCountryISOCode>
#                    </CountryIntPhoneCode>
#                </soap:Body>
#            </soap:Envelope>"""
# headers
headers = {
    'Content-Type': 'text/xml; charset=utf-8'
}
# POST request
response = requests.request("POST", url, headers=headers, data=payload, proxies=proxies)

# prints the response
print(response.text)
print(response)
