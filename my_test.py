# from ads_base.models import BaseAds
#
# print(BaseAds.objects.get(pk=1))
# a = BaseAds.objects.get(pk=1)
# a.on_delete

import requests

p = {
}

r = requests.put('http://127.0.0.1:8000/post/like/2', data = p)
print(r.content)
