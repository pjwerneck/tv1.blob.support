# -*- coding: utf-8 -*-

from tv1.blob.support.migration.newsitem import migrateNewsItem, getNewsItemMigrationWalker
from tv1.blob.support.browser.base import BlobMigrationView



class NewsItemMigrationView(BlobMigrationView):

    migration = migrateNewsItem
    walker = getNewsItemMigrationWalker


