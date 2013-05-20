import urllib
import xml.etree.ElementTree as ET
#Lets me use code from another library

APIKEY = '76VQAR-YVLL3LVRPV'
# This key let us acess wolfram alpha's server
WOLFRAMURL = 'http://api.wolframalpha.com/v2/query?input='
# url we acess

def wolfram(question):
    url = WOLFRAMURL + urllib.quote(question) + "&appid=" + APIKEY
    #sets up url that we are visiting.
    response = urllib.urlopen(url)
    #visits the url
    url_response = response.read()
    tree = ET.fromstring(url_response)
    #start to parse data wolfram gives us
    child = tree.findall('pod')[0] 
    #find all elements in the data with the name pod
    if 'input' in child.attrib.get('title').lower():
        child = tree.findall('pod')[1]
    #Sometimes the first result is the input, we don't want that
    #So we change it to the next result
    for sub_child in child.find('subpod'):
        answer = sub_child.get('title')
        #store the answer
    return '%s' % answer
    #prints answer out
def derive(function):
    string = wolfram('derive '+function)
    index = string.find('=')
    return string[(index+2):]
def integrate(function):
    string = wolfram('integrate '+function)
    index = string.find('=')
    string = string[(index+2):-len('constant')]+'C'
    return string
def evaluate(function, xval):
    string = wolfram('evaluate ' + function + ' for x=' + str(xval))
    if string.find('~') > -1:
        string = string[(string.find('~')+2):]
    return string
def taylor(function, nth, center):
    string = wolfram(str(nth)+'th taylor polynomial of ' + function + ' centered at '+str(center))
    return string
