import random
import time
import openai
import os

# Safely load API key from environment variable
openai.api_key = os.getenv("AIzaSyDa6EQ8y2i8kvGLjuz9RDsPSC02lld-37g")

class ScriptWriterBot:
    def __init__(self):
        self.genre = ""
        self.characters = []
        self.plot_points = []
        self.theme = ""

    def generate_idea(self, genre=None):
        prompts = {
            "horror": ["A haunted asylum", "Cursed video tape", "Ancient burial ground"],
            "romance": ["Second chance love", "Forbidden relationship", "Wedding disaster"],
            "scifi": ["AI rebellion", "First contact", "Time loop paradox"]
        }

        if genre and genre.lower() in prompts:
            self.genre = genre.lower()
            idea = random.choice(prompts[self.genre])
        else:
            all_ideas = [item for sublist in prompts.values() for item in sublist]
            idea = random.choice(all_ideas)

        return f"How about this concept: '{idea}'? Want to develop it further?"

    def develop_character(self):
        traits = {
            "strengths": ["Brave", "Intelligent", "Resourceful"],
            "flaws": ["Impulsive", "Secretive", "Arrogant"],
            "arcs": ["Redemption", "Self-discovery", "Moral decline"]
        }

        character = {
            "name": "Character " + str(len(self.characters) + 1),
            "traits": f"{random.choice(traits['strengths'])}, but {random.choice(traits['flaws'])}",
            "arc": random.choice(traits['arcs'])
        }
        self.characters.append(character)
        return character

    def generate_dialogue(self, character_type="protagonist"):
        dialogues = {
            "protagonist": [
                "I can't turn back now, not when we're so close!",
                "There has to be another way...",
                "This changes everything."
            ],
            "antagonist": [
                "You think you can stop what's already begun?",
                "Your morality makes you weak.",
                "This world needs a new order."
            ]
        }
        return random.choice(dialogues.get(character_type.lower(), ["..."]))

    def ai_assisted_writing(self, prompt):
        """Requires OpenAI API"""
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Write a screenplay scene about {prompt}. Include dialogue and scene directions:",
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].text.strip()

    def feedback(self, script):
        feedback_options = [
            "Consider adding more character development in act 2.",
            "The pacing feels slow in the middle section.",
            "Great opening scene! Maybe strengthen the antagonist's motivation."
        ]
        return random.choice(feedback_options)

def chat():
    bot = ScriptWriterBot()
    print("ScriptBot: Hi! Let's create an amazing story.\n")

    while True:
        user_input = input("You: ").lower()

        if "idea" in user_input:
            genre = input("ScriptBot: Any preferred genre? (horror/romance/scifi) or press enter: ")
            print("ScriptBot:", bot.generate_idea(genre))

        elif "character" in user_input:
            char = bot.develop_character()
            print(f"ScriptBot: New character created!\nName: {char['name']}\nTraits: {char['traits']}\nArc: {char['arc']}")

        elif "dialogue" in user_input:
            char_type = input("ScriptBot: For protagonist or antagonist? ")
            print("ScriptBot:", bot.generate_dialogue(char_type))

        elif "write" in user_input:
            prompt = input("ScriptBot: What should the scene be about? ")
            print("ScriptBot: Here's a draft:\n", bot.ai_assisted_writing(prompt))

        elif "feedback" in user_input:
            script = input("ScriptBot: Paste your script excerpt: ")
            print("ScriptBot: Feedback:", bot.feedback(script))

        elif "exit" in user_input:
            print("ScriptBot: Happy writing! See you next time!")
            break

        else:
            print("ScriptBot: I can help with: ideas, characters, dialogue, feedback, or exit")

if __name__ == "__main__":
    chat()
