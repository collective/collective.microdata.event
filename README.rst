Introduction
============

Install this package and get an alternative version of event view in your Plone site. Changes are minimal, just to
add basic HTML 5 `microdata`__ information, taken from `schema.org`__ specification.

__ http://en.wikipedia.org/wiki/Microdata_%28HTML%29
__ http://www.schema.org/Event

Microdata available in Web pages can be used from search engines, enhancing the quality of information indexed.

Details
=======

Follow a list supported properties:

``name``
    Taken from event title
``description``
    Taken from the event description
``url``
    Taken from the event URL field
``attendees``
    Taken from Attendees field (raw data, not as `Person`__ elements)
``location``
    Taken from event location
``startDate``
    Taken from the start date
``endDate``
    Taken from the end date
``duration``
    Rendered in one of the ISO8601 formats, providing both start and end dates

__ http://www.schema.org/Person

Notes
-----

Providing microdata doesn't ensure that search engines will use them.
