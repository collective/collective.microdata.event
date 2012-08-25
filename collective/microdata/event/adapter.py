# -*- coding: utf8 -*-

import isodate

from zope.interface import implements

from collective.microdata.event.interfaces import ISchemaOrgEvent
from collective.microdata.core.adapter import ThingMicrodataProvider

class EventMicrodataProvider(ThingMicrodataProvider):
    implements(ISchemaOrgEvent)
    
    def __init__(self, content):
        super(EventMicrodataProvider, self).__init__(content)
        self.microdata_vocabulary = 'http://schema.org/Event'
        # must the event implements the event_url as "url"?
        self.url = content.event_url() or content.absolute_url()
        self.attendees = content.getAttendees()
        self.startDate = content.start().ISO8601()
        self.endDate = content.end().ISO8601()
        self.duration = isodate.duration_isoformat(content.end().asdatetime() - content.start().asdatetime()) 
        self.location = content.location


class EventMicrodataBrainProvider(object):
    implements(ISchemaOrgEvent)
    
    def __init__(self, brain):
        self.brain = brain
        self.microdata_vocabulary = 'http://schema.org/Event'
        # must the event implements the event_url as "url"?
        self.url = brain.getRemoteUrl or brain.getURL()
        self.startDate = brain.start.ISO8601()
        self.endDate = brain.end.ISO8601()
        self.duration = isodate.duration_isoformat(brain.end.asdatetime() - brain.start.asdatetime()) 
        self.location = brain.location
