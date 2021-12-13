#HELLO GUYS I AM PINKY .THIS IS TOOL FOR FIND IN WENSITE THAT XML RPC FILE IS OPNELY WITH (POST METHOD) IS AVAILABLE OR NOT 
#IF YOU HAVE LARGE AMOUNT OF URL AND YOU WANT TO CHECK XMLRPC FILE IS ENABLE OR NOT ?
#DEFINITLELY yOU WILL NOT GOING TO DO MANUALLY AND HERE YOU CAN USE THIS TOOL FOR DIG OUT 


#IF YOU GOT STATUS CODE IS 405 OR 403 THATS MEAN YOU XML RPC IS EXISTS 


import requests

 
urls = ["http://www.URL.com","http://URL.com","https://www.URL.be","http://www.URL.com","https://www. URL.com","https://www.URL.org","https://-URL.pl","http://URL.com","https://URL.com","https://URL.org","https://www.URL.com","https://www.URL.com","https://URL.com"]
for url in urls:
    xml_url = url+"/xmlrpc.php"
    req = requests.get(xml_url)
    print("................................................")

    print(req.status_code)
    st_code = req.status_code
    print(xml_url)
    if st_code == 405 or st_code == 403:
        print("xmlrpc present")
    else:
        print("no xmlrpc present")


