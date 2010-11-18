# -*- coding: utf-8 -*-

from tv1.blob.support.migration.chamada import migrateChamada, getChamadaMigrationWalker

from tv1.blob.support.browser.base import BlobMigrationView


class ChamadaMigrationView(BlobMigrationView):

    migration = migrateChamada
    walker = getChamadaMigrationWalker


