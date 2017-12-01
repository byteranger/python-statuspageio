
from statuspageio.errors import ConfigurationError


class PageService(object):
    """
    :class:`statuspageio.PageService` is used by :class:`statuspageio.Client` to make
    actions related to Page resource.

    Normally you won't instantiate this class directly.
    """

    OPTS_KEYS_TO_PERSIST = ['name', 'url', 'notifications_from_email', ]

    def __init__(self, http_client, page_id):
        """
        :param :class:`statuspageio.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client
        self.container = 'page'
        self.page_id = page_id

    @property
    def http_client(self):
        return self.__http_client

    def get(self):
        """
        Get page details

        Gets page information
        If the specified page does not exist, the request will return an error


        :calls: ``get pages/{page_id}.json``
        :return: Dictionary that support attriubte-style access and represents updated Component resource.
        :rtype: dict
        """
        _, _, page = self.http_client.get('/pages/{page_id}.json'.format(self.page_id))

        return page

    def update(self, **kwargs):
        """
        Update page details

        Updates page information
        If the specified page does not exist, the request will return an error


        :calls: ``patch pages/{page_id}.json``
        :param dict **kwargs:  component attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Component resource.
        :rtype: dict
        """


        OPTS_KEYS_TO_PERSIST = [
            'name',
            'url',
            'notifications_from_email',
            'time_zone',
            'city',
            'state',
            'country',
            'subdomain',
            'domain',
            'layout',
            'allow_email_subscribers',
            'allow_incident_subscribers',
            'allow_page_subscribers',
            'allow_sms_subscribers',
            'hero_cover_url',
            'transactional_logo_url',
            'css_body_background_color',
            'css_font_color',
            'css_light_font_color',
            'css_greens',
            'css_oranges',
            'css_reds',
            'css_yellows']

        if not kwargs:
            raise Exception('attributes are missing')

        attributes = dict((k, v) for k, v in kwargs.iteritems()
                          if k in OPTS_KEYS_TO_PERSIST)

        page = self.http_client.patch('/pages/{page_id}.json'.format(self.page_id),
                                      container=self.container,
                                      body=attributes)

        return page

class ComponentsService(object):
    """
    :class:`statuspageio.ComponentsService` is used by :class:`statuspageio.Client` to make
    actions related to Components resource.

    Normally you won't instantiate this class directly.
    """

    OPTS_KEYS_TO_PERSIST = ['name', 'description', 'group_id', 'status']

    def __init__(self, http_client, page_id):
        """
        :param :class:`statuspageio.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client
        self.page_id = page_id
        self.container = 'component'

    @property
    def http_client(self):
        return self.__http_client

    def list(self):
        """
        List components

        Lists components and their information
        If the specified contact does not exist, the request will return an error


        :calls: ``get pages/{page_id}/components/{component_id}.json``
        :return: Dictionary that support attriubte-style access and represents updated Component resource.
        :rtype: dict
        """

        _, _, components = self.http_client.get(
            '/pages/{page_id}/components.json'.format(page_id=self.page_id))
        return components


    def create(self, **kwargs):
        """
        Create a component

        Creates component
        If the specified contact does not exist, the request will return an error


        :calls: ``post pages/{page_id}/components.json``
        :param dict **kwargs:  component attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Component resource.
        :rtype: dict
        """


        if not kwargs:
            raise Exception('attributes are missing')

        attributes = dict((k, v) for k, v in kwargs.iteritems()
                          if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, component = self.http_client.post(
            '/pages/{page_id}/components.json'.format(
                page_id=self.page_id), container=self.container, body=attributes)

        return component

    def delete(self, component_id):
        """
        Delete a component

        Deletes a component
        If the specified contact does not exist, the request will return an error


        :calls: ``delete pages/{page_id}/components/{component_id}.json``
        :param int component_id: Unique identifier of a component.
        :return: Dictionary that support attriubte-style access and represents updated Component resource.
        :rtype: dict
        """

        status_code, _, _ = self.http_client.delete(
            "/pages/{page_id}/components/{component_id}.json".format(
                page_id=self.page_id, component_id=component_id))
        return status_code


    def update(self, component_id, **kwargs):
        """
        Update a component

        Updates component information
        If the specified contact does not exist, the request will return an error


        :calls: ``patch pages/{page_id}/components/{component_id}.json``
        :param int component_id: Unique identifier of a component.
        :param dict **kwargs:  component attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Component resource.
        :rtype: dict
        """

        if not kwargs:
            raise Exception('attributes for Contact are missing')

        attributes = dict((k, v) for k, v in kwargs.iteritems()
                          if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, component = self.http_client.patch(
            "/pages/{page_id}/components/{component_id}.json".format(
                page_id=self.page_id, component_id=component_id), container='component', body=attributes)
        return component

class IncidentsService(object):
    """
    :class:`statuspageio.IncidentsService` is used by :class:`statuspageio.Client` to make
    actions related to Incidents resource.

    Normally you won't instantiate this class directly.
    """

    OPTS_KEYS_TO_PERSIST = ['name', 'description', 'group_id', 'status']

    def __init__(self, http_client, page_id):
        """
        :param :class:`statuspageio.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client
        self.page_id = page_id
        self.container = 'incident'

    @property
    def http_client(self):
        return self.__http_client

    def list(self):      
        """
        List all incidents

        :calls: ``get pages/{page_id}/incidents.json``
        :return: Dictionary that support attriubte-style access and represents updated Component resource.
        :rtype: dict
        """

        _, _, incidents = self.http_client.get(
            '/pages/{page_id}/incidents.json'.format(page_id=self.page_id))
        return incidents

    def list_unresolved(self):
        """
        List unresolved incidents

        :calls: ``get pages/{page_id}/incidents/unresolved.json``
        :return: Dictionary that support attriubte-style access and represents updated Component resource.
        :rtype: dict
        """

        _, _, incidents = self.http_client.get(
            '/pages/{page_id}/incidents/unresolved.json'.format(page_id=self.page_id))
        return incidents

    def list_scheduled(self):
        """
        List scheduled incidents

        :calls: ``get pages/{page_id}/incidents/scheduled.json``
        :return: Dictionary that support attriubte-style access and represents updated Component resource.
        :rtype: dict
        """
        _, _, incidents = self.http_client.get(
            '/pages/{page_id}/incidents/scheduled.json'.format(page_id=self.page_id))
        return incidents

    def create(self, **kwargs):
        """
        Create a incident

        :calls: ``post pages/{page_id}/incidents.json``
        :param dict **kwargs:  incident attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Component resource.
        :rtype: dict
        """

        OPTS_KEYS_TO_PERSIST = [
            'name',
            'status',
            'message',
            'wants_twitter_update',
            'impact_override',
            'component_ids']

        if not kwargs:
            raise Exception('attributes are missing')

        attributes = dict((k, v) for k, v in kwargs.iteritems()
                          if k in OPTS_KEYS_TO_PERSIST)

        _, _, component = self.http_client.post(
            '/pages/{page_id}/incidents.json'.format(
                page_id=self.page_id), container=self.container, body=attributes)

        return component

    def create_scheduled(self, **kwargs):
        """
        Create a scheduled incident

        :calls: ``post pages/{page_id}/incidents.json``
        :param dict **kwargs:  incident attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Component resource.
        :rtype: dict
        """

        OPTS_KEYS_TO_PERSIST = [
            'name',
            'status',
            'scheduled_for',
            'scheduled_until',
            'message',
            'wants_twitter_update',
            'scheduled_remind_prior',
            'scheduled_auto_in_progress',
            'scheduled_auto_completed',
            'impact_override',
            'component_ids']
        if not kwargs:
            raise Exception('attributes are missing')

        attributes = dict((k, v) for k, v in kwargs.iteritems()
                          if k in OPTS_KEYS_TO_PERSIST)

        _, _, incident = self.http_client.post(
            '/pages/{page_id}/incidents.json'.format(
                page_id=self.page_id), container=self.container, body=attributes)

        return incident

    def delete(self, incident_id):
        """
        Remove a incident

        :calls: ``delete pages/{page_id}/incidents.json``
        :return: status code
        :rtype: int
        """

        status_code, _, _ = self.http_client.delete(
            "/pages/{page_id}/incidents/{incident_id}.json".format(
                page_id=self.page_id, incident_id=incident_id))
        return status_code 

    def update(self, incident_id, **kwargs):
        """
        Update a incident

        Updates incident information

        NOTE: if either of status or message is modified, a new incident update will be generated.
        You should update both of these attributes at the same time to avoid two separate incident
        updates being generated.
        :param dict **kwargs:  incident attributes to update.
        :calls: ``patch /pages/[page_id]/incidents/[incident_id].json``
        :return: Status code
        :rtype: string

        """
        OPTS_KEYS_TO_PERSIST = [
            'name',
            'status',
            'message',
            'wants_twitter_update',
            'impact_override',
            'component_ids']

        if not kwargs:
            raise Exception('attributes for Contact are missing')

        attributes = dict((k, v) for k, v in kwargs.iteritems()
                          if k in OPTS_KEYS_TO_PERSIST)

        _, _, component = self.http_client.patch(
            "/pages/{page_id}/incidents/{incident_id}.json".format(
                page_id=self.page_id, incident_id=incident_id), container=self.container, body=attributes)
        return component

