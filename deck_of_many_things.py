import random
import json
# import pickle

'''
https://roll20.net/compendium/dnd5e/Deck%20of%20Many%20Things#content

'''

class DeckOfManyThings(object):

    def __init__(self, size=None):

        if 13 != size and 22 != size:
            size = random.choice([13, 13, 13, 22])

        self._cards = [
            {
        		"name": "Sun",
        		"playing_card": "King of diamonds",
                "tarot_card": "XIX. The Sun",
                "description": "You gain 50,000 XP, and a wondrous item (which the DM determines randomly) appears in your hands.",
                "destroy": True
        	}, {
        		"name": "Moon",
        		"playing_card": "Queen of diamonds",
                "tarot_card": "XVIII. The Moon",
                "description": "You are granted the ability to cast the wish spell 1d3 times.",
                "destroy": True
        	}, {
        		"name": "Star",
        		"playing_card": "Jack of diamonds",
                "tarot_card": "XVII. The Star",
                "description": "Increase one of your Ability Scores by 2. The score can exceed 20 but can't exceed 24.",
                "destroy": True
        	}, {
        		"name": "Throne",
        		"playing_card": "King of hearts",
                "tarot_card": "Four of wands",
                "description": "You gain proficiency in the Persuasion skill, and you double your proficiency bonus on checks made with that skill. In addition, you gain rightful ownership of a small keep somewhere in the world. However, the keep is currently in the hands of Monsters, which you must clear out before you can claim the keep as. yours.",
                "destroy": True
        	}, {
        		"name": "Key",
        		"playing_card": "Queen of hearts",
                "tarot_card": "V. The Hierophant",
                "description": "A rare or rarer Magic Weapon with which you are proficient appears in your hands. The DM chooses the weapon.",
                "destroy": True
        	}, {
        		"name": "Knight",
        		"playing_card": "Jack of hearts",
                "tarot_card": "Page of swords",
                "description": "You gain the service of a 4th-level Fighter who appears in a space you choose within 30 feet of you. The Fighter is of the same race as you and serves you loyally until death, believing the fates have drawn him or her to you. You control this character.",
                "destroy": True
        	}, {
        		"name": "The Void",
        		"playing_card": "King of clubs",
                "tarot_card": "Eight of swords",
                "description": "This black card Spells disaster. Your soul is drawn from your body and contained in an object in a place of the DM's choice. One or more powerful beings guard the place. While your soul is trapped in this way, your body is Incapacitated. A wish spell can't restore your soul, but the spell reveals the location of the object that holds it. You draw no more cards.",
                "destroy": True
        	}, {
        		"name": "Flames",
        		"playing_card": "Queen of clubs",
                "tarot_card": "XV. The Devil",
                "description": "A powerful devil becomes your enemy. The devil seeks your ruin and plagues your life, savoring your suffering before attempting to slay you. This enmity lasts until either you or the devil dies.",
                "destroy": True
        	}, {
        		"name": "Skull",
        		"playing_card": "Jack of clubs",
                "tarot_card": "XIII. Death",
                "description": "You summon an avatar of death-a ghostly humanoid Skeleton clad in a tattered black robe and carrying a spectral scythe. It appears in a space of the DM's choice within 10 feet of you and attacks you, warning all others that you must win the battle alone. The avatar fights until you die or it drops to 0 Hit Points, whereupon it disappears. If anyone tries to help you, the helper summons its own avatar of death. A creature slain by an avatar of death can't be restored to life.",
                "destroy": True
        	}, {
        		"name": "Ruin",
        		"playing_card": "King of spades",
                "tarot_card": "XVI. The Tower",
                "description": "All forms of Wealth that you carry or own, other than Magic Items, are lost to you. Portable property vanishes. Businesses, buildings, and land you own are lost in a way that alters reality the least. Any documentation that proves you should own something lost to this card also disappears.",
                "destroy": True
        	}, {
        		"name": "Euryale",
        		"playing_card": "Queen of spades",
                "tarot_card": "Ten of swords",
                "description": "The card's medusa-like visage curses you. You take a -2 penalty on Saving Throws while cursed in this way. Only a god or the magic of The Fates card can end this curse.",
                "destroy": True
        	}, {
        		"name": "Rogue",
        		"playing_card": "Jack of spades",
                "tarot_card": "Five of swords",
                "description": "A nonplayer character of the DM's choice becomes hostile toward you. The identity of your new enemy isn't known until the NPC or someone else reveals it. Nothing less than a wish spell or Divine Intervention can end the NPC's hostility toward you.",
                "destroy": True
        	}, {
        		"name": "Jester",
        		"playing_card": "Joker (without TM)",
                "tarot_card": "XII. The Hanged Man",
                "description": "You gain 10,000 XP, or you can draw two additional cards beyond your declared draws.",
                "destroy": False
        	}
        ]

        if 22 == size:
            self._cards += [
                {
            		"name": "Vizier",
            		"playing_card": "Ace of diamonds",
                    "tarot_card": "IX. The Hermit",
                    "description": "At any time you choose within one year of drawing this card, you can ask a question in meditation and mentally receive a truthful answer to that question. Besides information, the answer helps you solve a puzzling problem or other dilemma. In other words, the knowledge comes with Wisdom on how to apply it.",
                    "destroy": True
            	}, {
            		"name": "Comet",
            		"playing_card": "Two of diamonds",
                    "tarot_card": "Two of swords",
                    "description": "If you single-handedly defeat the next hostile monster or group of Monsters you encounter, you gain Experience Points enough to gain one level. Otherwise, this card has no effect.",
                    "destroy": True
            	}, {
            		"name": "The Fates",
            		"playing_card": "Ace of hearts",
                    "tarot_card": "Three of Cups",
                    "description": "Reality's fabric unravels and spins anew, allowing you to avoid or erase one event as if it never happened. You can use the card's magic as soon as you draw the card or at any other time before you die.",
                    "destroy": True
            	}, {
            		"name": "Gem",
            		"playing_card": "Two of hearts",
                    "tarot_card": "Seven of Cups",
                    "description": "Twenty-five pieces of jewelry worth 2,000 gp each or fifty gems worth 1,000 gp each appear at your feet.",
                    "destroy": True
            	}, {
            		"name": "Talons",
            		"playing_card": "Ace of clubs",
                    "tarot_card": "Queen of pentacles",
                    "description": "Every magic item you wear or carry disintegrates. Artifacts in your possession aren't destroyed but do Vanish.",
                    "destroy": True
            	}, {
            		"name": "Idiot",
            		"playing_card": "Two of clubs",
                    "tarot_card": "Two of pentacles",
                    "description": "Permanently reduce your Intelligence by 1d4 + 1 (to a minimum score of 1). You can draw one additional card beyond your declared draws.",
                    "destroy": True
            	}, {
            		"name": "Donjon",
            		"playing_card": "Ace of spades",
                    "tarot_card": "Four of swords",
                    "description": "You disappear and become entombed in a state of suspended animation in an extradimensional Sphere. Everything you were wearing and carrying stays behind in the space you occupied when you disappeared. You remain imprisoned until you are found and removed from the Sphere. You can't be located by any Divination magic, but a wish spell can reveal the location of your prison. You draw no more cards.",
                    "destroy": True
            	}, {
            		"name": "Balance",
            		"playing_card": "Two of spades",
                    "tarot_card": "XI. Justice",
                    "description": "Your mind suffers a wrenching alteration, causing your Alignment to change. Lawful becomes chaotic, good becomes evil, and vice versa. If you are true neutral or unaligned, this card has no effect on you.",
                    "destroy": True
            	}, {
                    "name": "Fool",
            		"playing_card": "Joker (with TM)",
                    "tarot_card": "O. The Fool",
                    "description": "You lose 10,000 XP, discard this card, and draw from the deck again, counting both draws as one of your declared draws. If losing that much XP would cause you to lose a level, you instead lose an amount that leaves you with just enough XP to keep your level.",
                    "destroy": False
                }
            ]

        self.deck = {}
        for card in self._cards:
            self.deck[card['name']] = card

    def draw(self):
        name = random.choice(list(self.deck.keys()))
        card = self.deck[name]
        if card['destroy']:
            del self.deck[name]
        return card

    def size(self):
        return len(list(self.deck.keys()))

    def save(self, outfile):
        json.dump( self.deck, open( outfile + ".deck", "w" ) )

    def load(self, infile):
        self.deck = json.load( open( infile + ".deck", "r" ) )
