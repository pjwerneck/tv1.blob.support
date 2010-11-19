# -*- coding: utf-8 -*-

from tv1.blob.support.migration.artista import migrateArtista, getArtistaMigrationWalker

from tv1.blob.support.browser.base import BlobMigrationView

class ArtistaMigrationView(BlobMigrationView):

    migration = migrateArtista
    walker = getArtistaMigrationWalker


