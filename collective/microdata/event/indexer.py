# -*- coding: utf8 -*-

from plone.indexer.decorator import indexer
from Products.ATContentTypes.interfaces import IATEvent
from collective.microdata.core.interfaces import IMicrodataVocabulary

@indexer(IATEvent)
def microdata_itemtype(object, **kw):
    adapter = IMicrodataVocabulary(object)
    return adapter.microdata_vocabulary