class SubscribersService(object):
    """
    :class:`statuspageio.SubscribersService` is used by :class:`statuspageio.Client` to make
    actions related to Subscriber resource.

    Normally you won't instantiate this class directly.
    """
    
    OPTS_KEYS_TO_PERSIST = ['name', 'description', 'group_id', 'status']

    def __init__(self, http_client, page_id):
        """
        :param :class:`statuspageio.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client
        self.page_id = page_id
        self.container = 'subscriber'

    @property
    def http_client(self):
        return self.__http_client

    def list(self):
        """
        List subscribers

        Lists all of the current subscribers
        :calls: ``get /pages/[page_id]/subscribers.json``
        :return: Dictionary that support attriubte-style access and represents updated Component resource.
        :rtype: dict
        """

        _, _, subscribers = self.http_client.get(
            '/pages/{page_id}/subscribers.json'.format(page_id=self.page_id))
        return subscribers

    def create(self, **kwargs):
        """
        Create a subscriber

        :calls: ``post pages/{page_id}/subscribers.json``
        :param dict **kwargs:  subscriber attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Component resource.
        :rtype: dict
        """

        OPTS_KEYS_TO_PERSIST = [
            'email',
            'phone_number',
            'phone_country',
            'endpoint',
            'skip_confirmation_notification',
            'page_access_user']

        if not kwargs:
            raise Exception('attributes are missing')

        attributes = dict((k, v) for k, v in kwargs.iteritems()
                          if k in OPTS_KEYS_TO_PERSIST)

        _, _, subscriber = self.http_client.post(
            '/pages/{page_id}/subscribers.json'.format(
                page_id=self.page_id), container=self.container, body=attributes)

        return subscriber

    def delete(self, subscriber_id=None):
        """
        Create a subscriber

        :calls: ``delete pages/{page_id}/subscribers.json``
        :param subscriber_id
        :return: status code
        :rtype: int
        """

        status_code, _, _ = self.http_client.delete(
            "/pages/{page_id}/subscribers/{subscriber_id}.json".format(
                page_id=self.page_id, subscriber_id=subscriber_id))
        return status_code

class MetricsService(object):
    """
    :class:`statuspageio.MetricsService` is used by :class:`statuspageio.Client` to make
    actions related to Metrics resource.

    Normally you won't instantiate this class directly.
    """

    def __init__(self, http_client, page_id):
        """
        :param :class:`statuspageio.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client
        self.page_id = page_id
        self.container = 'metric'

    @property
    def http_client(self):
        return self.__http_client

    def list_available(self):
        """
        List available metric providers
        :calls: ``get /metrics_providers.json``
        :return: Dictionary that support attriubte-style access and represents updated Component resource.
        :rtype: dict
        """

        _, _, providers = self.http_client.get('/metrics_providers.json')
        return providers

    def list_linked(self):
        """
        List linked metric providers
        :calls: ``get /pages/[page_id]/metrics_providers.json``
        :return: Dictionary that support attriubte-style access and represents updated Component resource.
        :rtype: dict
        """

        _, _, providers = self.http_client.get(
            '/pages/{page_id}/metrics_providers.json'.format(page_id=self.page_id))
        return providers

    def list_metrics_for_provider(self, provider_id=None):
        """
        List metrics for a linked metric provider
        :params provider_id This is the ID from the provider you are looking up
        :calls: ``/pages/{page_id}/metrics_providers/{metrics_provider_id}/metrics.json``
        :return: Dictionary that support attriubte-style access and represents updated Component resource.
        :rtype: dict
        """
        _, _, metrics = self.http_client.get(
            '/pages/{page_id}/metrics_providers/{metrics_provider_id}/metrics.json'.format(
                page_id=self.page_id, metrics_provider_id=provider_id))
        return metrics

    def create(self, provider_id=None, **kwargs):
        """
        Create a custom metric

        :calls: ``post /pages/[page_id]/metrics_providers/[metrics_provider_id]/metrics.json``
        :param provider_id: The id of the custom provider or 'self' from the available providers list
        :param dict **kwargs:  metic attributes to create.
        :return: Dictionary that support attriubte-style access and represents updated Component resource.
        :rtype: dict
        """

        OPTS_KEYS_TO_PERSIST = [
            'name',
            'suffix',
            'display',
            'tooltip_description',
            'y_axis_min',
            'y_axis_max',
            'decimal_places']

        if not kwargs:
            raise Exception('attributes are missing')

        attributes = dict((k, v) for k, v in kwargs.iteritems()
                          if k in OPTS_KEYS_TO_PERSIST)

        _, _, metric = self.http_client.post(
            '/pages/{page_id}/metrics_providers/{metrics_provider_id}/metrics.json'.format(
                page_id=self.page_id, metrics_provider_id=provider_id), container=self.container, body=attributes)

        return metric

    def submit_data(self, metric_id=None, **kwargs):
        """
        Create a custom metric

        :calls: ``post /pages/{page_id}/metrics/{metric_id}/data.json``
        :param metric_id: The id of the custom metric.
        :param dict **kwargs:  metic attributes to create.
        :return: Dictionary that support attriubte-style access and represents updated Component resource.
        :rtype: dict
        """

        OPTS_KEYS_TO_PERSIST = ['timestamp', 'value']

        if not kwargs:
            raise Exception('attributes are missing')

        attributes = dict((k, v) for k, v in kwargs.iteritems()
                          if k in OPTS_KEYS_TO_PERSIST)

        _, _, metric = self.http_client.post(
            '/pages/{page_id}/metrics/{metric_id}/data.json'.format(
                page_id=self.page_id, metric_id=metric_id), container='data', body=attributes)

        return metric

    def delete_all_data(self, metric_id=None):
        """
        Delete All Metric Data
        
        :calls: ``delete /pages/[page_id]/metrics/[metric_id]/data.json``
        :param metric_id: The id of the custom metric.
        :return: Dictionary that support attriubte-style access and represents updated Component resource.
        :rtype: dict
        """

        metric, _, _, = self.http_client.delete(
            "/pages/{page_id}/metrics/{metric_id}/data.json".format(
                page_id=self.page_id, metric_id=metric_id))
        return metric

    def delete(self, metric_id=None):
        """
        Delete Custom Metric
        
        :calls: ``delete /pages/[page_id]/metrics/[metric_id].json``
        :param metric_id: The id of the custom metric.
        :return: status code.
        :rtype: int
        """

        _, _, metric = self.http_client.delete(
            "/pages/{page_id}/metrics/{metric_id}.json".format(
                page_id=self.page_id, metric_id=metric_id))
        return metric

class UsersService(object):
    """
    :class:`statuspageio.UsersService` is used by :class:`statuspageio.Client` to make
    actions related to Users resource.

    Normally you won't instantiate this class directly.
    """
    def __init__(self, http_client, organization_id):
        """
        :param :class:`statuspageio.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client
        self.organization_id = organization_id
        self.container = 'user'

    @property
    def http_client(self):

        # TODO: Review. I did not want to have to set the orginization_id all
        # the time as many people may not want to manage users.
        if not self.organization_id:
            raise ConfigurationError(
                'No organization_id provided.'
                'You are unable to manage users. Set your organization_id during client initialization using: '
                '"statuspageio.Client(organization_id= <YOUR_PERSONAL_page_id>)"')

        return self.__http_client

    def list(self):
        """
        List all users
        :calls: ``get organizations/[organization_id]/users.json``
        :return: Dictionary that support attriubte-style access and represents User resource.
        :rtype: dict
        """
        _, _, users = self.http_client.get(
            '/organizations/{organization_id}/users.json'.format(
                organization_id=self.organization_id), container=self.container)
        return users

    def create(self, **kwargs):
        """
        Create a user 
        
        :calls: ``post /organizations/[organization_id]/users.json``
        :param dict **kwargs:  Users attributes to create.
        :return: Dictionary that support attriubte-style access and represents updated User resource.
        :rtype: dict
        """
        OPTS_KEYS_TO_PERSIST = ['email', 'password', 'first_name', 'last_name']

        if not kwargs:
            raise Exception('attributes are missing')

        attributes = dict((k, v) for k, v in kwargs.iteritems()
                          if k in OPTS_KEYS_TO_PERSIST)

        _, _, user = self.http_client.post(
            '/organizations/{organization_id}/users.json'.format(
                organization_id=self.organization_id), container=self.container, body=attributes)

        return user

    def delete(self, user_id=None):
        """
        Delete a User
        
        :calls: ``delete organizations/[organization_id]/users/[user_id].json``
        :param user_id: The id of the user to delete.
        :return: status code.
        :rtype: int
        """

        _, _, user = self.http_client.delete(
            "/organizations/{organization_id}/users/{user_id}.json".format(
                organization_id=self.organization_id, user_id=user_id))
        return user
