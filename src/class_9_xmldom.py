from xml.dom import minidom

doc =  minidom.parse("sample_xml.xml")

ads = doc.getElementsByTagName("ad")
for ad in ads:
    print("Year is",ad.getElementsByTagName("year")[0].firstChild.data)
    print("Model is", ad.getElementsByTagName("model")[0].firstChild.data)
    print("Color is", ad.getElementsByTagName("color")[0].firstChild.data)
    print("Description is", ad.getElementsByTagName("description")[0].firstChild.data)
    print("Seller is", ad.getElementsByTagName("seller")[0].firstChild.data)
    print("Seller phone no is",ad.getElementsByTagName("seller")[0].getAttribute("phone"))
    print("Seller email id is", ad.getElementsByTagName("seller")[0].getAttribute("email"))
    print("city is", ad.getElementsByTagName("location")[0].getElementsByTagName("city")[0].firstChild.data)
    print("state is", ad.getElementsByTagName("location")[0].getElementsByTagName("state")[0].firstChild.data)
    print("-"*50)