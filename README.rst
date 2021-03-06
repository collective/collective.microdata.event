Introduction
============

Install this package and get an alternative version of event view in your Plone site. Changes are minimal,
just to add basic HTML 5 `microdata`__ information, taken from `schema.org`__ specification.

__ http://en.wikipedia.org/wiki/Microdata_%28HTML%29
__ http://www.schema.org/Event

.. image:: http://keul.it/images/plone/collective.microdata/collective.microdata.event-0.2-01.png
   :alt: Event view with microdata tool enabled

Microdata available in Web pages can be used from search engines, enhancing the quality of information indexed.

This package is a proper implementation of the `collective.microdata.core`__ product. Read it's documentation
for more information.

__ https://github.com/keul/collective.microdata.core

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
    Taken from the difference from end and start date

__ http://www.schema.org/Person

Support for folder content listing views
----------------------------------------

This package supports also `collective.microdata.contentlisting`__ but not depends on it
(you have to manually install that add-on yourself).

__ https://github.com/keul/collective.microdata.contentlisting

Then you will be able to provide microdata information about events also when listing folders content.

.. image:: http://keul.it/images/plone/collective.microdata/collective.microdata.event-0.2-02.png
   :alt: Events and other contents in folder listing view

See it's documentation for knowing what views are supported.

Final notes
===========

Providing microdata doesn't ensure that search engines will use it.
