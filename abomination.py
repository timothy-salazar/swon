import random
from random import randrange

class Abomination:
    def __init__(self, rank, size):
        self.lines = []
        self.rank = rank
        self.ac = 10
        self.get_rolls()
        self.size = size + get_count(self.rolls, 4)
        self.number = 1
        self.speed = 5
        self.abom_8()
        self.calc_stats()
        self.ac += self.dexterity_mod
        self.flavor = self.get_flavor()

    def calc_stats(self):
        self.strength_mod = get_count(self.rolls,4) + self.size
        self.dexterity_mod = get_count(self.rolls,5) + 1 + self.rank if self.size < 2 else get_count(self.rolls,5) + self.rank
        self.constitution_mod = get_count(self.rolls,5) + self.rank
        self.intelligence_mod =  -2 + get_count(self.rolls,1) - get_count(self.rolls,8)
        if self.intelligence_mod < -2: self.intelligence_mod = -2
        self.wisdom_mod = -2 + get_count(self.rolls,6)
        self.charisma_mod = -2 + get_count(self.rolls,6)

        self.strength = self.mod_to_stat(self.strength_mod)
        self.dexterity = self.mod_to_stat(self.dexterity_mod)
        self.constitution = self.mod_to_stat(self.constitution_mod)
        self.intelligence = self.mod_to_stat(self.intelligence_mod)
        self.wisdom = self.mod_to_stat(self.wisdom_mod)
        self.charisma = self.mod_to_stat(self.charisma_mod)

    def get_lines(self):
        lines = self.get_stats() + '\n'
        lines += self.flavor
        return lines 

    def print(self):
        stats = self.get_stats()
        print(stats)
        self.print_flavor()

    def mod_to_str(self, stat_mod):
        if stat_mod < 0:
            return str(stat_mod)
        else:
            return f'+{stat_mod}'

    def get_stats(self):
        stats = ''
        if self.number > 1: 
            stats += f"""WARNING: THE ABOMINATION HAS SPLIT INTO {self.number} IDENTICAL COPIES!!!"""
        stats += f"""
        The creature has the following attribute:
            Strength:      {str(self.strength).ljust(3)} {self.mod_to_str(self.strength_mod)}
            Dexterity:     {str(self.dexterity).ljust(3)} {self.mod_to_str(self.dexterity_mod)}
            Constitution:  {str(self.constitution).ljust(3)} {self.mod_to_str(self.constitution_mod)}
            Intelligence:  {str(self.intelligence).ljust(3)} {self.mod_to_str(self.intelligence_mod)}
            Wisdom:        {str(self.wisdom).ljust(3)} {self.mod_to_str(self.wisdom_mod)}
            Charisma:      {str(self.charisma).ljust(3)} {self.mod_to_str(self.charisma_mod)}

        Other stats:
            AC:            {self.ac}
            Speed:         {self.speed}m/turn (standard movement is 10m/turn)
            Weapon:        {self.get_melee_attack() if self.get_melee_attack() else 'None.'}

        """
        return stats

    def get_flavor(self):
        lines = []
        # attributes
        lines.append(self.abom_0())
        lines.append(self.abom_2())
        lines.append(self.abom_3())
        # physical stats
        lines.append(self.abom_4())
        lines.append(self.abom_5())
        # mental stats
        lines.append(self.abom_1())
        lines.append(self.abom_6())
        return '\n'.join(['\n'.join(([j for j in i if len(j) > 0])) for i in lines if len(i) > 0])

    def print_flavor(self):
        print(self.flavor)

    def get_rolls(self):
        self.rolls = [randrange(10) for i in range(self.rank + 1)]
        self.rolls += abom_9(self.rolls, 9)
        self.rolls += self.abom_7()
        
    def abom_0(self):
        """It sprouts legs or wheels (base 10m/turn). On subsequent rolls it will sprout wings (allowing it to fly) or increase its speed.
        """
        c = get_count(self.rolls,0)
        lines = []
        fly = False
        fly_lines = [
            'The unholy creature sprouts wings! It can fly!!!',
            'There is a corruscation of sparks and an overwhelming reek of ozone as gravity looses its grip upon the unnatural creature. It can fly!!!',
            'Dragonfly wings of gleaming, razor edged metal sprout from the creature\'s back. As they blur into invisibility the abomination takes flight!!!',
            'Incandescent jets of energy shoot out of from the underside of the creature sending it rocketing into the air! It can fly!!!',
            'There is sound like someone running their finger along the rim of a wine glass. As the sound rises to an unbearable pitch the creature lifts from the ground without any visible means of propulsion! It can fly!!!',
        ]
        if c > 0:
            self.speed = self.speed * 2
            lines.append(
                'It sprouts legs or wheels, giving it a base movement speed of ')
            if c > 1:
                i = 1
                while i < c:
                    if not fly:
                        roll = random.choice([True, False])
                        if roll:
                            lines.append(random.choice(fly_lines))
                            fly = True
                        else:
                            self.speed = self.speed * 2
                    else:
                        self.speed = self.speed * 2
                    i += 1
            lines[0] = lines[0] + f'{self.speed}m/turn (standard movement is 10m/turn).'
        else:
            lines.append(
                f'The creature has no legs, but is able to roll and thrash its way across the ground giving it a base movement of {self.speed}m/turn (half standard)'
            )
        return lines

    def mod_to_stat(self, stat_mod):
        if stat_mod < -1:
            return 3
        if stat_mod == -1:
            return randrange(5,8)
        if stat_mod == 0:
            return randrange(9,14)
        if stat_mod == 1:
            return randrange(14,18)
        if stat_mod == 2:
            return 18
        if stat_mod > 2:
            start = 20 + (stat_mod-3)*5
            return randrange(start, start+5)
        

    def abom_1(self):
        """Intelligence modifier increased by 1
        """
        c = get_count(self.rolls, 1) -  get_count(self.rolls, 8)
        lines = []
        eyes = [
            'the abomination\'s terrifying segmented eyes',
            'the constantly whirring lenses of the monster\'s gaze',
            'the unnaturally ticking, writhing mechanisms of the creature\'s gaze',
            'the creature\'s strangely human eyes',
            'the cold lenses of the creature\'s eyes'
            ]
        if c < 1:
            lines.append(
                'The monstrosity only has room in its mind for an unthinking, psychotic rage! (intelligence 3, modifier -2)'
            )
            # self.intelligence = 3
            # self.int_mod = -2
        if c == 1:
            # self.intelligence = randrange(5,8)
            # self.int_mod = -1
            lines.append(
                f'Behind {random.choice(eyes)} you can see the spark of a malevolent intelligence (intelligence {self.intelligence}, modifier -1)'
            )

        if c == 2:
            # self.intelligence = randrange(9,14)
            # self.int_mod = 0
            lines.append(
                f'When you look into the creature\'s {random.choice(eyes)}, you see a cunning and dangerous mind looking back at you (intelligence {self.intelligence}, modifier +{self.intelligence_mod})'
            )
        if c == 3:
            lines.append(
                f'When you look into the creature\'s {random.choice(eyes)}, you see a disturbingly keen mind looking back at you (intelligence {self.intelligence}, modifier +{self.intelligence_mod})'
            )
        if c == 4:
            lines.append(
                f'When you look into the creature\'s {random.choice(eyes)}, you feel your blood run cold. There is an unnaturally sharp mind looking back at you (intelligence {self.intelligence}, modifier +{self.intelligence_mod})'
            )
        if c > 4:
            lines.append(
                f'When you look into the creature\'s eyes your blood runs cold. A truly superhuman intellect looks back at you, its gaze as terrible and pitiless as the sun (intelligence {self.intelligence}, modifier +{self.intelligence_mod})'
            ) 
        return lines 

    def get_melee_attack(self):
        c = get_count(self.rolls,2)
        melee_attacks = [
            '',
            '''Damage: 1d4     Shock: 1 point/AC 15   Attribute: Str/Dex   Type: Primitive''',
            '''Damage: 1d6+1   Shock: 2 point/AC 13   Attribute: Str/Dex   Type: Primitive''',
            '''Damage: 1d8+1   Shock: 2 point/AC 15   Attribute: Str/Dex   Type: Primitive''',
            '''Damage: 1d6     Shock: 1 point/AC 15   Attribute: Str/Dex   Type: Advanced''',
            '''Damage: 1d8+1   Shock: 2 point/AC 13   Attribute: Str/Dex   Type: Advanced''',
            '''Damage: 1d10+1  Shock: 2 point/AC 15   Attribute: Str/Dex   Type: Advanced''',
        ]
        return melee_attacks[c]

    def abom_2(self):
        """Consult the melee weapon chart on page 68. The first 6 entries go from small primative weapons to large advanced weapons. Number these entries 1-6 (1=small primative, 6=large advanced), and give the abomination a melee attack equal to its rank. Each subsequent roll will give it a stronger melee attack.
        """
        lines = []
        c = get_count(self.rolls,2)
        melee_lines_primative = [
            "Jagged, razor sharp bone spurs crack the abomination's casing, sliding out with a horrible scraping noise.",
            "The substance of the creature begins to warp. In places the metal runs like mercury, before reforming into gleaming tendrils that whip through the air viciously.",
            "The abomination finds a knife somewhere.",
            "With a pants-shittingly loud noise, a chainsaw blade emerges from the creature's \"chest\"."
        ]
        melee_lines_advanced = [
            "There is an overwhelming reek of ozone as the creature is surrounded by a fountain of sparks. As you watch, the sparks seem to take on substance, like the claws of a tiger formed from blue lightning.",
            "The creature begins to ooze a purple liquid that pulses with unnatural luminosity. Where it touches objects begin to blacken and spark, before seeming to disintigrate with a scintillation of impossible colors. As you watch, the ooze begins to form tentacles that squirm horribly through the air.",
            "The space around the creature seems to crack, like a reflection in a broken mirror. But these \"cracks\" in the air move with purpose. As one passes through a rock you watch it fall neatly in half. The glassy surface suggests a cut of euclidean perfection.",
        ]

        if c == 0:
            return lines
        elif c < 3:
            lines.append(random.choice(melee_lines_primative))
            lines.append('\t'+self.get_melee_attack())
        elif c > 6:
            lines.append(
                "The creature is suddenly surrounded by a living blaze of hideous light. It appears to you as a rainbow in which all natural color has been mutated into a painfully lush iridescence by some prism fantastically corupted in its form. It is an aurora that paints the scene with a shimmering effulgence that does not belong to this world."
            )
            lines.append(f'''Damage: 1d12+{1+(c-6)}  Shock: 2 point/AC 18   Attribute: Str/Dex   Type: Pretech''')
        else:
            lines.append(random.choice(melee_lines_advanced))
            lines.append(self.get_melee_attack())
        return lines

    def abom_3(self):
        """Grows a pair of fine manipulators or hands. Each subsequent roll gives it another pair of hands and gives the abomination +2 when grappling.
        """
        lines = []
        c = get_count(self.rolls,3)
        hands = [
            f'The creature grows {c} pairs of hands! This gives it +{c} to grapple attempts.',
            f'The creature sprouts {c} pairs of skeletal metal hands! It gains +{c} to grapple attempts.',
            f'The abomination begins to leak black slime. As you watch, the liquid forms itself into {c} pairs of inhuman hands! It gains +{c} to grapple attempts'
        ]
        if c == 0:
            return lines
        else:
            lines.append(random.choice(hands))
        return lines

    def abom_4(self):
        """Size increases by 1"""
        c = get_count(self.rolls, 4)
        lines = []
        size_list = [
                f'tiny (the size of a flashlight).',
                f'small (the size of a pair of heavy boots or a laptop).',
                f'medium sized (the size of a bicycle or hiking pack)',
                f'large (the size of a desk or a compact car)',
                f'huge (the size of a bus)',
                f'ridiculously huge (the size of a jumbo jet)']
        size_desc = size_list[self.size if self.size < len(size_list) else -1]
        if c == 0:
            lines.append(
                f'The creature\'s form is hideously warped, but it retains its original size.'
            )
        if c == 1:
            lines.append(
                f'A shudder ripples through the creature. The thing\'s unnatural musculature swells noticeably. The creature is {size_desc}'
            )
        if c == 2:
            lines.append(
                f'Matter seems to congeal out of the tortured vortex of metadimensional energy. Metallic muscles bulge, carapace stretches and cracks as the creature grows to an alarming size. It is now {size_desc}'
            )
        if c > 2:
            lines.append(
                f'With a sound like a lobster being fed through a paper shredder, the creature\'s carapace shatters. This exposes muscles made of strange metallic fillaments, which swell grotesquely even as you watch. It\'s not just the muscles. You can see "bones" shooting out so fast that they rip the creature open in a grisley spectacle of pulsing tissue and spurting black blood, but the damage is healed just as quickly as new tissue spins itself out of nowhere. It is now {size_desc}'
            )
        return lines 

    def abom_5(self):
        """+1 to Dexterity and Constitution modifier"""
        # c = get_count(self.rolls, 5) + self.rank
        lines = []
        dex_desc = ''
        const_desc = ''
        if self.size < 2:
            lines.append("The creature's small size belies it's surprising nimbleness!")
        if self.dexterity_mod == 1:
            dex_desc = 'surprising dexterity'
        elif self.dexterity_mod == 2:
            dex_desc = 'astonishing dexterity'
        elif self.dexterity_mod == 3:
            dex_desc = 'superhuman dexterity'
        elif self.dexterity_mod > 3:
            dex_desc = 'terrifying, inhuman dexterity'
        
        if self.constitution_mod < 3:
            const_desc = 'shakes off the trauma of its transformation you can guess that it\'s pretty hardy.'
        elif self.constitution_mod == 3:
            const_desc = 'doesn\'t really seem to notice when the powercell it\'s chewing on explodes in it mouth, you can guess that it\'s...sturdy.'
        elif self.constitution_mod > 3:
            const_desc = 'doesn\'t really seem to notice when the metadimensional rift that spawned it begins belching out radioactive plasma, you feel pretty safe in guessing that it\'s frighteningly robust.'
        lines.append(
            f'The creature moves with {dex_desc}, and from the way it {const_desc}'
        ) 
        return lines

    def abom_7(self):
        # Calculate AC
        extra_rolls = []
        c = get_count(self.rolls,7)
        attr_vals = [1,4,5,6]
        for i in range(c):
            roll = random.choice(attr_vals)
            extra_rolls.append(roll)
            self.ac += 1
        return extra_rolls

    def abom_8(self):
        c = get_count(self.rolls,8)
        for i in range(c):
            self.number = self.number * 2


    def abom_6(self):
        """+1 to Wisdom and Charisma modifier"""
        "Wisdom: Noticing things, making judgments, reading situations, intuition"
        "Charisma: Commanding, charming, attracting attention, being taken seriously"
        lines = []
        wis_desc = 'Quite aside from intelligence is its alertness and awareness of its environment. '
        char_desc = ''
        if self.wisdom_mod < -1:
            wis_desc += 'The creature seems too focused on a single target to pay proper attention to its surroundings.'
        elif self.wisdom_mod == -1:
            wis_desc += 'The creature is easily distracted, and seems to have difficulty dividing its attention between its target and its surroundings.'
        elif self.wisdom_mod == 0:
            wis_desc += 'The creature seems to have average awareness, focusing on its target while keeping a wary eye on its surroundings.'
        elif self.wisdom_mod == 1:
            wis_desc += 'The creature focuses intently on its target while remaining acutely aware of its surroundings.'
        elif self.wisdom_mod == 2:
            wis_desc += 'From the way it adjusts its posture and positioning in response to movement from anyone in the room, you can tell that it has exceptional situational awareness.'
        elif self.wisdom_mod == 3:
            wis_desc += 'The creature makes small adjustments to its posture and positioning, seeming to anticipate where you will go before you\'ve fully decided yourself. It has superhuman situational awareness, and you have no doubt that it is aware of the exact location of every person and weapon in the room.'
        elif self.wisdom_mod > 3:
            wis_desc += 'The creature makes small adjustments to its posture and positioning, not only anticipating your moves and resituating itself to be better prepared, but seeming to do so with a lazy, effortless grace. It is terrifyingly, inhumanly aware of its surroundings and your intentions.'

        lines.append(wis_desc)

        if self.charisma_mod < -1:
            char_desc += 'The hideous creature is an abomination, and you have no compunctions about putting an end to the horror. It is a stain on the universe that you will be glad to see expunged.'
        elif self.charisma_mod == -1:
            char_desc += 'The loathsome thing is pitiful. You almost feel sorry for it.'
        elif self.charisma_mod == 0:
            char_desc += 'It has a certain gravity to it, and the way it looks at you with a certain tilt to its head makes it feel almost human.'
        elif self.charisma_mod == 1:
            char_desc += 'Despite the horrifying intermediary steps, the creature eventually settles into a form that feels "normal", more like a thing humans might make. '
        elif self.charisma_mod == 2:
            char_desc += 'Despite the horrifying intermediary steps, the being eventually settles into a form that feels like an organic whole. Something that feels like the product of terrestrial evolution, though realized in gleaming metal. When it looks at you now, the eyes do not seem like the windows to an inhuman, alien mind, but to a very human seeming soul. If you want to harm it, you will have to come to terms with the fact that the act of destroying it will be morally inseperable murder.' 
        elif self.charisma_mod == 3:
            char_desc += 'Despite the horrifying intermediary steps, the being has settled into a form that is gleaming. Perfect. Its mirrored surface glows softly with a light that, through some deep chain of genetic memory, reminds you of the moonlight of an Old Earth you have never known.  When you look into its eyes, you see a person looking back at you. Though this being may not have evolved on any planet, destroying it would be murder. And beyond that - it has an almost superhuman majesty, and the thought of destroying something so beautiful fills you with sadness. Makes you feel like the worst kind of vandal.'
        elif self.charisma_mod > 3:
            char_desc += 'The creature radiates such powerful majesty that it\'s a struggle to keep from falling to your knees. But while you may be able to resist - for now, anyway - the way the electronic devices in the immediate area pause, as though listening to something you cannot hear, makes you think that it may have found other supplicants to bow to its commanding presence.'
        lines.append(char_desc)
        return lines

def roll_twice(l,n):
    extra_rolls = []
    for i in range(2):
        roll = randrange(10)
        if roll == n:
            print('roll:', roll)
            extra_rolls += roll_twice(l,n)
        else:
            extra_rolls.append(roll)
    return extra_rolls

def abom_9(l,n):
    """Roll again twice"""
    extra_rolls = []
    c = get_count(l,n)
    for i in range(c):
        extra_rolls += roll_twice(l,n)
    return extra_rolls

def get_count(l, n):
    return sum([i == n for i in l])