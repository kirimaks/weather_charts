import requests
from scrapers.tools import get_http_proxy
from scrapers.tools import get_https_proxy
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_temp_sochicamera():
    url = "http://sochi.camera/temperatures/w_5578bdf8ea9f37d8c78a827d.json"

    while True:
        try:
            logging.debug("<<-- Make request -->>")
            proxies = {
                "http": get_http_proxy("plain"),
                "https": get_https_proxy("plain")
            }
            resp = requests.get(url, proxies=proxies, timeout=5)
        except:
            logging.warning("!!! Exception occured !!!")
        else:
            if resp.headers['Content-Type'] == 'application/json':
                logging.debug("Get some JSON, stop it...")
                break

    data = resp.json()
    first_key = sorted(data)[0]
    assert(first_key)

    print(data)

    return data[first_key]['water']


if __name__ == "__main__":
    buff = get_temp_sochicamera()
    print(buff)
