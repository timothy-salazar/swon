import random
from random import randrange
from abomination import Abomination
import re

RANK = 1
SIZE = 0

def get_body_part():
    body_parts = [
        'abdomen',
        'spine',
        'buttocks',
        'chest',
        'face',
        'head',
        'mouth',
        'arm',
        'hand',
        'eye',
        'foot',
        'leg',
        'ear'
    ]
    return random.choice(body_parts)

def get_color():
    colors = ['Almond','Antique Brass','Apricot','Aquamarine','Asparagus','Atomic Tangerine','Banana Mania','Beaver','Bittersweet','Black','Blue','Blue Bell','Blue Green','Blue Violet','Blush','Brick Red','Brown','Burnt Orange','Burnt Sienna','Cadet Blue','Canary','Caribbean Green','Carnation Pink','Cerise','Cerulean','Chestnut','Copper','Cornflower','Cotton Candy','Dandelion','Denim','Desert Sand','Eggplant','Electric Lime','Fern','Forest Green','Fuchsia','Fuzzy Wuzzy','Gold','Goldenrod','Granny Smith Apple','Gray','Green','Green Yellow','Hot Magenta','Inchworm','Indigo','Jazzberry Jam','Jungle Green','Laser Lemon','Lavender','Macaroni and Cheese','Magenta','Mahogany','Manatee','Mango Tango','Maroon','Mauvelous','Melon','Midnight Blue','Mountain Meadow','Navy Blue','Neon Carrot','Olive Green','Orange','Orchid','Outer Space','Outrageous Orange','Pacific Blue','Peach','Periwinkle','Piggy Pink','Pine Green','Pink Flamingo','Pink Sherbert','Plum','Purple Heart','Purple Mountain\'s Majesty','Purple Pizzazz','Radical Red','Raw Sienna','Razzle Dazzle Rose','Razzmatazz','Red','Red Orange','Red Violet','Robin\'s Egg Blue','Royal Purple','Salmon','Scarlet','Screamin\' Green','Sea Green','Sepia','Shadow','Shamrock','Shocking Pink','Silver','Sky Blue','Spring Green','Sunglow','Sunset Orange','Tan','Tickle Me Pink','Timberwolf','Tropical Rain Forest','Tumbleweed','Turquoise Blue','Unmellow Yellow','Violet','Violet Red','Vivid Tangerine','Vivid Violet','White','Wild Blue Yonder','Wild Strawberry','Wild Watermelon','Wisteria','Yellow','Yellow Green','Yellow Orange']
    return random.choice(colors)
    
def environmental_mishap(n):
    mishaps = [
        'A fog begins to roll in. It is alive with skittering, whispering shadows. They tell you not to be afraid. They tell you over and over again that "It won\'t hurt. It won\'t hurt."',
        'All light sources seem to grow painfully bright and become tinged with strange, otherworldly hues. Anyone who spends a turn within 10 feet of a bright light source will begin taking damage, as though from a very bad sunburn or a radiation burn.',
        'Different eras of radio and television are broadcast over compads, radios, and television, making communication difficult.',
        'Doors, windows, and containers slam shut and lock themselves.',
        'Monstrous forms moving through impossible geometries are visible on the other side of windows and mirrors.',
        'People appear normal enough, but their physical form is in fact a kind of skin bag stuffed with animals. This will become apparent if their skin is cut or torn (i.e., if they take enough non-bludgeoning damage) when the animals come spilling out like the cotton batting out of a ripped teddy bear.',
        'Plants turn to glass.',
        'Dead people call on nearby compads, telephones, and radios.',
        'Fabric within the area begins to disintigrate. Roll 1d10 to determine disintigration rate. Ordinary clothing, backpacks, tents, and other mundane fabrics will be destroyed within [disintrigration rate] turns. Some armor may begin to take damage as well, but at a slower rate. Secure Clothing might be destroyed within 3 x [disintigration rate] turns, for example. The GM can substitute some other material on a capricious whim.',
        'Food bleeds, sometimes screams.',
        'Animals speak in strange, unearthly tongues.',
        'The spaces which doors and other portals open onto are randomly shuffled.',
        'Complex mathematical formulas appear on walls, and are correct.',
        'Complex mathematical formulas appear on walls, and contain subtle flaws.',
        'Mirrors reflect the past instead of the present.',
        'Strange moons and stars can be seen in the sky.',
        'Eggs hatch with strange inanimate objects inside them.',
        'Liquids fall upward and pool on the ceiling.',
        'Birds fly backwards',
        'Boxes, containers, doors, and windows open on their own, even if locked.']
    pass

