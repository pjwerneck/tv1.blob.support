
from archetypes.schemaextender.field import ExtensionField
from plone.app.blob.field import ImageField as BlobImageField


class ExtensionImageBlobField(ExtensionField, BlobImageField):
    pass
