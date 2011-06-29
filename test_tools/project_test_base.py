# -*- coding: utf-8 -*-
from django.conf import settings

from service_api_tools.test_utils.test_base import TestBase

from test_tools.test_utils import super_setup, super_teardown
from test_tools.mock_functions import auth_api_mock, story_mock

class ProjectTestBase(TestBase):
    fixtures = []
    mock_functions = TestBase.mock_functions + [auth_api_mock,story_mock]

    def setUp(self):
        super_setup(ProjectTestBase,self)

        # just to make sure of the service urls, we're going to force the service host
        self._orig_service_project = settings.SERVICE_PROJECT
        settings.SERVICE_PROJECT = 'http://127.0.0.1:8002'

        self._orig_service_story = settings.SERVICE_FEATURE
        settings.SERVICE_FEATURE = 'http://127.0.0.1:8000'

        self._orig_service_auth = settings.SERVICE_AUTH
        settings.SERVICE_AUTH = 'http://127.0.0.1:8001'

        self.http_json_connection_mock.get.side_effect=self.conditional_mock_calls
        self.httplib2_json_connection_mock.mock_httplib2_http_request.side_effect=self.conditional_mock_httplib2_calls
        
    def tearDown(self):
        settings.SERVICE_PROJECT = self._orig_service_project
        settings.SERVICE_FEATURE = self._orig_service_story
        settings.SERVICE_AUTH = self._orig_service_auth
        super_teardown(ProjectTestBase,self)

  