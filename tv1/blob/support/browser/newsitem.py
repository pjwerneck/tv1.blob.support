# -*- coding: utf-8 -*-

from plone.app.blob.migrations import haveContentMigrations

from plone.app.blob.browser.migration import BlobMigrationView
from tv1.blob.support.migration.newsitem import migrateNewsItem, getNewsItemMigrationWalker
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import PloneMessageFactory as _
from Products.Five import BrowserView
from Products.statusmessages.interfaces import IStatusMessage

class BlobMigrationView(BrowserView):

    #migration = migrateATFiles
    #walker = getATFilesMigrationWalker

    def __call__(self):
        context = aq_inner(self.context)
        request = aq_inner(self.request)
        walker = self.walker()
        options = dict(target_type=walker.src_portal_type)
        clicked = request.form.has_key
        portal_url = getToolByName(context, 'portal_url')()
        ttool = getToolByName(context, 'portal_types')
        fti = ttool.get(walker.dst_portal_type)
        #import pdb; pdb.set_trace()
        if not haveContentMigrations:
            msg = _(u'Please install contentmigrations to be able to migrate to blobs.')
            IStatusMessage(request).addStatusMessage(msg, type='warning')
            options = dict(nomigrations=42)
        elif clicked('migrate'):
            output = self.migration()
            # Only count actual migration lines
            lines = output.split('\n')
            count = len([l for l in lines if l.startswith('Migrating')])
            msg = _(u'blob_migration_info',
                default=u'Blob migration performed for ${count} item(s).',
                mapping={'count': count})
            IStatusMessage(request).addStatusMessage(msg, type='info')
            options = dict(count=count, output=output)
        elif clicked('cancel'):
            msg = _(u'Blob migration cancelled.')
            IStatusMessage(request).addStatusMessage(msg, type='info')
            request.RESPONSE.redirect(portal_url)
        else:
            options.update( dict(available=len(list(walker.walk()))))
        return self.index(**options)


class NewsItemMigrationView(BlobMigrationView):

    migration = migrateNewsItem
    walker = getNewsItemMigrationWalker


