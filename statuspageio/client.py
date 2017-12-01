from statuspageio.configuration import Configuration
from statuspageio.http_client import HttpClient
import statuspageio.services


class Client(object):
    """
    The :class:`Client <Client>` is the entry point to all services and actions.

    :attribute :class:`Configuration <basecrm.Configuration>` config: Current StatusPage.io client configuration.
    :attribute :class:`HttpClient <statuspageio.HttpClient>` http_client: Http client.

    :copyright: (c) 2016 by GameSparks Developers, and partial code by 2015, BaseCRM developers (developers@getbase.com).
    :license: MIT, see LICENSE for more details.
    """

    def __init__(self, **options):
        """
        Usage::

          >>> import os
          >>> import statuspageio
          >>> client = statuspageio.Client(api_key='<YOUR_PERSONAL_API_KEY>', page_id=<YOUR_PERSONAL_PAGE_ID')
          <statuspageio.Client>


        :param str access_token: Personal access token.
        :param str base_url: (optional) Base url for the api. Default: ``https://api.getbase.com``.
        :param str user_agent: (optional) Client user agent. Default: ``statuspageio/v1 Python/{basecrm.VERSION}``.
        :param bool verbose: (optional) Verbose/debug mode. Default: ``False``.
        :param int timeout: (optional) Connection and response timeout. Default: **30** seconds.
        :param bool verify_ssl: (optional) Whether to verify ssl or not. Default: ``True``.

        :raises ConfigurationError: if no ``access_token`` provided.
        :raises ConfigurationError: if provided ``access_token`` is invalid - contains disallowed characters.
        :raises ConfigurationError: if provided ``access_token`` is invalid - has invalid length.
        :raises ConfigurationError: if provided ``base_url`` is invalid.
        """

        self.config = Configuration(**options)
        self.config.validate()

        self.http_client = HttpClient(self.config)
        self.organization_id = self.config.organization_id

        
        self.__pages = statuspageio.services.PageService(self.http_client, self.config.page_id)
        self.__components = statuspageio.services.ComponentsService(self.http_client, self.config.page_id)
        self.__incidents = statuspageio.services.IncidentsService(self.http_client, self.config.page_id)
        self.__subscribers = statuspageio.services.SubscribersService(self.http_client, self.config.page_id)
        self.__metrics = statuspageio.services.MetricsService(self.http_client, self.config.page_id)
        self.__users = statuspageio.services.UsersService(self.http_client,self.organization_id)


    @property
    def pages(self):
        return self.__pages
    
    @property   
    def components(self):
        return self.__components
    
    @property   
    def incidents(self):
        return self.__incidents
    
    @property
    def subscribers(self):
        return self.__subscribers
        
    @property
    def metrics(self):
        return self.__metrics
    
    @property
    def users(self):
        return self.__users