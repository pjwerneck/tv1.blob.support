# -*- coding: utf-8 -*-

from plone.app.blob.migrations import ATFileToBlobMigrator, getMigrationWalker, migrate

# migration of image content to image replacement content type
class ArtistaToBlobImageMigrator(ATFileToBlobMigrator):
    src_portal_type = 'Artista'
    src_meta_type = 'Artista'
    dst_portal_type = 'Artista'
    dst_meta_type = 'Artista'

    # migrate all fields except 'image', which needs special handling...
    fields_map = {
        'image': None,
    }

    def migrate_data(self):
        if self.old.schema['image']:
            oldfield = self.old.schema['image']
            value = oldfield.get(self.old)
                
            if value:
                self.new.getField('image').getMutator(self.new)(value)
                if hasattr(oldfield, 'removeScales'):
                    # clean up old image scales
                    oldfield.removeScales(self.old)
            

def getArtistaMigrationWalker(self):
    return getMigrationWalker(self, migrator=ArtistaToBlobImageMigrator)


def migrateArtista(self):
    return migrate(self, walker=getArtistaMigrationWalker)


