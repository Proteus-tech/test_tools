# -*- coding: utf-8 -*-
import simplejson
import urllib

from django.http import HttpResponse
from django.conf import settings

def auth_api_user_return(user_list):
    data_list = []
    for index, user in enumerate(user_list):
        data = {}
        data['id'] = 1
        data['username'] = user
        data['first_name'] = 'Test'
        data['last_name'] = '%s' % (index)
        data['email'] = '%s@proteus-tech.com' % (user)
        data['last_login'] = data['date_joined'] = '2011-03-04 22:29:00'
        data_list.append(data.copy())

    if len(data_list) == 1:
        return_data = data_list[0]
    else:
        return_data = data_list
    return HttpResponse(simplejson.dumps(return_data),content_type='application/json')

def auth_api_mock(url):
    if '/api/user/' in url:
        return auth_api_user_return(['chanita',])
    elif '/api/users/' in url:
        return auth_api_user_return(['chanita','nattapon'])
    return None # we can return None here because conditional_mock_calls will handle returning HttpResponse by default

def story_mock(url):
    if '/story/project/' in url:
        story_json_file = open(settings.PROJECT_PATH_JOIN('test_tools','data','test_story_data.json'))
        stories = simplejson.load(story_json_file)
        if 'current_owner=' in url:
            split_url = url.split('current_owner=')
            current_owner = urllib.unquote(split_url[1])
            filtered_stories = [story for story in stories if story['current_owner'] == current_owner]
            stories = filtered_stories
        return HttpResponse(simplejson.dumps(stories),content_type='application/json')
    return None
  