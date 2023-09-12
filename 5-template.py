from abc import ABC, abstractmethod


class AuditTrail:
    def record(self):
        print('audited')


class Task(ABC):
    def __init__(self) -> None:
        self._audit_trail = AuditTrail()

    def execute(self):
        self._audit_trail.record()
        self._do_execute()

    @abstractmethod
    def _do_execute(self):
        pass


class MoneyTransfer(Task):
    def _do_execute(self):
        print('money transfered')


class GenerateReport(Task):
    def _do_execute(self):
        print('report genrated')


if __name__ == '__main__':
    MoneyTransfer().execute()
    