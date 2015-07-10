#!/usr/bin/env python3

import datetime
import hashlib
import time

title = input("Enter the title of the ePub: ")
ts = time.time()

tstring = "{0}, dcterms:modified, {1}".format(title, ts)
tbytes = tstring.encode("utf-8")
#tsha1 = hashlib.sha1(tbytes)
tsha256 = hashlib.sha256(tbytes)
thex = tsha256.hexdigest()
thid = thex.upper()
tmod = datetime.datetime.utcfromtimestamp(ts).isoformat()[0:19]

print("""Enter the following data into ePub metadata:

{0}
{1}

<dc:identifier id="pub-id">urn:sha256:{0}</dc:identifier>
<meta refines="#pub-id" property="identifier-type" scheme="xsd:string">sha256</meta>
<meta property="dcterms:modified">{1}Z</meta>

""".format(thid, tmod))
