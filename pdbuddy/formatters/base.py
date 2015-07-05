class BaseFormatter(object):

    def __call__(self, frame, event, arg):
        raise NotImplementedError('Subclasses should implement __call__')