"""
swim through the air as though it were water,
jingles and catchy tunes dramatically accelerate the effects of entropy on inanimate matter,
everyone astrally projects to the surface of the nearest moon. Their physical bodies will move around in synchrony with their astral form, and their astral form on the moon will be blocked by obstacles which impede their physical form.
The player/people appears normal enough, but their skin is a bag stuffed with creatures which will come spilling out if cut. 
The dead rise and:
    - pyramid schemes
    - telemarketing
"""

def temporary_mishap(n):
    mishaps = [
        'Leaves trail of slime',
        'Cannot leave room while anyone is watching',
        "A soothing voice narrates the player's actions over nearby comm channels/loudspeakers/intercoms",
        'Birds near the player speak their thoughts and intentions',
        "If anyone else would see the player in a reflection or video stream, they instead see the player brutally murdering them",
        'Cannot lie',
        'Plants will attempt to grab the player',
        'Anyone the player touches becomes temporarily magnetic',
        'Phobia',
        'Whatever the player says carves itself into nearby surfaces',
        'Must speak in rhymes',
        'Must obey a polite request. They also acquire an indefinable "what a helpful looking young man/lady/lizard" quality about them.',
        'Uncontrollably attracts friendly (or at least neutral) wildlife.',
        'Cannot cross a threshold without announcing their presence',
        "All the player's hair grows at 2d6 feet/scene",
        'Player shrinks to 1/(1d6)th their original size',
        'Every piece of furniture that sees the player will fall in love with them, and will begin slowly inching towards them. This is likely to make exiting a building by the same route they entered more difficult. Any piece of furniture they touch (for example, if they sit in a chair) will emit a soft, contented purring sound.',
        "A miscellaneous collection of wallets and other personal valuables within one convenience unit teleport into the player's backpack, sack, purse, or whatever other recepticle they might have. The player has no idea this is happening. Their surprise, should the gendarmerie ask to see what's in that bulging backpack, will be genuine.",
        'Heightened hearing',
        'Control clocks (not time, clock displays)']
    pass

def permanent_mishap(n):
    mishaps = [
        'The player acquires an embarassing nickname that everyone they meet instinctively knows.',
        'Transparent skin',
        'Joints make a sound like popping bubblewrap when moving',
        'Feet are replaced with:',
        'Rubber bones',
        'Eye stalks',
        'No shadow*',
        'Squirt ink when alarmed',
        'Clothes',
        'Glows',
        '1d6 extra digits',
        'Covered in leaves. May grow fruit.',
        'The player can "see" with sonar, but only by screaming very loudly',
        'Can puff up like a pufferfish',
        'Webbed fingers and toes',
        'Protective eyelids',
        'Vomit at will',
        'Removable eyeballs',
        'Pouch',
        'Slighty taller']
    pass


'*Anyone studying this phenomenon with powerful, hi-tech sensors will probably go insane and try to build a machine that destroys life.'



def get_env_stats(rank, roll):
    start = rank-1
    stop = int(5 + (10-(roll-1))/2)
    roll = randrange(start, stop)
    duration_list = [
        'One turn',
        'A few turns',
        'One scene',
        'A few scenes',
        'A day',
        'A few days',
        'A week',
        'A month', 
        'A year',
        'Permanent'
    ]
    area_list = [
        'A room sized area',
        'A building sized area',
        'A block sized area',
        'A neighborhood sized area',
        'A town sized area',
        'A large city sized area',
        'A continent sized area',
        'Half of a planet',
        'A planet sized area',
        'A star system sized area'
    ]
    duration = duration_list[randrange(start, stop)]
    area = area_list[randrange(start, stop)]
    text = f'  Area of Effect: {area}\n  Duration: {duration}\n'
    return text



