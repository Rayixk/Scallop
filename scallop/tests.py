from django.test import TestCase

# Create your tests here.
import re
ss = """
<video id="media" autoplay="autoplay" width="680" height="500" controls=""> 
    <source src="http://y.syasn.com/p/p76.mp4"> <div>1234sdsdsd</div> </video><div>1234</div>cdscdsfsdfsdfsadfasdfga<h1>456</h1>

"""


res = re.findall(r'<div>(.*?)</div>|<h1>(.*?)</h1>',ss,re.S)
print(res)