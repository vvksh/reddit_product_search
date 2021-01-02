from unittest import TestCase

from entity_recognizer import EntityRecognizer


class TestEntityRecognizer(TestCase):
    er = EntityRecognizer()


    def test_get_labels_one_entity_in_input_outputs_one(self):
        sentence = "I've been living off a Dirt Devil (sorry Father for I have sinned) for awhile now, and I just bought a house so it's time to evolve."
        expected_output = ["Dirt Devil"]
        actual_output = self.__class__.er.get_labels(sentence)
        assert expected_output.__eq__(actual_output)

    def test_get_labels_two_entity_in_input_outputs_two(self):
        sentence = "Personally, I JUST inherited my late mother-in-law's nearly-new Miele Libra.   " \
                         "She was a stickler for upkeep with her appliances, so it's in great condition. " \
                         "We have zero carpeting and a small cat. She bought me a Roomba " \
                     "after she saw a commercial for it, but I'm selling it. I only used it a few " \
                     "times. Is there a good place to sell it?"
        expected_output = ["Miele Libra", "Roomba"]
        actual_output = self.__class__.er.get_labels(sentence)
        assert expected_output.__eq__(actual_output)