def get_permanent_mishap(start=0, stop=9):
    permanent_mishaps = [
        ['"But you screw one goat..."','The player acquires an embarassing nickname that everyone they meet instinctively knows.'],
        ['Invisible Skin','The player\'s skin becomes transparent. If you like looking gruesome, congrats! Otherwise, you can probably get by with makeup (though you may want to get in the habit of carrying an umbrella with you)'],
        ['The player\'s joints make a sound like popping bubblewrap when moving'], #
        ['Linnaeus would have a fit',f"The player\'s {random.choice(['feet','legs','hands','arms','head'])} is/are replaced with those of a {random.choice(['bird','lizard','robot','some mammal','squid'])}"],
        ['Rubber bones','The player\'s bones are made of rubber. This makes it harder to stand up straight and use their muscles properly. Strength is reduced, but they can fit into tight spaces easier.'],
        ['Eye stalks'],
        ['No shadow*'],
        ['Amazing squid powers','The player will squirt ink when alarmed'],
        ['Clothes','The player appears to be wearing clothes, but this is actually just the appearance of its naked skin. It can still wear clothes over top of its garment-resembling skin, of course.'],
        ['Glows', 'The player emits a soft but noticeable glow.'],
        ['Buying gloves is about to start sucking',f'{random.randrange(1,7)} extra digits'],
        ['Covered in leaves. May grow fruit.'],
        ['Batman','The player can "see" with sonar, but only by screaming very loudly'],
        ['Full of hot air','Can puff up like a pufferfish'],
        ['Webbed fingers and toes'],
        ['Protective eyelids'],
        ['Vomit at will'],
        ['Removable eyeballs'],
        ['Pouch'],
        ['Slighty taller']
        ]


def mishap(rank=RANK, size=SIZE, spacing='  '):


    permanent_mishaps = [
        'The player acquires an embarassing nickname that everyone they meet instinctively knows.',
        'The player\'s skin becomes transparent. If you like looking gruesome, congrats! Otherwise, you can probably get by with makeup (though you may want to get in the habit of carrying an umbrella with you)',
        'The player\'s joints make a sound like popping bubblewrap when moving', #
        'The player\'s feet are replaced with:',
        'The player\'s bones are made of rubber. This makes it harder to stand up straight and use their muscles properly. Strength is reduced, but they can fit into tight spaces easier.',
        'Eye stalks',
        'No shadow*',
        'Squirt ink when alarmed',
        'Clothes',
        'Glows',
        '1d6 extra digits',
        'Covered in leaves. May grow fruit.',
        'The player can "see" with sonar, but only by screaming very loudly',
        'Can puff up like a pufferfish',
        'Webbed fingers and toes',
        'Protective eyelids',
        'Vomit at will',
        'Removable eyeballs',
        'Pouch',
        'Slighty taller'
        ]


# def get_temporary_mishap(start=0, stop=9):
#     note = """Temporary effects are effects that are too mean/annoying to keep track of to make permanent. The metadimensional charge should wear off soon-ish."""
    temporary_mishaps = [
        'The player turns into a corgi.',
        'The player cannot leave a room while anyone is looking at them.',
        "A soothing voice narrates the player's actions over nearby comm channels/loudspeakers/intercoms.",
        'Birds near the player speak their thoughts and intentions.',
        "If anyone else would see the player in a reflection or video stream, they instead see the player brutally murdering them",
        'The player cannot lie', #
        'Plants will attempt to grab and restrain the player', #
        'Anyone the player touches becomes temporarily magnetic',
        'Phobia', #
        'Whatever the player says carves itself into nearby surfaces.',
        'The player must speak in rhymes.',
        'The player must obey a polite request. They also acquire an indefinable "what a helpful looking young man/lady/lizard" quality about them.',
        'Uncontrollably attracts friendly (or at least neutral) wildlife.', #
        'The player cannot cross a threshold without announcing their presence',
        "All of the player's hair grows at 2d6 feet/scene.",
        f'The player shrinks to 1/{random.randrange(2,7)}th of their original size.',
        'Every piece of furniture that sees the player will fall in love with them, and will begin slowly inching towards them. This is likely to make exiting a building by the same route they entered more difficult. Additionally: any piece of furniture they touch (for example, if they sit in a chair) will emit a soft, contented purring sound.',
        "A miscellaneous collection of wallets and other personal valuables within one convenience unit teleport into the player's backpack, sack, purse, or whatever other recepticle they might have. The player has no idea this is happening. Their surprise, should the gendarmerie ask to see what's in that bulging backpack will be genuine.",
        'Heightened hearing', #
        'The player gains an amazing and dangerous power! They have control over clocks! (not time, just clocks. Mostly displays, but if they really focus they can set off an alarm clock. Also: computers don\'t count as clocks just because they display the time - that\'s not their primary purpose, you munchkins)']
    # mishap = random.choice(temporary_mishaps[start:stop])
    # return f"""&{{template:default}} {{{{name=Temporary Effect}}}} {{{{Note={note}}}}} {{{{Effect={mishap}}}}}"""

