# -*- coding: utf8 -*-

from Products.Five.browser import BrowserView
from collective.microdata.core.interfaces import ISchemaOrgThing

class EventView(BrowserView):
    
    def microdata(self):
        return ISchemaOrgThing(self.context)
