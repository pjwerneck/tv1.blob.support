.. contents:: Table of Contents
   :depth: 2

tv1.blob.support
****************************************

Overview
--------

Requirements
------------

    - Plone >= 3.2.x (http://plone.org/products/plone)
    
Installation
------------
    
To enable this product,on a buildout based installation:

    1. Edit your buildout.cfg and add ``tv1.blob.support``
       to the list of eggs to install ::

        [buildout]
        ...
        eggs = 
            tv1.blob.support

    2. Tell the plone.recipe.zope2instance recipe to install a ZCML slug::

        [instance]
        ...
        zcml = 
            ...
            tv1.blob.support
    

If another package depends on the tv1.blob.support egg or 
includes its zcml directly you do not need to specify anything in the 
buildout configuration: buildout will detect this automatically.

After updating the configuration you need to run the ''bin/buildout'',
which will take care of updating your system.

Go to the 'Site Setup' page in the Plone interface and click on the
'Add/Remove Products' link.

Choose the product (check its checkbox) and click the 'Install' button.

Uninstall -- This can be done from the same management screen, but only
if you installed it from the quick installer.

Note: You may have to empty your browser cache and save your resource registries
in order to see the effects of the product installation.

Sponsoring
----------

Development of this product was sponsored by `Simples Consultoria 
<http://www.simplesconsultoria.com.br/>`_.


Credits
-------

    * Simples Consultoria (products at simplesconsultoria dot com dot br) - 
      Implementation
    
