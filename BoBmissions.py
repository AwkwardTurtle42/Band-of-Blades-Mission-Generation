from random import randint,choice

def missionName():
	first = ['Azure','Amber','Broken','Chosen','Crimson','Diamond','Emerald','Flying','Grasping','Screaming','Shattered',]
	
	second = ['Arrow','Citadel','Fire','Hawk','Light','Mountain','Western','Peak','Storm','Thorn','Tiger','Wing','Wolf']
	return choice(first) + ' ' + choice(second)

def details(mtype,augmented=False):
	if mtype == 'Assault':
		types = ['People','The Wild','Undead','Undead','Powerful Unead','Powerful Undead']
		rewards = ['+2 Morale','+3 Morale','+4 Morale','+2 Morale, +1 Supply','+2 Morale, +1 Intel','+2 Morale, -1 Time']
		penalties = ['+1 Pressure, +1 Time','+1 Time','-1 Supply','+1 Pressure','+1 Pressure','+1 Pressure']
		return [types[d6(augmented)],rewards[d6(augmented)],penalties[d6(augmented)]]
	if mtype == 'Recon':
		types = ['Area Recon','Route Recon','Troop Recon','Infiltration','Exfiltration','Pick One (Area, Route, Troop, Infiltration, Exfiltraion) + Danger']
		rewards = ['+2 Intel','+2 Intel','Asset, +1 Intel','Asset or Troops, +1 Intel','+1 Intel, -1 Time','+3 Intel']
		penalties = ['+1 Time','2 Deaths','1 Death','+1 Pressure','+1 Pressure','None']
		return [types[d6(augmented)],rewards[d6(augmented)],penalties[d6(augmented)]]
	if mtype == 'Religious':
		types = ['Escort','Cleansing','Defense','Unearth','Pick One (Escort, Cleansing, Defense, Unearth) + Favor: ' + favor(),'Pick One (Escort, Cleansing, Defense, Unearth) + Favor: ' + favor()]
		rewards = ['-1 Time, +2 xp','+2 Morale +10 Points','+1 Intel, +2 Morale','Fine Asset','Exceptional Asset','Specialist']
		penalties = ['-1 Morale, +1 Pressure','+1 Pressure','+1 Pressure','-1 Morale','-1 Morale','None']
		return [types[d6(augmented)],rewards[d6(augmented)],penalties[d6(augmented)]]
	if mtype == 'Supply':
		types = ['Scrounge or Trade','Scrounge or Trade','Rescue Supplies','Rescue Supplies','Mercenary Work','Mercenary Work']
		rewards = ['Asset, +1 Supply','Asset, +1 Supply','+2 Supply','Asset, +2 Supply','+3 Supply','+3 Supply']
		penalties = ['-1 Morale, -1 Supply','-1 Supply','-1 Morale','-1 Morale','None','None']
		return [types[d6(augmented)],rewards[d6(augmented)],penalties[d6(augmented)]]

def d6(augmented=False,available=None):
	if available is None:
		available = [0,1,2,3,4,5]
	roll = sorted([0,randint(0,5) + int(augmented == True),5])[1]
	while roll not in available and roll < 6:
		roll+=1
	return roll

def favor():
	favors = ['Holy','Mystic','Glory','Knowledge','Mercy','Wild']
	return favors[d6()]

def missionCount():
	count = [[3],[3],[3,'+1 Specialist'],[2],[3,'Favor'],[3,'Special Mission']]
	return count[d6()]

def missionType(commander_focus = 'Assault',GM_choice = 'Assault',available=None):
	missions = ['Assault','Recon','Religious','Supply',commander_focus,GM_choice]
	return missions[d6(available=available)]

def locationAvailability(location):
	if location == None:
		return [0,1,2,3,4,5]

	location = location.lower()
	if location == 'western front':
		available = [0,1]
	elif location == 'plainsworth':
		available = [0,1,2,3]
	elif location == 'long road':
		available = [0,1]
	elif location == 'barrak mines':
		available = [0,1,3]
	elif location == 'gallows pass':
		available = [0,1,2]
	elif location == 'sunstrider camp':
		available = [0,1]
	elif location == 'duresh forest':
		available = [0,1,2]
	elif location == 'talgon forest':
		available = [1,2]
	elif location == 'westlake':
		available = [0,1,2,3]
	elif location == 'eastlake':
		available = [0,1,2,3]
	elif location == 'fort calisco':
		available = [0,1,2,3]
	elif location == 'the maw':
		available = [0,2]
	elif location == 'high road':
		available = [0,1]
	else:
		return [0,1,2,3,4,5]

	available += [4,5]

	return available


def genMissions(commander_focus = 'Assault',GM_choice = 'Assault',augmented=False,intel=False,location=None):
	if intel:
		num = [3,'Special Mission']
	else:
		num = missionCount()

	available = locationAvailability(location)

	for i in range(num[0]):
		if i == 0:
			print(*['-']*30)
			if len(num) > 1:
				if num[1] == 'Special Mission':
					if intel:
						print("Mission 1: Special Mission of Commander's Choice")
					else:
						print("Mission 1: Special Mission of GM's Choice")
				elif num[1] == '+1 Specialist':
					mtype = missionType(commander_focus = commander_focus,GM_choice = GM_choice,available=available)
					mission = details(mtype)
					print("Mission 1: Operation {}\nRequires extra specialist.\n{} Mission. Type: {}\nRewards: {}\nPenalties: {}".format(missionName(), mtype,*mission))
				elif num[1] == 'Favor':
					mtype = missionType(commander_focus = commander_focus,GM_choice = GM_choice,available=available)
					mission = details(mtype)
					print("Mission 1: Operation {}\nGrants {} Favor.\n{} Mission. Type: {}\nRewards: {}\nPenalties: {}".format(missionName(), favor(),mtype,*mission))
			else:
				mtype = missionType(commander_focus = commander_focus,GM_choice = GM_choice,available=available)
				if augmented and mtype == commander_focus:
					mission = details(mtype,augmented)
					augmented = False
				else:
					mission = details(mtype)
				print("Mission 1: Operation {}\n{} Mission. Type: {}\nRewards: {}\nPenalties: {}".format(missionName(),mtype,*mission))
		else:
			print(*['-']*30)
			mtype = missionType(commander_focus = commander_focus, GM_choice = GM_choice,available=available)
			if augmented and mtype == commander_focus:
				mission = details(mtype,augmented)
				augmented = False
			elif augmented and i == num[0] - 1:
				print(commander_focus)
				mtype = commander_focus
				mission = details(mtype,augmented)
				augmented = False
			else:
				mission = details(mtype)
			print("Mission {}: Operation {}\n{} Mission. Type: {}\nRewards: {}\nPenalties: {}".format(i+1,missionName(),mtype,*mission))


## To generate missions
genMissions(commander_focus = 'Supply', GM_choice = 'Supply',location='plainsworth')
