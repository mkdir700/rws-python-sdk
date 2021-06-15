# -*- coding: utf-8 -*-
"""
Created on 2021/6/15 10:39
---------
@summary: 
---------
@author: mkdir700
@email:  mkdir700@gmail.com
"""
from rws import RWS
from rws.models.orders import (
    SearchOrderRequestParameter,
    GetOrderRequestParameter,
    GetPaymentRequestParameter
)


class Orders(RWS):
    """
    Rakuten Orders API
    """
    URI = "/es/2.0/order"
    
    def search_order(self, params: SearchOrderRequestParameter):
        """
        搜索订单
        :return:
        """
        data = params.dict()
        return self.make_request("searchOrder", data)
    
    def get_order(self, params: GetOrderRequestParameter):
        """
        获取订单详情
        :return:
        """
        data = params.dict()
        return self.make_request("getOrder", data)
    
    def get_payment(self, params: GetPaymentRequestParameter):
        """
        获取付款
        :return:
        """
        data = params.dict()
        return self.make_request("getOrder", data)
