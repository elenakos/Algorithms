# You're testing a UI events seq that has steps A → B → C.
# Each step becomes enabled only after the previous one is complete.
# Given a sequence of UI events, validate whether the state transitions are valid.
# Example:
# events = ["startA", "completeA", "startB", "startC", "completeB", "completeC"] -> invalid
# events = ["startA", "completeA", "doSomething", "startC", "completeC", "doSomething", "startB", "completeB"] -> invalid
# events = ["startA", "doSomething", "completeA", "startB", "completeB", "startC", "doSomething", "completeC"] -> valid
import unittest

def verify_events(array):
    print("Verify if events happen in order")

    # Define a stack of expected events in order
    expected_events = ["startA", "completeA", "startB", "completeB", "startC", "completeC"]

    if len(array) < 6:
        print("Not enough events to complete steps A → B → C")
        return False

    # Navigate through the events array
    current_expected_index = 0
    for event in array:
        #print("Current in events: {}".format(event))
        if event in expected_events:
            if current_expected_index == len(expected_events):
                print("There is some repeated event")
                return False
            expected_event = expected_events[current_expected_index]
            #print("Popped from the expected event: {}".format(exp))
            if expected_event != event:
                print("Expected event {} is not the same as an actual event {}".format(event, expected_event))
                return False
            current_expected_index += 1

    if current_expected_index == len(expected_events):
        print("All events were correct!")
        return True

    print("Some events did not happen: {}".format(expected_events[current_expected_index:]))
    return False


class TestSolution(unittest.TestCase):
    def test_not_enough_events(self):
        print("\n*** TC: Test not enough events ***")
        event1 = ["startA", "completeA", "startB", "completeB", "completeC"]
        self.assertFalse(verify_events(event1))

    def test_event_not_in_order(self):
        print("\n*** TC: Test not all events ***")
        event2 = ["startA", "completeA", "doSomething", "startC", "completeC", "doSomething", "startB", "completeB"]
        self.assertFalse(verify_events(event2))

    def test_not_all_events(self):
        print("\n*** TC: Test not all events are completed ***")
        event2 = ["startA", "completeA", "doSomething", "startB", "something", "completeB", "startC",  "doSomething"]
        self.assertFalse(verify_events(event2))

    def test_all_events(self):
        print("\n*** TC: Test all events ***")
        event3 = ["startA", "doSomething", "completeA", "startB", "completeB", "startC", "doSomething", "completeC"]
        self.assertTrue(verify_events(event3))

    def test_all_events_with_repeats(self):
        print("\n*** TC: Test all events with one repeat ***")
        event3 = ["startA", "doSomething", "completeA", "startB", "completeB", "startC", "doSomething", "completeC", "doSomething", "startB"]
        self.assertFalse(verify_events(event3))