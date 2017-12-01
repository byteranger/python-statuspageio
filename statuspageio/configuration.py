from statuspageio.version import VERSION
from statuspageio.errors import ConfigurationError
import warnings


class Configuration(object):



    def __init__(self, **options):
        """
        :param str api_key: Personal access token.
        :param str page_id:  The page_id you wish to manage
        :param str organization_id: (optional) The organization id, used for managing user accounts
        :param bool verbose: (optional) Verbose/debug mode. Default: ``False``.
        :param int timeout: (optional) Connection and response timeout. Default: **30** seconds.
        :param bool verify_ssl: (optional) Whether to verify ssl or not. Default: ``True``.
        """

        self.api_key = options.get('api_key')
        self.page_id = options['page_id']
        self.organization_id = options['organization_id'] if 'organization_id' in options else False
        self.base_url = 'https://api.statuspage.io'
        self.user_agent = 'StatusPage/v1 Python/{0}'.format(VERSION)
        self.verbose = options['verbose'] if 'verbose' in options else False
        self.timeout = options['timeout'] if 'timeout' in options else 30
        self.verify_ssl = options['verify_ssl'] if 'verify_ssl' in options else True
        

        if self.verbose:
            print "StatusPage client configuration: " + str(self.__dict__)

    def validate(self):
        """Validates whether a configuration is valid.

        :rtype: bool
        :raises ConfigurationError: if no ``api_key`` provided.
        :raises ConfigurationError: if no ``page_id`` provided.
        :warns 'No organization_id provided.' if no ``organization_id`` provided
        """
        if self.api_key is None:
            raise ConfigurationError('No api_key provided. '
                                     'Set your access token during client initialization using: '
                                     '"statuspageio.Client(api_key= <YOUR_PERSONAL_api_key>)"')



        if not self.page_id:
            raise ConfigurationError('No page_id provided.'
                                     'Set your page id during client initialization using: '
                                     '"statuspageiocrm.Client(page_id= <YOUR_PERSONAL_page_id>)"')
            
        if not self.organization_id:
            warnings.warn('No organization_id provided.'
                          'You will be unable to manage users. Set your organization_id during client initialization using: '
                          '"statuspageiocrm.Client(organization_id= <YOUR_PERSONAL_page_id>)"')

        return True