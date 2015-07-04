class SimpleFormatter(object):

    def __call__(self, frame, event, arg):
        return "{}".format(frame.f_code)
