# -*- coding: utf8 -*-

from plone.indexer.decorator import indexer
from Products.ATContentTypes.interfaces import IATEvent

@indexer(IATEvent)
def getRemoteUrl(object, **kw):
    return object.event_url()
