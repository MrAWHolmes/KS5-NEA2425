#-------------------------------------------------------------------------------
# Name:        message_play.py
# Purpose:
#
# Author:      archi
#
# Created:     29/08/2024
# Copyright:   (c) archi 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""
PROMPT:
    In object orientated python, is there a message passing class
    that can send signals of an event to a message queue and that
    objects can accept or ignore.

    A simple example of class A throwing a message which class B
    catches but class C ignores would be helpful.

REF : https://chatgpt.com/c/c9c638bb-8fe6-41ab-9a06-d767878c44d1

"""
class MessageQueue:
    def __init__(self):
        self.subscribers = {}  # A dictionary to hold event types and their subscribers

    def subscribe(self, event_type, callback):
        """Subscribe a callback function to an event type."""
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)

    def unsubscribe(self, event_type, callback):
        """Unsubscribe a callback function from an event type."""
        if event_type in self.subscribers:
            self.subscribers[event_type].remove(callback)
            if not self.subscribers[event_type]:
                del self.subscribers[event_type]

    def publish(self, event_type, data):
        """Publish an event to all subscribers."""
        if event_type in self.subscribers:
            for callback in self.subscribers[event_type]:
                callback(data)


class ClassA:
    def __init__(self, message_queue):
        self.message_queue = message_queue

    def throw_message(self):
        print("ClassA: Throwing a message!")
        self.message_queue.publish("event_type_A", "Message from ClassA")


class ClassB:
    def __init__(self, message_queue):
        self.message_queue = message_queue
        self.message_queue.subscribe("event_type_A", self.catch_message)

    def catch_message(self, message):
        print(f"ClassB: Caught a message: {message}")


class ClassC:
    def __init__(self, message_queue):
        self.message_queue = message_queue
        # ClassC does not subscribe to any messages and will ignore them


# Example usage
message_queue = MessageQueue()

# Create instances of the classes
a = ClassA(message_queue)
b = ClassB(message_queue)
c = ClassC(message_queue)

# ClassA throws a message
a.throw_message()

# Output:
# ClassA: Throwing a message!
# ClassB: Caught a message: Message from ClassA