# def get_environmental_mishap(rank, roll, start=0, stop=9):
    environmental_mishaps = [
        'A fog begins to roll in. It is alive with skittering, whispering shadows. They tell you not to be afraid. They tell you over and over again that "It won\'t hurt. It won\'t hurt."',
        'All light sources seem to grow painfully bright and become tinged with strange, otherworldly hues. Anyone who spends a turn near a bright light source within the area of effect ("near" depends on the brightness of the source) will begin taking damage, as though from a very bad sunburn or a radiation burn.',
        'Different eras of radio and television are broadcast over compads, radios, and television, making communication difficult.',
        'Doors, windows, and containers slam shut and lock themselves.',
        'Monstrous forms moving through impossible geometries are visible on the other side of windows and mirrors.',
        'People appear normal enough, but their physical form is in fact a kind of skin bag stuffed with animals. This will become apparent if their skin is cut or torn (i.e., if they take enough non-bludgeoning damage) when the animals come spilling out like the cotton batting out of a ripped teddy bear.',
        'Plants turn to glass.',
        'Dead people call on nearby compads, telephones, and radios.',
        'Fabric within the area begins to disintigrate. Roll 1d10 to determine disintigration rate. Ordinary clothing, backpacks, tents, and other mundane fabrics will be destroyed within [disintrigration rate] turns. Some armor may begin to take damage as well, but at a slower rate. Secure Clothing might be destroyed within 3 x [disintigration rate] turns, for example. The GM can substitute some other material on a capricious whim.',
        'Food bleeds, sometimes screams.',
        'Animals speak in strange, unearthly tongues.',
        'The spaces which doors and other portals open onto are randomly shuffled.',
        'Complex mathematical formulas appear on walls, and are correct.',
        'Complex mathematical formulas appear on walls, and contain subtle flaws.',
        'Mirrors reflect the past instead of the present.',
        'Strange moons and stars can be seen in the sky.',
        'Eggs hatch with strange inanimate objects inside them.',
        'Liquids fall upward and pool on the ceiling.',
        'People and animals can swim through the air as though it were water',
        'Boxes, containers, doors, and windows open on their own, even if locked.']
    # mishap = random.choice(environmental_mishaps[start:stop])
    # duration, area = get_env_stats(rank, roll)
    # return f"""&{{template:default}} {{{{name=Environmental Mishap}}}} {{{{Area={area}}}}} {{{{Duration={duration}}}}} {{{{Effect={mishap}}}}}"""

