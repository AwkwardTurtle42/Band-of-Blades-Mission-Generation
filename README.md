# Band-of-Blades-Mission-Generation

Python script to generate missions for the Band of Blades role playing game.
All description and content taken from the Band of Blades rulebook.

## To use:

Run the genMissions() function. Options are: 

commander_focus which can be ('Assault', 'Recon', 'Religious', or 'Supply')

GM_choice which can be ('Assault', 'Recon', 'Religious', or 'Supply')

Set augmented=True if the Spymaster has augmented the mission generation.

Set intel=True if the Commander has spent intel.

location = the location you are currently at in Aldermark, which restricts which missions are available.

#### Example:

To create missions for my group which just arrived in Plainsworth, with the Commander looking for Supply missions (I agreed) I used:

```python
genMissions(commander_focus = 'Supply', GM_choice = 'Supply',location = 'plainsworth')
```

Which output:

<pre>
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Mission 1: Operation Crimson Peak
Grants Mercy Favor.
Supply Mission. Type: Scrounge or Trade
Rewards: +2 Supply
Penalties: -1 Morale
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Mission 2: Operation Diamond Hawk
Recon Mission. Type: Infiltration
Rewards: +2 Intel
Penalties: None
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Mission 3: Operation Screaming Thorn
Religious Mission. Type: Defense
Rewards: +2 Morale +10 Points
Penalties: -1 Morale, +1 Pressure
</pre>

If I wanted to generate a single mission details, for instance if I wanted to change the GM choice after I saw what was generated automatically, I'd use

```python
details(commander_focus = 'Religious')
```

## Functions:

#### missionName()

Uses the tables from pg 329 to create fun operation names for your missions.

#### details(mtype,augmented=False)

Creates the details of a mission, given the type ('Assault', 'Recon', 'Religious', or 'Supply') and whether or not the spymaster has augmented the mission generation. Content from pgs. 312-313.

#### d6(augmented=False,available=None)

Returns an integer from 0 through 5. augmented increases the roll by 1, up to a max of 5. available accepts a list of the possible results (bounded by 0-5), if a roll is not on the list 1 will be added to it until it is.

#### favor()

Returns one of the possible favor types of missions ('Holy','Mystic','Glory','Knowledge','Mercy', or 'Wild')

#### missionCount()

Returns the results of the mission count table on pg 312. Returned is a list, first value of which is the number of missions, second value is the special modifier if any.

#### missionType(commander_focus = 'Assault',GM_choice = 'Assault',available=None)

Returns the type of mission ('Assault', 'Recon', 'Religious', or 'Supply'), taking into account the commander's focus, the GM's choice and which missions are available (mapped to 0-3 plus 4,5).

#### locationAvailability(loation)

Returns the 'available' list to be used with other functions based on the available missions at a given location (pg. 120).

#### genMissions(commander_focus = 'Assault',GM_choice = 'Assault',augmented=False,intel=False,location=None)

Generates a full set of missions and prints them out. Takes the commaner's focus, the GM's choice, whether the spymaster has augmented the rolls, whether the commander has spent intel, and what the current location is.
