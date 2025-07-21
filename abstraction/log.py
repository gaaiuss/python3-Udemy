# Abstraction
# Log
from pathlib import Path
from abc import ABC, abstractmethod

LOG_FILE = Path(__file__).parent / 'log.txt'


@abstractmethod
class Log(ABC):
    def _log(self, msg): ...

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        formatted_msg = f'{msg} ({self.__class__.__name__})'
        print(f'Saving log {formatted_msg}')
        with open(LOG_FILE, 'a', encoding='utf8') as archive:
            archive.write(formatted_msg)
            archive.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('\'Ello there!')
    lp.log_success('Nice!')
    lf = LogFileMixin()
    lf.log_error('\'Ello there!')
    lf.log_success('Nice!')
