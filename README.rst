python-statuspageio
==============

StatusPage.oi  API V1 library client for Python. Based on the documentaion from https://doers.statuspage.io/api/v1/

Provides most of the funcitonality for the http://statuspage.io api's via handy python code.


Installation
------------

Statuspageio package can be installed either via pip:

.. code:: bash

    $ pip install --upgrade statuspageio



You can install from the source code as well. First clone the repo and
then execute:

.. code:: bash

    $ python setup.py install

After installing, import ``statuspageio`` package:

.. code:: python

    import statuspageio

Usage
-----

.. code:: python

    import statuspageio

    # Then we instantiate a client (as shown below)

Build a client
~~~~~~~~~~~~~~

**Using this api without authentication gives an error**

.. code:: python

    client = statuspageio.Client(api_key='<YOUR_PERSONAL_API_KEY>', page_id=<YOUR_PERSONAL_PAGE_ID')
or
    client = statuspageio.Client(api_key='<YOUR_PERSONAL_API_KEY>', page_id=<YOUR_PERSONAL_PAGE_ID',organization_id=<YOUR_PERSONAL_ORGANIZATION_ID)


Client Options
~~~~~~~~~~~~~~

The following options are available while instantiating a client:

-  **api\_key**: Personal API Key
-  **page\_id**: Personal page id
-  **organization\_id**: Personal organization id, used for managing users.
-  **base\_url**: Base url for the api
-  **user\_agent**: Default user-agent for all requests
-  **timeout**: Request timeout
-  **verbose**: Verbose/debug mode

Architecture
~~~~~~~~~~~~

The library follows few architectural principles you should understand
before digging deeper. 1. Interactions with resources are done via
service objects. 2. Service objects are exposed as properties on client
instances. 3. Service objects expose resource-oriented actions. 4.
Actions return dictionaries that support attribute-style access, a la
JavaScript (thanks to Bunch and it's form Munch).

For example, to interact with components API you will use
``statuspageio.ComponentsService``, which you can get if you call:

.. code:: python

    client = statuspageio.Client(api_key='<YOUR_PERSONAL_API_KEY>', page_id=<YOUR_PERSONAL_PAGE_ID')
    client.components # statuspageio.ComponentsService

To retrieve list of resources and use filtering you will call ``#list``
method:

.. code:: python

    client = statuspageio.Client(api_key='<YOUR_PERSONAL_API_KEY>', page_id=<YOUR_PERSONAL_PAGE_ID')
    client.components.list() # list(dict|Munch)



Resources and actions
---------------------

Documentation for every action can be found in ``statuspageio/services.py``
file.


Tests
-----

Sorry. These need to be written. 


Thanks
------

Thank you to the BaseCRM development team who created the majority of the code for this project. 
We forked the code as the aritectural style worked really well for this project. 
Please see https://github.com/basecrm/basecrm-python for more details

Thank you so much!

License
-------

MIT

Bug Reports
-----------

Report `here <https://github.com/GameSparks/python-statuspageio/issues>`__.


