# -*- coding: utf8 -*-

from plone.indexer.decorator import indexer
from Products.ATContentTypes.interfaces import IATEvent
from collective.microdata.core.interfaces import IMicrodataVocabulary

@indexer(IATEvent)
def getRemoteUrl(object, **kw):
    return object.event_url()
