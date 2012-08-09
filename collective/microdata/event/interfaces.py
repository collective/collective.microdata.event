# -*- coding: utf8 -*-

from zope.interface import Interface
from zope import schema

from collective.microdata.core.interfaces import ISchemaOrgThing

class IMicrodataEventLayer(Interface):
    """Marker interface for the collective.microdata.event layer"""


class ISchemaOrgEvent(ISchemaOrgThing):
    """See http://schema.org/Event"""

    attendees = schema.Tuple(title=u'Attendees',
                             description=u'A person(s) attending the event',
                             required=False)

    duration = schema.TextLine(title=u"Duration",
                               description=u"The duration of the item (movie, "
                                           u"audio recording, event, etc.) in "
                                           u"ISO 8601 date format.",
                               required=False)

    startDate = schema.Datetime(title=u"Start date",
                                description=u"The start date and time of the event.",
                                required=True)

    endDate = schema.Datetime(title=u"End date",
                              description=u"The end date and time of the event.",
                              required=True)

    location = schema.TextLine(title=u"Location",
                               description=u"The location of the event or organization.",
                               required=False)

