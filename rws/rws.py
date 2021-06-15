# -*- coding: utf-8 -*-
"""
Created on 2021/6/15 10:09
---------
@summary: 
---------
@author: mkdir700
@email:  mkdir700@gmail.com
"""
import base64

from requests import request
from requests.exceptions import HTTPError

from rws.utils.params import remove_empty_param_keys

__version__ = "0.0.1"
PAM_DEFAULT_TIMEOUT = 300


class RWS(object):
    """
    Base Rakuten API class
    """
    URI = '/'
    ENDPOINT = "https://api.rms.rakuten.co.jp"
    
    def __init__(self, secret, key, proxy, uri, headers=None):
        self.secret = secret
        self.key = key
        self.proxy = proxy
        self.uri = uri or self.URI
        if headers is not None:
            self.headers = {}
    
    def set_default_headers(self):
        """
        设置默认请求头
        :return:
        """
        sign = base64.b64encode(f'{self.secret}:{self.key}'.encode()).decode()
        return {
            'Authorization': sign,
            'Content-Type': 'application/json; charset=utf-8'
        }
    
    def make_request(self, action, params, method="POST", timeout=PAM_DEFAULT_TIMEOUT, **kwargs):
        """
        构造请求
        :param action: 操作类型
        :param params: 请求参数
        :param method: 请求方法，默认POST
        :param timeout: 超时时间
        :param kwargs: 其他参数
        :return:
        """
        params = params or {}
        request_params = params
        # Remove empty keys and clean values before transmitting
        request_params = remove_empty_param_keys(request_params)
        # request_params = clean_params_dict(request_params)
        headers = self.set_default_headers()
        self.headers.update(headers)
        self.headers.update(kwargs.get('extra_headers', {}))
        proxies = self.get_proxies()
        
        request_args = {
            "method": method,
            "url": self.endpoint(action),
            "headers": self.headers,
            "proxies": proxies,
            "timeout": timeout,
        }
        
        body = kwargs.get("body")
        if body:
            request_args["method"] = "POST"
            request_args["data"] = body
            request_args["params"] = request_params
        elif method == "POST":
            request_args["data"] = request_params
        else:
            request_args["params"] = request_params
        
        try:
            response = request(**request_args)
            response.raise_for_status()
        except HTTPError as exc:
            raise exc
        
        return response
        
    def get_proxies(self):
        """Return a dict of http and https proxies, as defined by `self.proxy`."""
        proxies = {"http": None, "https": None}
        if self.proxy:
            proxies = {
                "http": "http://{}".format(self.proxy),
                "https": "https://{}".format(self.proxy),
            }
        return proxies
    
    def endpoint(self, action):
        return "{}{}{}".format(self.ENDPOINT, self.uri, action)