# def mishap(rank=RANK, size=SIZE, spacing='  '):
    lines = []
    roll = randrange(10)
    print(f'You rolled a {roll+1} on the SCIENTIFIC MISHAP table:\n')
    if roll == 0:
        ab = Abomination(rank, size)
        lines.append('You fool!!!\nThere is a terrible surge of INCOMPREHENSIBLE METADIMENSIONAL ENERGIES centered on the device! You are thrown back from the furious vortex of power your carelessness has unleashed, and as you look on in horror you see that the device is not destroyed, but rather TWISTED AND MUTATED! It seems to be ANIMATED by the surge of power, becoming a SCIENTIFIC ABOMINATION!!!\n')
        lines.append(ab.get_lines())
    if roll == 1:
        lines.append('Environmental Mishap:\n' \
            + get_env_stats(rank, roll) \
                + spacing + 'Effect: ' + random.choice(environmental_mishaps[:10]) + '\n')
        lines.append('Temporary-ish Mishap:\n'+ spacing + random.choice(temporary_mishaps[:10]) + '\n')
        lines.append('Semi-Permanent Mishap:\n'+ spacing + random.choice(permanent_mishaps))
    elif roll == 2:
        lines.append('Environmental Mishap:\n' \
            + get_env_stats(rank, roll) \
                + spacing + 'Effect: ' + random.choice(environmental_mishaps) + '\n')
        lines.append('Temporary-ish Mishap:\n' \
            + spacing + random.choice(temporary_mishaps) + '\n')
        lines.append('Semi-Permanent Mishap:\n'+ spacing + random.choice(permanent_mishaps))
    elif roll == 3:
        lines.append('Temporary-ish Mishap:\n' + spacing + random.choice(temporary_mishaps) + '\n')
        lines.append('Semi-Permanent Mishap:\n' + spacing + random.choice(permanent_mishaps))       
    elif roll == 4:
        lines.append('Environmental Mishap:\n' \
            + get_env_stats(rank, roll) \
                + spacing + 'Effect: ' + random.choice(environmental_mishaps) + '\n')
        lines.append('Semi-Permanent Mishap:\n'+ spacing + random.choice(permanent_mishaps))
    elif roll == 5:
        lines.append('Semi-Permanent Mishap:\n'+ spacing +  random.choice(permanent_mishaps))
    elif roll == 6:
        lines.append('Environmental Mishap:\n' \
            + get_env_stats(rank, roll) \
                + spacing + 'Effect: ' + random.choice(environmental_mishaps) + '\n')
        lines.append('Temporary-ish Mishap:\n'+ spacing + random.choice(temporary_mishaps))
    elif roll == 7:
        lines.append('Temporary-ish Mishap:\n'+ spacing +  random.choice(temporary_mishaps[10:]))
    elif roll == 8:
        lines.append('Environmental Mishap:\n' \
            + get_env_stats(rank, roll) \
                + spacing + 'Effect: ' + random.choice(environmental_mishaps[10:]))
    elif roll == 9:
        lines.append('Nothing super bad happens. As the device triggers you have a sense of narrowly averted catastrophe.')

    lines = '\n'.join(lines)
    if 'No shadow*' in lines:
        lines += '\n\n*Note: anyone studying this phenomenon with powerful, hi-tech sensors will probably go insane and try to build a machine that destroys life.'
    return lines

    '''0 The device becomes a SCIENTIFIC ABOMINATION (see below).
    1 Roll 1d10 on the Environmental and Temporary Mishap tables. Roll 1d20 on the Moderately Permanent Mishap table.
    2 Roll once on the Environmental, Temporary, and Moderately Permanent Mishap tables. The GM can choose to roll a d10 on one of them if they want to keep things spicy.
    3 Roll once on the Temporary and Moderately Permanent Mishap tables.
    4 Roll once on the Environmental and Moderately Permanent Mishap tables.
    5 Roll once on the Moderately Permanent Mishap tables.
    6 Roll once on the Environmental and Temporary Mishap tables.
    7 Roll 1d10 + 10 on the Temporary Mishap table.
    8 Roll 1d10 + 10 on the Environmental Mishap table
    Nothing super bad happens. As the device triggers you have a sense of narrowly averted catastrophe.'''

def cut_title(x):
    m = re.match('^[A-Za-z -]+?:',x)
    if m:
        index = m.span()[1]
        return x[:index], x[index:]

def cut_description(x):
    m = re.search('.*\n[A-Z]', x)
    if m:
        index = m.span()[0] + 1
        return x[:index], x[index:]
    else:
        return x, ''

def format_lines(x):
    return [f'{i}' for i in x.split('\n') if i]

def html_mishap(rank=RANK, size=SIZE):
    x = mishap(rank, size)
    if x[:8] == 'You fool':
        # Oh no...
        return [{'title':'Scientific Abomination',
                'lines':x}]
    output = []
    while True:
        title, x = cut_title(x)
        d, x = cut_description(x)
        output.append(
            {'title':title,
            'lines':format_lines(d)})
        if not x:
            break
    return output