"""
Observer Pattern
----------------
Defines a one-to-many dependency between objects so that when one object
(the subject) changes state, all its dependents (observers) are notified
and updated automatically.

Use cases: event systems, MVC frameworks, pub/sub messaging.
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, event, data=None):
        """Receive an update from the subject."""


class Subject:
    """Maintains a list of observers and notifies them of state changes."""

    def __init__(self):
        self._observers: list[Observer] = []

    def subscribe(self, observer: Observer):
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, event, data=None):
        for observer in self._observers:
            observer.update(event, data)


class EventLogger(Observer):
    """Logs every event it receives."""

    def update(self, event, data=None):
        print(f"[Logger] event='{event}' data={data!r}")


class AlertService(Observer):
    """Sends an alert for critical events."""

    CRITICAL_EVENTS = {"error", "critical"}

    def update(self, event, data=None):
        if event in self.CRITICAL_EVENTS:
            print(f"[Alert] CRITICAL event '{event}': {data}")


if __name__ == "__main__":
    subject = Subject()

    logger = EventLogger()
    alert_service = AlertService()

    subject.subscribe(logger)
    subject.subscribe(alert_service)

    subject.notify("user_login", data={"user": "alice"})
    subject.notify("error", data="Disk full")
    subject.notify("user_logout", data={"user": "alice"})

    print("\n--- Unsubscribed logger ---\n")
    subject.unsubscribe(logger)
    subject.notify("critical", data="Database unreachable")
