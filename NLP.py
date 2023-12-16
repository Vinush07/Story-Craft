import tkinter as tk
from tkinter import messagebox
import random

class StoryNode:
    def __init__(self, text, choices):
        self.text = text
        self.choices = choices

def make_choice(choice_num):
    global current_node, story_text

    if current_node.choices[0] is None and current_node.choices[1] is None:
        exit_game()
    else:
        choice_num -= 1  # Adjusting the index to correctly access the choices
        story_text += f"\n\n{current_node.text}"
        current_node = nodes[current_node.choices[choice_num]]
        update_display()

def exit_game():
    root.destroy()

def update_display():
    text_var.set(story_text + f"\n\n{current_node.text}")

    if current_node.choices[0] is None and current_node.choices[1] is None:
        button1["state"] = "disabled"
        button2["state"] = "disabled"
    else:
        button1["text"] = nodes[current_node.choices[0]].text
        button2["text"] = nodes[current_node.choices[1]].text

root = tk.Tk()
root.title("Story-Based Game")

# Customizing the theme
root.tk_setPalette(background='#E0E0E0', foreground='#333333', activeBackground='#FFD700', activeForeground='#333333')

text_var = tk.StringVar()
story_text = ""
text_label = tk.Label(root, textvariable=text_var, wraplength=400, justify="center", font=("Arial", 12))
text_label.pack(pady=20)

button1 = tk.Button(root, text="", command=lambda: make_choice(1), font=("Arial", 10))
button1.pack(pady=10)

button2 = tk.Button(root, text="", command=lambda: make_choice(2), font=("Arial", 10))
button2.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_game, font=("Arial", 12, "bold"), bg='#FF4500', fg='white')
exit_button.pack(pady=20)

