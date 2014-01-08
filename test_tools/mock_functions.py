# -*- coding: utf-8 -*-
import simplejson
import urllib

from django.http import HttpResponse
from django.conf import settings

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
  