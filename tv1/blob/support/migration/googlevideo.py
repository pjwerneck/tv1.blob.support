# -*- coding: utf-8 -*-

from plone.app.blob.migrations import ATFileToBlobMigrator, getMigrationWalker, migrate

# migration of image content to image replacement content type
class GoogleVideoToBlobImageMigrator(ATFileToBlobMigrator):
    src_portal_type = 'Google Video'
    src_meta_type = 'ATGoogleVideo'
    dst_portal_type = 'Google Video'
    dst_meta_type = 'ATGoogleVideo'

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

            

def getGoogleVideoMigrationWalker(self):
    return getMigrationWalker(self, migrator=GoogleVideoToBlobImageMigrator)

def migrateGoogleVideo(self):
    return migrate(self, walker=getGoogleVideoMigrationWalker)


