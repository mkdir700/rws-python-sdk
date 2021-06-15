# -*- coding: utf-8 -*-
"""
Created on 2021/6/15 13:03
---------
@summary: 
---------
@author: mkdir700
@email:  mkdir700@gmail.com
"""
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class SearchOrderRequestParameter(BaseModel):
    orderProgressList: Optional[List[int]] = None
    subStatusIdList: Optional[List[int]] = None
    dataType: int
    startDatetime: datetime
    endDatetime: datetime
    orderTypeList: Optional[List[int]] = None
    settlementMethod: Optional[int] = None
    deliveryName: Optional[str] = None
    shippingDateBlankFlag: Optional[int] = None
    shippingNumberBlankFlag: Optional[int] = None
    searchKeywordType: Optional[int] = None
    searchKeyword: Optional[str] = None
    mailSendType: Optional[int] = None
    ordererMailAddress: Optional[str] = None
    phoneNumberType: Optional[int] = None
    phoneNumber: Optional[str] = None
    reserveNumber: Optional[str] = None
    purchaseSiteType: Optional[int] = None
    asurakuFlag: Optional[int] = None
    couponUseFlag: Optional[int] = None
    drugFlag: Optional[int] = None
    overseasFlag: Optional[int] = None
    PaginationRequestModel: Optional["PaginationRequestDataModel"] = None


class PaginationRequestDataModel(BaseModel):
    requestRecordsAmount: int
    requestPage: int
    SortModelList: List["SortModel"] = None


class SortModel(BaseModel):
    sortColumn: int
    sortDirection: int


class GetOrderRequestParameter(BaseModel):
    orderNumberList: List[str]
    version: int = 5


class GetPaymentRequestParameter(BaseModel):
    orderNumber: str
    version: int = 5
