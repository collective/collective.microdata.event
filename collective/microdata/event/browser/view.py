# -*- coding: utf8 -*-

from Products.Five.browser import BrowserView
from collective.microdata.core.interfaces import IMicrodataVocabulary

class EventView(BrowserView):
    
    def microdata(self):
        return IMicrodataVocabulary(self.context)
