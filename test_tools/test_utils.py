import functools

import re
def raise_value(exc_type, exc_msg):
    def decorate(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                fn(*args, **kwargs)
            except Exception, exc:
                if not isinstance(exc, exc_type):
                    raise AssertionError(u'%s did not raise %s' % (fn.func_name, exc_type.__name__))
                if not re.match(exc_msg, unicode(exc)):
                    raise AssertionError(u'"%s" is not in "%s"' % (exc_msg, exc))
            else:
                raise AssertionError(u'%s did not raise %s' % (fn.func_name, exc_type.__name__))
                
        return wrapper
    return decorate

def skip_case(condition):
    def decorate(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            if not condition:
                return fn(*args, **kwargs)
            
        return wrapper
    return decorate

def super_setup(klass,instance):
    super(klass,instance).setUp()

def super_teardown(klass,instance):
    super(klass,instance).tearDown()
    