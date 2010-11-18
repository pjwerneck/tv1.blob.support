# -*- coding: utf-8 -*-

from plone.app.blob.migrations import ATFileToBlobMigrator, getMigrationWalker, migrate

# migration of image content to image replacement content type
class SuperFileToBlobImageMigrator(ATFileToBlobMigrator):
    src_portal_type = 'SuperFile'
    src_meta_type = 'Super File'
    dst_portal_type = 'SuperFile'
    dst_meta_type = 'Super File'

    # migrate all fields except 'image', which needs special handling...
    fields_map = {
        'imagefield': None,
    }

    def migrate_data(self):
        if self.old.schema['imagefield']:
            oldfield = self.old.schema['imagefield']
            value = oldfield.get(self.old)
                
            if value:
                self.new.getField('imagefield').getMutator(self.new)(value)
                if hasattr(oldfield, 'removeScales'):
                    # clean up old image scales
                    oldfield.removeScales(self.old)

            

def getSuperFileMigrationWalker(self):
    return getMigrationWalker(self, migrator=SuperFileToBlobImageMigrator)

def migrateSuperFile(self):
    return migrate(self, walker=getSuperFileMigrationWalker)


