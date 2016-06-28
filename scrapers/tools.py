import requests


def get_http_proxy(format):
    if format == "plain":
        return requests.get("https://mighty-ridge-44958.herokuapp.com/get_proxy/plain").text
    else:
        raise "NotImplemented"


def get_https_proxy(format):
    if format == "plain":
        return requests.get("https://mighty-ridge-44958.herokuapp.com/get_proxy/plain/https").text
    else:
        raise "NotImplemented"
