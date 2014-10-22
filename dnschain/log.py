import logging


class LoggingMixin(object):
    def _logger_helper(self, definitionmodulename):
        long_name = "%s.%s_debug.log" % (definitionmodulename, self.__class__.__name__)
        self._log = logging.getLogger(long_name)
        self._log.debug('Initialized.')
        logging.basicConfig(filename = long_name,
                            level = logging.DEBUG,
                            format = '\n%(asctime)s %(levelname) 7s [%(name)-25s L%(lineno)d]\
                            \n> %(message)s\n',
                            datefmt = '%Y-%m-%dT%H:%M:%S%z')

