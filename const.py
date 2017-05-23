
# Thanks to http://mirekw.com/rs/RSDOnline/Guides/guide.aspx?file=Experience%20formula.html for the formula
def _build_xp_table():
	table = [0]
	xp = 0

	for level in range(1, 99):
		diff = int( level + 300 * ( 2 ** ( level / 7.0 ) ) )
		xp += diff
		table.append(xp // 4)

	return table

# index retrives the amount of xp required for level index + 1
XP_TABLE = _build_xp_table()


SKILLS = ["attack", "defence", "strength", "hitpoints", "ranged", "prayer", "magic", 
          "cooking", "woodcutting", "fletching", "fishing", "firemaking", "crafting", 
          "smithing", "mining", "herblore", "agility", "thieving", "slayer", "farming",
          "runecrafting", "hunter", "construction"]

SKILLS_AMT = len(SKILLS)

# Allows for efficient querying of membership
SKILLS_SET = set(SKILLS)

# Allows us to get the index of a skill from the name
SKILLS_MAP = {s : f for f, s in enumerate(SKILLS)}

HISCORE_URL = "http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player="