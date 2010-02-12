from zope.interface import Interface
import zope.schema
from zope.schema import Text
from zope.schema import TextLine
from zope.schema import Dict
from plone.portlets import interfaces


class ILayout(Interface):
    """ """

    title = TextLine(title=u"Layout title")
    description = Text(title=u"Layout description")
    icon = TextLine(title=u"Layout icon")
    image = TextLine(title=u"Layout image")

class IMrWigginLayer(Interface):
    """collective mrwiggin layer"""

class IPortletManager(interfaces.IPortletManager):
    pass
