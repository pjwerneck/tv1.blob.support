# -*- coding: utf-8 -*-

from plone.app.blob.migrations import ATFileToBlobMigrator, getMigrationWalker, migrate

# migration of image content to image replacement content type
class NewsItemToBlobImageMigrator(ATFileToBlobMigrator):
    src_portal_type = 'News Item'
    src_meta_type = 'ATNewsItem'
    dst_portal_type = 'News Item'
    dst_meta_type = 'ATNewsItem'

    # migrate all fields except 'image', which needs special handling...
    fields_map = {
        'image': None,
    }

    def migrate_data(self):
        #import pdb; pdb.set_trace()
        #self.new.getField('text').getMutator(self.new)(self.old.getField('text').get(self.old), text_format='text/html')

        self.new.getField('text').setContentType(self.new, 'text/html')

        
        if self.old.schema['image']:
            oldfield = self.old.schema['image']
            value = oldfield.get(self.old)
                
            if value:
                self.new.getField('image').getMutator(self.new)(value)
                if hasattr(oldfield, 'removeScales'):
                    # clean up old image scales
                    oldfield.removeScales(self.old)

            

def getNewsItemMigrationWalker(self):
    return getMigrationWalker(self, migrator=NewsItemToBlobImageMigrator)

def migrateNewsItem(self):
    return migrate(self, walker=getNewsItemMigrationWalker)


