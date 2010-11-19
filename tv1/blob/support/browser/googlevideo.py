# -*- coding: utf-8 -*-

from tv1.blob.support.migration.googlevideo import migrateGoogleVideo, getGoogleVideoMigrationWalker

from tv1.blob.support.browser.base import BlobMigrationView

class GoogleVideoMigrationView(BlobMigrationView):

    migration = migrateGoogleVideo
    walker = getGoogleVideoMigrationWalker


