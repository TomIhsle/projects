# From: https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts/python#analyze-an-image-with-computer-vision-api-using-python-a-nameanalyzeimage-a

########### Python 2.7 #############
import httplib, urllib, base64, json
import os
import sys

###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key.
subscription_key = os.getenv("AZURE_COMPUTER_VISION_KEY")

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
# uri_base = 'westcentralus.api.cognitive.microsoft.com'
uri_base = os.getenv("AZURE_COMPUTER_VISION_REGION_URI")

headers = {
    # Request headers.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = urllib.urlencode({
    # Request parameters. All of them are optional.
    'visualFeatures': 'Categories,Description,Color',
    'language': 'en',
})

# The URL of a JPEG image to analyze.
url = sys.argv[1]
print url
body = '{"url":"' + url + '"}'

try:
    # Execute the REST API call and get the response.
    conn = httplib.HTTPSConnection(uri_base)
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()

    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(data)
    print ("Response:")
    print (json.dumps(parsed, sort_keys=True, indent=2))
    conn.close()

except Exception as e:
    print('Error:')
    print(e)

####################################