

from zope.component import adapts
from zope.component import getUtility
from zope.interface import implements
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
from Products.Archetypes.public import ImageWidget
from Products.Archetypes.public import AnnotationStorage
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.ATContentTypes.configuration import zconf

from zope.publisher.interfaces import IPublishTraverse
from zope.publisher.interfaces.http import IHTTPRequest
from ZPublisher.BaseRequest import DefaultPublishTraverse
from Products.validation import V_REQUIRED


from zope.interface import Interface

from brasil.app.galeriadearte.interfaces import IArtista
from blobfield import ExtensionImageBlobField



class ArtistaExtender(object):
    adapts(IArtista)
    implements(ISchemaExtender)

    fields = [ExtensionImageBlobField('image',
                                      required=False,
                                      validators=('isNonEmptyFile'),
                                      ),
              ]

    def __init__(self, context):
        self.context = context

        
    def getFields(self):
        return self.fields
