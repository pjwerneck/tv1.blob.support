# -*- coding: utf-8 -*-

from tv1.blob.support.migration.superfile import migrateSuperFile, getSuperFileMigrationWalker

from tv1.blob.support.browser.base import BlobMigrationView

class SuperFileMigrationView(BlobMigrationView):

    migration = migrateSuperFile
    walker = getSuperFileMigrationWalker


