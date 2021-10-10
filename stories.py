"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text,title):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text
        self.title = title

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key[0:len(key)-1] + "}", val)

        return text


# Here's a story to get you started


story_choices = [
    Story(
        ["place", "noun", "verb", "adjective", "plural_noun"],
        """Once upon a time in a long-ago {place}, there lived a
        large {adjective} {noun}. It loved to {verb} {plural_noun}.""",
        "A Short Story"
    ),
    Story(
        ["noun","adjective","animal","ice_cream_flavor","royal_title",
        "plural_noun","type_of_sandwich","verb","ing_verb","past_tense_verb",
        "exclamation","another_adjective","body_part"],
        """{exclamation} He said before {ing_verb} over the {adjective} {noun} connecting
        the two sides of the ravine. The road was rocky, like {ice_cream_flavor} ice cream,
        but he {past_tense_verb} for several more hours. Finally, just as he hit the peak
        of exhaustion, he came across the {royal_title} of the forest - a towering {animal}
        with piercing {another_adjective} {body_part}. The {animal} approached and after
        momentary contemplation chose to {verb} toward him and gave him a {type_of_sandwich}
        and some {plural_noun}.""",
        "Adventure Story"
    ),
    Story(
        ["noun","first_name","adjective","delicious_food","unpleasant_food","occupation",
        "body_of_water","large_corporation","verb","past_tense_verb","family_relation","plural_noun","adverb","adjective"],
        """{first_name} had only just {past_tense_verb} to the big city two months ago. Now,
        {first_name} found themself in quite a predicament. On the first day of their new job
        as head {occupation}, the business was bought by {large_corporation}. Long opposed to the
        unfair business practices of {large_corporation}, they had a {adjective} choice  to make.
        Continue to {verb} {adverb} every day for a terrible organization? Or look for new {plural_noun}
        after only just starting this one. But {first_name} remembered the wise words of their {family_relation}:
        'There are a {body_of_water} of opportunities out there. Never settle for {unpleasant_food} when you
        can have {delicious_food}!'""",
        "A Dilemma"
    ),
    Story(
        ["first_name","another_first_name","adjective","second_adjective","third_adjective",
        "fourth_adjective","fifth_adjective","business_with_many_locations","popular_beverage",
        "past_tense_verb","beverage","number","color","noun","term_of_endearment","activity"],
        """{first_name} had everything - {adjective}, {second_adjective}, and {third_adjective} with 
        a great {noun}. Most importantly, {first_name} was {fourth_adjective} and {fifth_adjective}. 
        {another_first_name} would take {first_name}'s order at {business_with_many_locations} every 
        single morning, and they would make small chit-chat. But today was the day {another_first_name} 
        decided to ask {first_name} out. When {first_name} {past_tense_verb} in to give his typical
        order - {beverage} with {number} shots of espresso - {another_first_name} already had it ready.  
        {another_first_name} handed the {beverage} over with a smile and looked in {first_name}'s beautiful 
        {color} eyes, the color of {noun}. 'Here's your {beverage}, {term_of_endearment}.'
        Would you like to go {activity} some time? {first_name} looked down
        at the drink and back up to {another_first_name}. 'Of course! The truth is, I don't even 
        like {beverage}.'""",
        "Love Story"
    )
]