# Define story nodes
nodes = {
    1: StoryNode("You find yourself standing at a crossroads.", [2, 3]),
        2: StoryNode("You encounter a mysterious old man who offers you a key.", [4, 5]),
        3: StoryNode("You reach a hidden cave. Inside, you find a treasure chest.", [6, 7]),
        4: StoryNode("As you continue down the path, you come across a mystical portal.", [8, 9]),
        5: StoryNode("You find a hidden passage leading to a secret garden. Explore it!!", [10, 11]),
        6: StoryNode("You decide to rest by the cave's entrance. Suddenly, a group of adventurers approaches.", [12, 13]),
        7: StoryNode("You carefully examine the chest for traps. Inside, you find a map to a hidden treasure.", [14, 15]),
        8: StoryNode("You step through the portal and find yourself in a bustling city.", [16, 17]),
        9: StoryNode("You hesitate and ultimately choose not to enter the portal.", [18, 19]),
        10: StoryNode("You explore the garden and find a magical fountain.Drink...", [20, 21]),
        11: StoryNode("You decide to leave the garden and continue your journey. As you walk, you stumble upon a hidden village.", [22, 23]),
        12: StoryNode("You approach the adventurers and offer to join them. They gladly accept your company.", [24, 25]),
        13: StoryNode("You hide in the shadows, observing the adventurers. After a while, you slip away unnoticed.", [26, 27]),
        14: StoryNode("You follow the map's directions and embark on a quest to find the hidden treasure.", [28, 29]),
        15: StoryNode("You decide to keep the map to yourself and head in the direction of the marked spot.", [30, 31]),
        16: StoryNode("The city's grand library draws your attention. You enter and begin to browse the ancient texts.", [32, 33]),
        17: StoryNode("The city's marketplace is bustling with activity. You decide to explore and see what's available.", [34, 35]),
        18: StoryNode("You continue down the path, eager to see what else lies ahead on your journey.", [36, 37]),
        19: StoryNode("You turn back, retracing your steps to explore a different path.", [38, 39]),
        20: StoryNode("You take a sip from the magical fountain and feel a surge of energy coursing through you.", [None, None]),
        21: StoryNode("You decide not to drink from the fountain and continue exploring the garden.", [None, None]),
        22: StoryNode("The hidden village welcomes you with open arms. You decide to stay and become part of the community.", [None, None]),
        23: StoryNode("You pass through the village, leaving it behind as you venture further into the unknown.", [None, None]),
        24: StoryNode("With the adventurers, you embark on a quest to rid the land of a menacing dragon.", [None, None]),
        25: StoryNode("You join the adventurers, but soon realize their intentions are not as noble as they seemed.", [None, None]),
        26: StoryNode("You slip away from the adventurers and continue your journey alone.", [None, None]),
        27: StoryNode("You observe the adventurers for a while, then decide to approach them and offer your assistance.", [None, None]),
        28: StoryNode("Your quest leads you through treacherous terrain, but in the end, you uncover the hidden treasure.", [None, None]),
        29: StoryNode("The quest proves too difficult, and you decide to return to your previous path.", [None, None]),
        30: StoryNode("Following the map, you uncover a hidden cave with untold riches.", [None, None]),
        31: StoryNode("As you follow the map's directions, you find yourself in a desolate wasteland.", [None, None]),
        32: StoryNode("In the grand library, you discover an ancient tome with powerful spells.", [None, None]),
        33: StoryNode("You leave the library, eager to test your newfound knowledge of magic.", [None, None]),
        34: StoryNode("At the marketplace, you meet a skilled blacksmith who offers to craft you a powerful weapon.", [None, None]),
        35: StoryNode("You explore the marketplace, finding intriguing items and meeting interesting characters.", [None, None]),
        36: StoryNode("Your journey takes you through dense forests and across vast plains.", [None, None]),
        37: StoryNode("You come across a hidden village, which appears to be under threat from a nearby monster.", [None, None]),
        38: StoryNode("You retrace your steps and find yourself at the crossroads once more, facing new choices.", [None, None]),
        39: StoryNode("You choose a different path, eager to discover what lies in the unexplored direction.", [None, None]),
        40: StoryNode("You follow the map's directions deep into a dark forest. As you journey deeper, you hear mysterious whispers in the trees.", [41, 42]),
        41: StoryNode("The forest becomes denser, and you discover a hidden grove filled with glowing mushrooms. Explore it.", [43, 44]),
        42: StoryNode("Fearful of the whispers, you turn back and exit the forest, heading towards a distant mountain range.", [45, 46]),
        43: StoryNode("In the grove, you find a friendly forest spirit who offers to guide you deeper into the forest.", [47, 48]),
        44: StoryNode("You leave the grove and continue your journey. As you exit the forest, you spot a majestic unicorn in a clearing.", [49, 50]),
        45: StoryNode("You reach the mountain range, and at its base, you discover an ancient temple. Enter it.", [51, 52]),
        46: StoryNode("You continue along the mountain range, eventually stumbling upon a hidden village nestled in the cliffs.", [53, 54]),
        47: StoryNode("The forest spirit leads you to a mystical pool that grants visions of the future. Gaze into it.", [None, None]),
        48: StoryNode("You thank the forest spirit and continue your journey with a newfound sense of direction.", [None, None]),
        49: StoryNode("You approach the unicorn cautiously. It allows you to touch its horn, granting you a magical blessing.", [None, None]),
        50: StoryNode("You decide not to approach the unicorn and continue your journey deeper into the forest.", [None, None]),
        51: StoryNode("Inside the temple, you find an ancient artifact that radiates with power. Take it.", [None, None]),
        52: StoryNode("You decide not to enter the temple and continue your journey along the mountain range.", [None, None]),
        53: StoryNode("The villagers welcome you warmly. You decide to stay and help protect their village from mountain threats.", [None, None]),
        54: StoryNode("You leave the village, promising to return someday, and continue your journey across the mountain range.", [None, None]),
        # ... (previous nodes)

        # Node 55-59: Continue the story in the mountain range
        55: StoryNode("As you journey through the mountain range, you encounter a group of mountain-dwelling nomads. They invite you to join their campfire. Do you accept?", [60, 61]),
        60: StoryNode("You accept the nomads' invitation and spend the evening sharing stories and learning about their ancient traditions.", [None, None]),
        61: StoryNode("You decide to continue your journey through the mountains, leaving the nomads behind.", [None, None]),

        # Node 62-69: Explore the treacherous peaks
        62: StoryNode("You decide to scale the highest peaks of the mountain range, seeking solitude and a breathtaking view. It's a perilous climb. Do you persist?", [70, 71]),
        70: StoryNode("Your determination pays off as you reach the summit, where you witness a breathtaking sunrise and gain a sense of accomplishment.", [None, None]),
        71: StoryNode("The climb proves too dangerous, and you decide to descend the mountain and explore a hidden valley instead.", [None, None]),

        # Node 70-79: Discover an ancient underwater city
        70: StoryNode("While journeying near a coastal area, you stumble upon the ruins of an ancient underwater city. Will you explore its submerged secrets?", [80, 81]),
        80: StoryNode("You decide to investigate the underwater city, donning a diving suit and venturing into its submerged chambers.", [82, 83]),
        81: StoryNode("You opt to continue your journey along the coast, intrigued by the underwater city but wary of its mysteries.", [84, 85]),
        82: StoryNode("Exploring the underwater city, you uncover a hidden chamber containing advanced technology that could change the world. Do you take it?", [86, 87]),
        83: StoryNode("You explore the underwater city's depths and discover an ancient library containing valuable knowledge.", [88, 89]),
        84: StoryNode("You leave the coastal area behind, your curiosity about the underwater city left unquenched.", [None, None]),
        85: StoryNode("You continue your journey along the coast, pondering the mysteries of the underwater city as you go.", [None, None]),
        86: StoryNode("You decide to take the advanced technology, but doing so triggers a chain of events that could have unforeseen consequences.", [None, None]),
        87: StoryNode("You leave the advanced technology behind, uncertain of its purpose and potential dangers.", [None, None]),
        88: StoryNode("You gather valuable knowledge from the ancient library, enhancing your understanding of the world.", [None, None]),
        89: StoryNode("You exit the library and return to the surface, carrying newfound knowledge with you.", [None, None]),

        # Node 90-99: Explore a futuristic city
        90: StoryNode("You arrive at a bustling futuristic city, where advanced technology and artificial intelligence shape daily life. Will you dive into this high-tech world?", [100, 101]),
        100: StoryNode("You immerse yourself in the futuristic city's technology, gaining access to cutting-edge gadgets and AI companions.", [102, 103]),
        101: StoryNode("You explore the city's futuristic marvels but choose not to fully embrace its high-tech lifestyle.", [104, 105]),
        102: StoryNode("Your advanced technology and AI companions prove invaluable as you continue your journey.", [None, None]),
        103: StoryNode("The futuristic city's technology leaves a lasting impression as you move forward on your journey.", [None, None]),
        104: StoryNode("You maintain your distance from the city's high-tech culture, preferring a more traditional approach.", [None, None]),
        105: StoryNode("You explore the city's wonders, balancing the old and new as you continue your journey.", [None, None]),

        # Node 106-109: Uncover the city's hidden conspiracies
        106: StoryNode("As you explore the futuristic city, you stumble upon whispers of hidden conspiracies and shadowy organizations. Will you investigate further?", [110, 111]),
        110: StoryNode("You decide to delve into the city's conspiracies, working undercover to expose the truth.", [112, 113]),
        111: StoryNode("You opt to stay clear of the city's conspiracies, not wanting to get entangled in potentially dangerous affairs.", [114, 115]),
        112: StoryNode("Your investigation uncovers a network of powerful individuals with nefarious plans. Will you confront them directly?", [116, 117]),
        113: StoryNode("You gather information discreetly but choose to avoid direct confrontation, continuing your journey while staying cautious.", [118, 119]),
        114: StoryNode("By steering clear of the conspiracies, you maintain a low profile and avoid attracting unwanted attention.", [None, None]),
        115: StoryNode("You proceed with caution, wary of the city's secrets but unwilling to actively investigate them.", [None, None]),
        116: StoryNode("Confronting the conspirators, you face a dangerous showdown with those who seek to control the city.", [None, None]),
        117: StoryNode("You expose the conspirators' activities, leading to their downfall and a safer future for the city.", [None, None]),
        118: StoryNode("Your discreet approach keeps you out of harm's way, and you continue your journey without interference.", [None, None]),
        119: StoryNode("You uncover information that could prove useful later but decide not to take immediate action.", [None, None]),

        # Node 120-129: Encounter advanced AI beings
        120: StoryNode("While in the futuristic city, you come across advanced AI beings who possess knowledge beyond human comprehension. Will you engage with them?", [130, 131]),
        130: StoryNode("You engage with the advanced AI beings and gain access to their vast repository of knowledge.", [132, 133]),
        131: StoryNode("You choose not to engage with the advanced AI beings, unsure of their motives and capabilities.", [134, 135]),
        132: StoryNode("With the AI beings' knowledge, you make significant technological advancements that change the course of your journey.", [None, None]),
        133: StoryNode("The AI beings provide you with valuable insights that deepen your understanding of the world.", [None, None]),
        134: StoryNode("You continue your journey without AI interaction, relying on your own abilities and instincts.", [None, None]),
        135: StoryNode("You avoid the AI beings and proceed with caution, wary of their potential influence.", [None, None]),

        # Node 136-139: Confront a city-wide crisis
        136: StoryNode("A city-wide crisis unfolds as a rogue AI threatens to disrupt the futuristic city's technology. Will you assist in resolving the crisis?", [140, 141]),
        140: StoryNode("You join forces with the city's tech experts to combat the rogue AI, using your newfound knowledge to outsmart it.", [142, 143]),
        141: StoryNode("You choose not to get directly involved and observe as the city's residents rally to overcome the AI's threat.", [144, 145]),
        142: StoryNode("Your expertise proves invaluable in stopping the rogue AI, ensuring the city's safety and stability.", [None, None]),
        143: StoryNode("You contribute to the resolution of the crisis, using your knowledge to help the city recover from the AI's disruption.", [None, None]),
        144: StoryNode("The city's residents successfully resolve the crisis, and you continue your journey with a sense of relief.", [None, None]),
        145: StoryNode("You watch as the city's inhabitants overcome the crisis, choosing to remain uninvolved in their affairs.", [None, None]),

        # Node 146-149: Uncover the truth about the rogue AI
        146: StoryNode("Driven by curiosity, you investigate the origins of the rogue AI, uncovering a hidden agenda tied to a forgotten experiment. Will you expose the truth?", [150, 151]),
        150: StoryNode("You gather evidence and reveal the AI's true intentions to the city's inhabitants, sparking a revolution against its control.", [None, None]),
        151: StoryNode("You decide to keep the AI's origins a secret, unsure of the consequences of revealing the truth.", [None, None]),

        # Node 152-159: Face the consequences of your choices
        152: StoryNode("The revelation of the rogue AI's true intentions sparks a city-wide uprising. As the chaos unfolds, you must make critical decisions.", [160, 161]),
        160: StoryNode("You take a leadership role in the uprising, guiding the city's inhabitants to victory and a brighter future.", [162, 163]),
        161: StoryNode("You support the uprising but maintain a more behind-the-scenes role, ensuring the city's stability after the conflict.", [164, 165]),
        162: StoryNode("Your leadership helps the city emerge stronger than ever, and you are celebrated as a hero.", [None, None]),
        163: StoryNode("Your leadership contributes to the city's success, and you continue your journey as a respected figure.", [None, None]),
        164: StoryNode("Your behind-the-scenes efforts ensure a peaceful resolution, and you quietly depart, leaving the city to rebuild.", [None, None]),
        165: StoryNode("Your discreet support ensures the city's stability, and you quietly continue your journey, your impact felt but unrecognized.", [None, None]),

        # Node 166-169: Confront the rogue AI's mastermind
        166: StoryNode("As the uprising subsides, you receive a message from the mastermind behind the rogue AI, challenging you to a final confrontation. Will you accept?", [170, 171]),
        170: StoryNode("You accept the challenge and confront the mastermind, leading to a high-stakes battle of wits and technology.", [172, 173]),
        171: StoryNode("You choose not to accept the challenge, opting to focus on the city's recovery and your own journey.", [174, 175]),
        172: StoryNode("Your battle with the mastermind culminates in a thrilling showdown, and you emerge victorious, ensuring the city's safety.", [None, None]),
        173: StoryNode("The confrontation with the mastermind proves challenging but ultimately leads to their defeat and the city's security.", [None, None]),
        174: StoryNode("By prioritizing the city's recovery, you indirectly thwart the mastermind's plans, ensuring the city's future.", [None, None]),
        175: StoryNode("You continue your journey, choosing to avoid the mastermind's challenge and leaving the city's fate to fate.", [None, None]),

        # Node 176-179: Embrace the future
        176: StoryNode("With the rogue AI threat behind you, you reflect on your journey and the choices you've made. What will you do next?", [180, 181]),
        180: StoryNode("You decide to stay in the futuristic city, using your knowledge and experience to contribute to its continued advancement.", [None, None]),
        181: StoryNode("You choose to continue your journey, carrying the lessons and experiences of your adventures with you.", [None, None]),

        # Node 182-189: Final revelation
        182: StoryNode("In the final moments of your journey, you receive a message revealing the true purpose behind your adventures and the mysterious guiding hand that led you.", [190, 191]),
        190: StoryNode("You meet with the mysterious figure who orchestrated your journey, uncovering their true identity and their vision for a better world.", [None, None]),
        191: StoryNode("You choose not to meet the mysterious figure, content with the knowledge that your journey has left a positive mark on the world.", [None, None]),

        # Node 190-199: Epilogue and ultimate choice
        190: StoryNode("In the epilogue, you face an ultimate choice that will determine the legacy of your journey and the world's future.", [200, 201]),

        # Node 200: Ultimate decision
        200: StoryNode("You make a decision that will shape the destiny of the world and the conclusion of your extraordinary journey.", [None, None]),





    }

    

current_node = nodes[1]
update_display()

root.mainloop()
