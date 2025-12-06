#EG, 2nd Period, Larry's Comeback

# Larry's Comeback

# Variables
# player_name = "Larry"                     
# fixed protagonist name
# current_location = "Goblin Stadium"       
# starting arena
# game_running = True                       
# controls main loop
# final_boss_defeated = False               
# set True when Mega Knight falls

# player_stats: dictionary containing all primary stats
#   player_stats = {
#       "level": 1,                         
        # starting level
#       "xp": 0,                            
        # experience points
#       "coins": 0,                         
        # currency for leveling/items
#       "health": 100,                      
        # current HP
#       "max_health": 100,                  
        # max HP based on level/items
#       "strength": 10,                     
        # base attack stat
#       "defense": 5,                       
        # base defense stat
#       "speed": 5,                         
        # affects fleeing / initiative
#       "crit_chance": 0.05                 
        # chance to deal critical hit
#   }

# XP and coin progression constants
#   XP_TO_LEVEL_BASE = 100                 
# base XP needed for level 2
#   XP_GROWTH_FACTOR = 1.5                 
# XP needed scales by this factor per level
#   COIN_COST_PER_LEVEL_BASE = 20          
# base coin cost for level-ups
#   COIN_COST_GROWTH = 1.7                 
# coin cost scales per level

# high-damage threshold constant (used for conditional #1)
# HIGH_DAMAGE_THRESHOLD = 15             
# any computed damage >= this is "high damage"

# cards_collection: LIST of card descriptors (meets list requirement)
#   Each card descriptor = { "name", "damage", "type", "desc" }
#   Example entries:
#       {name: "Skeleton Spear", damage: 8, type: "melee", desc: "Quick jab, low damage"}
#       {name: "Archer Volley",  damage: 6, type: "ranged", desc: "Ranged shots, can hit flying"}
#       {name: "Mega Minion",    damage: 18, type: "flying", desc: "Strong flying attacker"}
#       {name: "P.E.K.K.A Strike", damage: 25, type: "melee", desc: "Heavy single target"}
#   cards_collection used by show_cards() and some scripted arena encounters

# inventory: LIST, starts empty
#   inventory stores item names and optionally small metadata (uses remaining)
#   examples of inventory items:
#       "Small Potion" is  consumable, heals 25 HP
#       "Strength Elixir" is consumable, +6 strength for next battle (one use)
#       "Larry's Shield" is equippable/permanent, +8 defense permanently
#       "Coin Pouch" is consumable, +30 coins when used
#       "Mega Minion Sigil" is special item that unlocks/boosts Mega Minion card in Builder's Workshop
#       "Boot Camp Badge" is required to enter Legendary Arena (after boss 4)
#       "Golem Core" is special key item from Hog Mountain used to unlock shortcuts

# items_taken: DICTIONARY mapping item_name -> True/False (prevents respawn)
# defeated_enemies: LIST of defeated standard enemies (prevents re-fight)
# defeated_bosses: LIST of bosses defeated (prevents boss re-fight and triggers unlocks)
# friends_met: DICTIONARY mapping friend_name -> True/False (so helpers do one-time rewards)
# visited_arenas: LIST to track which arenas visited (for text variations / quests)

# arena_map: DICTIONARY keyed by arena_name
#   Example arena_map entry structure:
#       arena_map["Goblin Stadium"] = {
#           "description": "Description text...",
#           "paths": ["Bone Pit", "Barbarian Bowl"],
#           "item": "Small Potion",
#           "friend": "Friendly Archer",
#           "enemy": "Goblin Squad",
#           "boss": None,
#           "locked": False,
#           "unlock_requirements": None
#       }
#   All arenas from your list will be created similarly with unique content.

# boss_unlocks: DICTIONARY mapping boss_name -> list of arenas to unlock when defeated
#   e.g., boss_unlocks["Skeleton Dragons"] = ["P.E.K.K.A.'s Playhouse", "Royal Arena"]


# Derived and used formulas (explicit detail)
#   1. Level-up XP requirement: xp_required_for_next = floor(XP_TO_LEVEL_BASE * (XP_GROWTH_FACTOR ** (player_stats["level"] - 1)))
#   2. Coin cost to level up: coin_cost_for_next = floor(COIN_COST_PER_LEVEL_BASE * (COIN_COST_GROWTH ** (player_stats["level"] - 1)))
#   3. Max health formula on level up: new_max_health = player_stats["max_health"] + 20  # flat +20 per level
#   4. Stat increases per level (example): on level up:
#           player_stats["strength"] += 3
#           player_stats["defense"] += 2
#           player_stats["speed"] += 1 every two levels (optional)
#   5. Damage calculation base: raw_damage = attacker_strength + card_damage_modifier - defender_defense * defense_factor
#       where:
#           attacker_strength = player_stats["strength"] or enemy strength
#           card_damage_modifier = damage value from chosen card (if using cards)
#           defense_factor = 0.5 (example) meaning defender_defense reduces damage partially
#       Enforce minimum_damage = 1
#   6. Critical hits:
#       roll = random number [0,1]
#       if roll <= attacker.crit_chance:
#           damage = damage * 1.5  # critical multiplier
#   7. Temporary buffs:
#       Strength Elixir grants +X strength for specified combat rounds or next combat only
#       Defense buff from "Larry's Shield" is permanent and applied on pickup
#   8. Healing cap: when adding health via potion, health cannot exceed max_health


# Items 
# "Small Potion":
#   type: consumable
#   effect: heals 25 HP when used
#   flavor: "A bubbling potion brewed by arena healers."
#
# "Strength Elixir":
#   type: consumable (temporary)
#   effect: +6 strength for the next 3 combat rounds or next combat (design choice)
#   flavor: "A bitter tonic that sharpens your bones' strikes."
#
# "Larry's Shield":
#   type: permanent/equippable
#   effect: +8 defense applied immediately on pickup
#   flavor: "A tarnished shield once owned by a legendary skeleton knight."
#
# "Coin Pouch":
#   type: consumable
#   effect: grants +30 coins on use
#   flavor: "A pouch stitched from tournament banners — surprisingly heavy."
#
# "Mega Minion Sigil":
#   type: special
#   effect: unlocks or upgrades Mega Minion card in Builder's Workshop; may allow summoning a temporary ally in one fight
#   flavor: "A rune that hums with the memory of winged knights."
#
# "Boot Camp Badge":
#   type: key item
#   effect: unlocks Legendary Arena entrance
#   flavor: "Worn by champions of the boot camp; the gatekeeper respects it."


# Abilities
# Abilities unlocked by helpers or bosses are persistent and stored in abilities_unlocked
# Example abilities:
#   "Arc Blast": one-time ranged AoE that deals moderate damage to all minor enemies (from Wandering Mage)
#   "Whirl Attack": cost energy, deals high melee damage to single target and reduces enemy defense for next turn (from Sergeant)
#   "Spectral Ally": temporary ally that deals X damage for two rounds (from Friendly Ghost)
# Abilities may have cooldowns or charge counts;


# Friend or Helper text and rewards
# Friendly Archer (Goblin Stadium)
#   Dialogue sequence:
#       "Hey skeleton! You look lost. Here, take my bow; it never sees daylight."
#       "If you ever need an arrow, come back and I’ll spare a few."
#   Reward:
#       Option A: Give player an Archer card (adds to cards_collection)
#       Option B: Give +5 coins
#   friends_met["Friendly Archer"] = True after interaction

# Bone Wizard (Bone Pit)
#   Dialogue:
#       "The bones whisper secrets. I can bind a strand to your ribs, grant you fortified bonework."
#   Reward:
#       On acceptance: +2 defense permanent (applied immediately) and a Small Potion
#   friends_met["Bone Wizard"] = True

# Barbarian Trainer (Barbarian Bowl)
#   Dialogue:
#       "A few hard swings and your strikes will sting. Push, skeleton!"
#   Reward:
#       One-time training: +1 permanent strength
#   friends_met["Barbarian Trainer"] = True

# Wandering Mage (Spell Valley)
#   Dialogue:
#       "A spark for a weary attacker. Learn this and harness the valley."
#   Reward:
#       Teach ability "Arc Blast" (add to abilities_unlocked) and give Mana Flask (item)
#   friends_met["Wandering Mage"] = True

# Tinker (Builder's Workshop)
#   Dialogue:
#       "Everything has a cog. Here—this sigil will make a winged thing favor you."
#   Reward:
#       Give Mega Minion Sigil (special item); small coin reward or repair kit
#   friends_met["Tinker"] = True

# Hog Wrangler (Hog Mountain)
#   Dialogue:
#       "Steady on—these beasts bite back. I'll lend you aid for the right price."
#   Reward:
#       Temporary mount in next fight (gives +2 speed and +2 strength for one combat) or give Golem Core
#   friends_met["Hog Wrangler"] = True

# Spark Engineer (Electro Valley)
#   Dialogue:
#       "Tinker a wire here and a spark there—take this grenade, it'll jolt 'em good."
#   Reward:
#       Give Shock Grenade (consumable) and +10 coins
#   friends_met["Spark Engineer"] = True

# Friendly Ghost (Spooky Town)
#   Dialogue:
#       "I was a champion once. I will stand with you one time."
#   Reward:
#       Spectral Ally (ability or temporary companion that attacks for two rounds), consumable flag consumed on use
#   friends_met["Friendly Ghost"] = True

# Old Miner (Miner's Mine)
#   Dialogue:
#       "We dug up things best left buried. Here, take this—pair of old coins and a key."
#   Reward:
#       Give Miner’s Pick (item) and +20 coins
#   friends_met["Old Miner"] = True

# Sergeant (Boot Camp)
#   Dialogue:
#       "Discipline builds bone. One more rep, skeleton!"
#   Reward:
#       Complete a training trial (mini-challenge) that grants +1 strength and Boot Camp Badge on success
#   friends_met["Sergeant"] = True

# COMBAT SYSTEM — DETAILED FORMULATION
# Main combat function signature: combat(actor, enemy)
# actor may be player or allied helper (for temporary companions)
# enemy includes enemy_stats = {health, strength, defense, speed, type, special_moves}
# Combat loop detailed:
#   Set player_temp_bonuses = {temp_strength: 0, temp_defense: 0, rounds_remaining: 0}
#   Set enemy_temp_bonuses similarly if needed
# While player_stats["health"] > 0 and enemy["health"] > 0:
#       Display round header with both HP values and statuses
#       Display available actions:
#           1) Attack (choose basic attack or choose a card from cards_collection; cards may have limited uses in scripted fights)
#           2) Defend (gain defend_flag that reduces next incoming damage by extra factor)
#           3) Use Item (open inventory, call use_item)
#           4) Use Ability (if abilities_unlocked; check cooldown/charges)
#           5) Attempt to Flee (allowed for standard enemies, not bosses; success when player speed > enemy speed * random factor)
#
#       Player action branch:
#           If Attack:
#               If using a card:
#                   card_damage = card["damage"]
#                   attack_type = card["type"]
#                   base_attacker_strength = player_stats["strength"]
#                   computed_damage = compute_damage(base_attacker_strength, card_damage, enemy["defense"], attack_type)
#               Else (basic attack):
#                   computed_damage = compute_damage(player_stats["strength"], 0, enemy["defense"], "melee")
#
#               Apply critical hit check:
#                   roll = random(0,1)
#                   if roll <= player_stats["crit_chance"]:
#                       computed_damage = floor(computed_damage * 1.5)
#                       log "Critical hit!"
#
#               Apply computed_damage to enemy["health"]
#
#           If Defend:
#               set defend_flag = True for player this round (reduces damage by extra percentage, e.g., +30% effective defense)
#
#           If Use Item:
#               call use_item(item_choice) -> effects apply immediately
#
#           If Use Ability:
#               check ability charges / energy costs:
#                   if enough energy/charges -> apply effect (damage, buff, ally summon)
#                   else -> print "Not ready"
#
#           If Attempt to Flee:
#               flee_roll = random(0,1) + player_stats["speed"]*0.01
#               threshold = 0.5 + enemy["speed"]*0.01
#               if flee_roll > threshold:
#                   print "You escaped"
#                   break combat loop and return "escaped"
#               else:
#                   print "Flee failed! Enemy attacks for free."
#
#       After player's action:
#           If enemy["health"] <= 0:
#               process_enemy_death() -> award xp, coins, drop items if any, append enemy to defeated_enemies, break combat loop
#
#       Enemy turn (only if alive):
#           Enemy decides action (pattern or random)
#           enemy_attack_type = enemy["type"]  # e.g., "melee", "ranged", "flying"
#
#           Range/Type conditional (explicit conditional #2):
#               IF enemy_attack_type == "ranged":
#                   apply ranged_damage_modifier = 0.7 to player's defense (player defense counts less)
#               ELSE:
#                   apply ranged_damage_modifier = 1.0 (normal defense application)
#
#           raw_enemy_damage = compute_damage(enemy["strength"], 0, player_stats["defense"], enemy_attack_type)
#           If player defend_flag is True:
#               raw_enemy_damage = floor(raw_enemy_damage * 0.6)  # defend reduces damage by 40% additionally
#
#           Subtract raw_enemy_damage from player_stats["health"]
#
#       End of round: reduce durations for temporary buffs, abilities, and defend_flag resets
#
#   End combat loop
#
#   If player_stats["health"] <= 0:
#       return "dead"
#   If enemy["health"] <= 0:
#       return "victory"
#   If escaped:
#       return "escaped"
#
# compute_damage(attacker_strength, card_damage, defender_defense, attack_type) detailed:
#   # Basic raw = attacker_strength + card_damage
#   raw = attacker_strength + card_damage
#   # Defense mitigation
#   defense_effective = defender_defense * 0.5  # defense_factor
#   damage_after_def = raw - defense_effective
#   # Ensure minimum damage
#   if damage_after_def < 1:
#       damage_after_def = 1
#   # DAMAGE CHECK conditional (explicit conditional #1):
#   if damage_after_def >= HIGH_DAMAGE_THRESHOLD:
#       damage_category = "high"
#       # High damage special effects:
#       #   - high damage may partially ignore a percentage of defense (already applied) or cause stagger
#   else:
#       damage_category = "low"
#   return floor(damage_after_def), damage_category

# Combat thingy
# Scenario: Larry (strength=12, defense=6, health=60) vs. Workshop Golem (strength=10, defense=4, health=40, type="melee")
# Round 1:
#   show_stats -> Larry HP 60/100, Golem HP 40/40
#   Player chooses Attack using "Skeleton Spear" card with damage 8 (melee)
#   compute_damage:
#       raw = attacker_strength (12) + card_damage (8) = 20
#       defense_effective = enemy_defense (4) * 0.5 = 2
#       damage_after_def = 20 - 2 = 18
#       damage_category check: 18 >= HIGH_DAMAGE_THRESHOLD(15) -> "high"
#   Apply critical check (assume no crit)
#   Enemy health reduces: 40 - 18 = 22
#   Enemy still alive -> enemy's turn
#   Enemy attack calculation:
#       compute_damage(enemy_strength=10, card_damage=0, defender_defense=6, attack_type="melee")
#       raw = 10
#       defense_effective = 6 * 0.5 = 3
#       damage_after_def = 10 - 3 = 7
#       since 7 < HIGH_DAMAGE_THRESHOLD -> "low"
#   Larry health reduces: 60 - 7 = 53
#   End Round 1: log "Larry dealt 18 (high) to Golem. Golem dealt 7 (low) to Larry."
#
# Round 2:
#   Player chooses Defend -> defend_flag True
#   Enemy attacks with slam (attack strength 12)
#       compute_damage raw = 12, defense_effective=6*0.5=3 => 9
#       defend_flag reduces to floor(9 * 0.6) = 5
#   Larry health reduces: 53 - 5 = 48
#   End Round 2
#
# Round 3:
#   Player uses Strength Elixir (+6 for this combat), strength becomes 18 for calculation
#   Player attacks with basic attack:
#       raw = 18 + 0 = 18
#       defense_effective = 4 * 0.5 = 2
#       damage_after_def = 16 ("high")
#   Enemy HP reduces: 22 - 16 = 6
#   Enemy attacks, but health still > 0, compute and apply damage...
#   Round continues until one reaches 0

# Ex: Boss phase change skeleton dragons
# Skeleton Dragons stats: health 150, phase thresholds at 100 and 40
# Phase 1 (150->101):
#   Behavior: sweeping melee with moderate damage; occasional wing gust that deals area minor damage
# Phase 2 (100->41):
#   Behavior: flame breath (ranged) that partially ignores defense; summons small skellings
#   Attack type changes to "ranged": Range/Type conditional applies (defense less effective)
# Phase 3 (40->0):
#   Behavior: enraged slam with very high damage and stun chance; increased speed
# On each phase change:
#   Print cinematic text and adjust enemy_stats accordingly
# On defeat:
#   Award big XP, coins, Dragon Scale item (permanent +5 defense), and unlock next arena group

# Player items and like feedback
# When picking up item:
#   Print: "You found a [item_name]! Flavor text describing it. (Added to inventory.)"
# When meeting helper:
#   Print helper dialogue lines, then print "You received [reward]."
# When attempting to enter locked arena:
#   Print: "The path forward is blocked. Requirement: [unlock_requirements]. You must defeat [boss] or obtain [item]."
# When leveling up possible:
#   Print: "You have enough XP for level [next_level]. Do you want to spend [coin_cost] coins to level up? (Y/N)"
# When an invalid movement chosen:
#   Print: "You can't go that direction. Try a listed path."

# Game restart, save, and end game
# On death:
#   Print defeat cinematic, show stats summary (level, XP, coins, bosses defeated, items collected)
#   Prompt: "Restart? Y/N"
# On victory (defeat Mega Knight):
#   Print victory cinematic, final score, option to restart
# restart_game():
#   Reset all global variables to initial start_game() values and call main loop again
# quit_game():
#   Set game_running = False and exit program loop

# Functions list
# start_game()
# main_game_loop()
# show_stats()
# show_cards()
# show_card_stats(card)
# check_type(card_or_attack)
# level_up()
# pick_up_item(item_name)
# use_item(item_name)
# friend_interaction(friend_name)
# compute_damage(attacker_strength, card_damage, defender_defense, attack_type)
# combat(enemy_name, enemy_stats)
# boss_battle(boss_name, boss_stats)
# enter_arena(arena_name)
# move_to(target_arena)
# restart_game()
# game_over()
# win_game()

# Arena 1: Goblin stadium
# description:
#   "screeching stands of cracked wood and patched banners. A dirt floor
#    ringed by toppled seats. The echoes of past matches hang in the air.
#    Small fires still burn in a few braziers. This arena is designed
#    as the first tutorial area where Larry practices basic moves."
#
# flavor notes:
#   - The crowd is long gone; the bones of old battle dummies rest where
#     goblins once cheered. Ranks of broken wooden poles form cover spots.
#
# content:
#   item: "Small Potion"
#       description: "A bubbling potion brewed by arena healers. Restores 25 HP."
#       placed_on_map: True (only one)
#       xp_value_when_found: 0 (items don't grant XP, but help in fights)
#   friend: "Friendly Archer"
#       dialogue:
#           1) "Hey skeleton, look alive! I can't stand the noise alone."
#           2) "Take this arrow bundle; it saved me in the last skirmish."
#       reward: either give "Archer Card" (adds to cards_collection) OR +5 coins
#       friend_flag: friends_met["Friendly Archer"] = True after interaction
#   enemy: "Goblin Squad"
#       enemy_stats:
#           health: 20
#           strength: 6
#           defense: 2
#           speed: 4
#           type: "melee"
#       xp_reward: 10
#       coin_reward: 5
#   boss: None
#   paths: ["Bone Pit", "Barbarian Bowl"]
#   locked: False
#
# interactions & behavior:
#   on_enter:
#       - call show_stats()
#       - if "Small Potion" not in items_taken:
#           prompt: "You see a Small Potion on the ground. Pick up? (Y/N)"
#           if Y -> call pick_up_item("Small Potion") -> inventory append; items_taken["Small Potion"]=True
#       - if friends_met["Friendly Archer"] is False:
#           offer friend_interaction("Friendly Archer")
#       - if "Goblin Squad" not in defeated_enemies:
#           offer combat("Goblin Squad", enemy_stats)
#               sample combat turn example (see below)
#   movement:
#       - show available paths to "Bone Pit" and "Barbarian Bowl"
#       - allow player to choose where to go
#
# sample combat turn (Goblin Squad):
#   initial player_stats example: health=100, strength=10, defense=5
#   enemy: health=20, strength=6, defense=2
#   round 1:
#       player chooses Attack (basic)
#       compute_damage:
#           raw = player_strength (10) + card_damage (0) = 10
#           defense_effective = enemy_defense (2) * 0.5 = 1
#           damage = 10 - 1 = 9 -> damage_category = "low" if < HIGH_DAMAGE_THRESHOLD
#       enemy_health = 20 - 9 = 11
#       enemy attacks:
#           raw_enemy = 6; defense_effective_player = 5 * 0.5 = 2.5 -> damage = 6 - 2.5 = 3 (min 1)
#           player_health = 100 - 3 = 97
#   round 2:
#       player uses "Small Potion"? (if in inventory)
#       else player attacks and finishes enemy
#   victory:
#       add "Goblin Squad" to defeated_enemies
#       grant player_stats["xp"] += 10
#       grant player_stats["coins"] += 5
#
# design notes:
#   - Goblin Stadium is forgiving. Combat teaches attack/defend/item usage.
#   - Friend gives the player an early card or coins to show reward loops.


# Arena 2 Bone pit
# description:
#   "A pit of interlocking femurs and jawbones. Occasional steam rises
#    from cracks in the ground. The crunch of bones underfoot is constant.
#    Echoes create strange acoustics, making ranged attacks sometimes miss."
#
# content:
#   item: "Band of Bones"
#       description: "A braided band of bone shards that laces around the ribs.
#                     Grants +2 permanent defense when equipped."
#   friend: "Bone Wizard"
#       dialogue:
#           1) "Quiet, Larry. The bones remember the strikes of old."
#           2) "Let me bind you with bonework—your frame will hold longer."
#       reward: +2 defense permanently and 1 Small Potion
#   enemy: "Skelly Patrol"
#       enemy_stats:
#           health: 30
#           strength: 8
#           defense: 3
#           speed: 3
#           type: "melee"
#       xp_reward: 18
#       coin_reward: 8
#   boss: None
#   paths: ["Goblin Stadium", "Barbarian Bowl", "Spell Valley"]
#   locked: False
#
# interactions & behavior:
#   environmental hazard:
#       - certain tiles apply minor poison damage (e.g., 2 HP) unless player chooses careful traversal
#       - players may choose "step carefully" action that reduces movement speed (narrative effect)
#   item interaction:
#       - pick_up_item("Band of Bones") sets items_taken and immediately applies player_stats["defense"] += 2
#   helper:
#       - friend_interaction("Bone Wizard") triggers dialogue and gives defense + potion
#   enemy combat:
#       - if encounter "Skelly Patrol", use combat() with their stats
#       - sample special enemy move: "Bone Throw" (ranged low damage) - causes Range/Type conditional where defense less effective
#
# sample combat turn (Skelly Patrol uses Bone Throw):
#   Player attacks first; suppose player deals 12 damage -> enemy hp reduces accordingly
#   Enemy uses Bone Throw (type "ranged")
#       Range/type conditional applies:
#           player_effective_defense = floor(player_stats["defense"] * 0.7) # ranged less effective
#       compute_damage with defense reduced -> may deal slightly more damage
#   reward on victory: xp + coins; optionally rare drop chest with small chance

# Arena 3 Barbarian Bowl
# description:
#   "A circular arena lined with crude training dummies and kettlebells.
#    Loud grunts and shouts echo. Barbarians test each other and newcomers."
#
# content:
#   item: "Barbarian Protein"
#       description: "A raw bundle that burns with fury. Consumable: +10 strength for next combat only."
#   friend: "Barbarian Trainer"
#       dialogue:
#           1) "If you're going to swing bones, swing with purpose."
#           2) "I'll put you through a strike—one trial, one gain."
#       reward: +1 permanent strength on completion of a short trial (simple stat check or small combat)
#   enemy: "Barbarian Recruits"
#       enemy_stats:
#           health: 28
#           strength: 9
#           defense: 3
#           speed: 4
#           type: "melee"
#       xp_reward: 20
#       coin_reward: 10
#   boss: None
#   paths: ["Goblin Stadium", "Bone Pit", "Spell Valley"]
#   locked: False
#
# interactions & behavior:
#   trainer trial:
#       - mini-challenge: "Do 3 practice strikes" simulated by choosing "attack" 3 times
#       - success grants +1 strength permanent; trainer removed from giving reward again
#   item usage:
#       - Barbarian Protein presents a choice: "Use now?" (recommended before tough enemy)
#   combat nuances:
#       - Barbarians favor heavy single-target attacks; occasional "Rally" to temporarily increase their strength by +2 for one round
#
# sample combat turn vs Barbarian Recruits:
#   Round 1: player attacks -> damage computed; barbarians may "rally" (buff) on their turn making next round riskier
#   Round 2: player uses Barbarian Protein (if had it) to power through; temporary strength raises damage significantly
#   Reward: xp and coin payout; optional drop of "Minor Weapon Part"

# Arena 4 Spell Valley
# description:
#   "Floating runes, pulsing glyphs, and a humming sky. Magic feels thick here;
#    ranged attacks can be both amplified and deflected. This arena introduces
#    ranged enemies and introduces the concept of 'abilities' to the player."
#
# content:
#   item: "Mana Flask"
#       description: "A crystal vial that restores 5 energy or one ability charge."
#   friend: "Wandering Mage"
#       dialogue:
#           1) "A careful hand holds power without burning."
#           2) "Take this: arcane knowledge for a ribcage. Use it wisely."
#       reward: teaches ability "Arc Blast" (adds to abilities_unlocked) and gives 1 Mana Flask
#   enemy: "Apprentice Wizard"
#       enemy_stats:
#           health: 24
#           strength: 7
#           defense: 2
#           speed: 5
#           type: "ranged"
#       xp_reward: 22
#       coin_reward: 12
#   boss: None
#   paths: ["Barbarian Bowl", "Builder's Workshop"]
#   locked: False
#
# interactions & behavior:
#   magic hazards:
#       - stepping on certain runes triggers a random small effect: heal 5 HP, zap 5 HP, or buff next attack
#   friend_interaction:
#       - Wandering Mage demonstrates "Arc Blast"; upon acceptance, add ability to abilities_unlocked
#       - teach how to spend "energy" to use abilities in combat; show ability cost and effect
#   enemy combat:
#       - Apprentices use ranged attacks; apply Range/Type conditional (ranged less fully mitigated by defense)
#       - Apprentices sometimes cast "Magic Shield" raising defense for a round
#
# sample combat turn vs Apprentice Wizard where player uses Arc Blast (if learned):
#   Player uses "Arc Blast" ability (cost: 2 energy)
#       effect: deals 18 area magic damage (acts like high damage)
#       check compute_damage with card_damage = 18 and attack_type = "ranged"
#       result likely >= HIGH_DAMAGE_THRESHOLD -> damage_category = "high"
#       if enemy dies: reward xp/coins and possibly a minor drop
#   Enemy turn: if alive uses "Magic Missile" dealing small damage

#Arena 5 Builder's Workshop Boss Battle
# description:
#   "A cavernous workshop of half-built contraptions and smashed bellows.
#    The smell of ash hangs heavy. Colossal metal ribs line the walls.
#    Here lurks the first arena boss: the Skeleton Dragons."
#
#content:
#   item: "Mega Minion Sigil"
#       description: "A winged rune that binds a single Mega Minion spirit to your cause.
#                     When activated in Builder's Workshop, it grants a one-fight ally or permanently
#                     enhances the Mega Minion card (design choice)."
#   friend: "Tinker"
#       dialogue:
#           1) "Cogs and bones. You look like you need a lift."
#           2) "This sigil will make a winged thing remember you—use it at the right time."
#       reward: give "Mega Minion Sigil" and +10 coins; friends_met["Tinker"] = True
#   enemy: "Workshop Golems"
#       enemy_stats (minions spawned around boss):
#           health: 30
#           strength: 8
#           defense: 4
#           speed: 3
#           type: "melee"
#       xp_reward: 30 (each)
#       coin_reward: 15 (each)
#   boss: "Skeleton Dragons"
#       boss_stats initial:
#           total_health: 150 (multi-head HP may be split logically across phases)
#           phase_thresholds: [100, 40]  # phase changes at these HP values
#           base_strength: 20
#           base_defense: 8
#           speed: 6
#           type: "flying" in some phases, "ranged" in breath phase, "melee" in slam phase
#       boss_specials:
#           - Phase 1: "Wing Sweep" (melee-area attack hitting all targets)
#           - Phase 2: "Flame Breath" (ranged attack that partially ignores defense; applies burn status)
#           - Phase 3: "Tail Slam" (massive single-target damage + stun chance)
#       boss_rewards_on_defeat:
#           - XP: 250
#           - coins: 150
#           - item: "Dragon Scale" (permanent +5 defense)
#           - unlocks: set boss_unlocks["Skeleton Dragons"] -> unlock ["P.E.K.K.A.'s Playhouse", "Royal Arena"]
#
# boss encounter flow:
#   pre-boss:
#       - Tinker offers the Mega Minion Sigil and a small hint: "When they breathe, the floor cools—use that moment."
#       - Player can pick up any remaining items in Builder's Workshop
#       - Warn player to prepare (level up, use items) before initiating boss_battle()
#   boss_battle sequence (detailed):
#       - Phase 1 (150 -> 101):
#           boss uses Wing Sweep (melee) occasionally and summons two Workshop Golems at 125 HP mark
#           enemies have lower HP; defeat them to reduce incoming pressure
#       - Phase 2 (100 -> 41):
#           boss switches to Flame Breath (ranged): apply range/type conditional; player's defense is partially bypassed (defense_effective = defense * 0.6)
#           Flame Breath applies "burn" that deals 5 HP per round for 2 rounds (stacking avoided)
#       - Phase 3 (40 -> 0):
#           boss enrages: increases base_strength, uses Tail Slam that can stun Larry (skip player turn once)
#           introduce a risk-reward: if Larry staggers the boss (high damage threshold applied), boss drops to next phase with temporary vulnerability (defense lowered)
#       - boss mechanics ensure player must vary actions: attack, defend to avoid heavy blows, use items for sustain, and use abilities for burst damage
#
# boss example combat snippet:
#   Round 1: Larry attacks for 18 (high) -> boss HP 132
#   Boss Wing Sweep deals 12 to Larry -> Larry HP reduced accordingly
#   Round 2: Workshop Golems attack; Larry uses Strength Elixir -> increased damage next round
#   Round 3: Boss reaches 100 HP threshold -> prints cinematic "Bones clatter, breath warms the air" -> Phase 2 begins
#   Phase 2: Flame Breath hits for 25 but uses ranged rules -> if player defense is low, heavy damage; burn triggers 5 HP per round
#   Managing burn via Small Potion or resting between minor fights is key
#
# post-boss:
#   - On victory:
#       call pick_up_item("Dragon Scale") OR automatically apply player_stats["defense"] += 5
#       append "Skeleton Dragons" to defeated_bosses
#       unlock next group arenas by setting arena_map[unlocked]["locked"] = False for each
#       award xp and coins to player account
#       possible optional cutscene: Tinker bows, "The wings remember your name."
#   - On defeat:
#       call game_over() flow (offer restart)
#
# design notes:
#   - Builder's Workshop is a gatekeeper: fighting here without sufficient stats or items (potions, shield) will likely lead to player death
#   - Encourages backtracking: if player can't beat boss, they should explore earlier arenas, gather coins/xp, level up, and return
#   - Mega Minion Sigil is thematic: using it during the boss fight can provide a temporary ally (one-time) to distract the dragon for two rounds; requires design choice whether it's permanent enhancement or consumable ally

# Arena 11 Electro Valley
# description:
#   "A valley threaded with humming power lines and crackling pylons.
#    Sparks jump between metal posts. The ground vibrates with low electricity.
#    Strange machines and broken generators make eerie mechanical music."
#
# environment mechanics:
#   - Electrical arcs: random small shocks that deal 3-5 HP if player stands still too long.
#   - Metal surfaces increase chance for 'shock' status when hit by lightning attacks.
#
# items in arena:
#   - "Electric Core"
#       description: "A warm, pulsing core used for crafting and powering contraptions.
#                     Can be exchanged for coins or used in later puzzles."
#       effect: key component; no immediate stat boost
#   - "Shock Grenade"
#       description: "A fragile orb that emits an electrical burst. Consumable in combat.
#                     Deals 20 electrical damage to a single enemy; may stun small enemies for 1 turn."
#       effect: consumable; single use
#
# friend/helper:
#   - "Spark Engineer"
#       dialogue lines:
#           1) "Careful with your bones near live wires. Here, take this grenade."
#           2) "If you learn to time it, the sparks can be your ally."
#       reward:
#           - Give one Shock Grenade immediately
#           - Provide a small hint about the Electro Giant's vulnerability to rapid strikes
#       friend flag: friends_met["Spark Engineer"] = True after interaction
#
# enemies:
#   - "Arc Sparks" (swarm minions)
#       stats example: health 18, strength 6, defense 2, speed 6, type "ranged"
#       special: hit chance increased vs shields, small chance to chain damage to player for 2 extra HP
#       xp_reward: moderate
#   - "Stun Bot"
#       stats example: health 28, strength 9, defense 4, speed 3, type "melee"
#       special: has a chance to apply stun for 1 turn on player
#
# boss: None in this arena (part of the arena group unlocked by Hog Mountain)
#
# paths:
#   - Hog Mountain (if returning)
#   - Spooky Town
#   - Rascal's Hideout
#
# interactions
# def arena_electro_valley():
#     # Print arena description and ambient electrical sounds
#     # If Electric Core not taken:
#     #     Offer pickup; if accepted: pick_up_item("Electric Core")
#     # If Spark Engineer not met:
#     #     friend_interaction("Spark Engineer") -> grant Shock Grenade, hint
#     # For each enemy in arena not defeated:
#     #     Present encounter options: avoid, fight, or use item
#     #     If fight chosen: combat(enemy_stats)
#     # Random arc hazard:
#     #     On each 'wait' or long action, roll for electrical arc (3-5 damage)
#     # Show exits and prompt for movement choice
#     # Return chosen next arena


# sample combat turn in Electro Valley (using Shock Grenade):
#   - Player turns: choose Use Item -> Shock Grenade
#       compute_damage = 20 (special electrical) -> apply to Stun Bot
#       Stun Bot HP reduced accordingly; if dies, no counterattack
#   - If enemy survives and is stunned: skip enemy turn for 1 round

# Arena 12 Spooky Town
# description:
#   "Narrow cobblestone streets with leaning houses, fog, and flickering lamplight.
#    Whispered voices drift from alleyways. Lanterns flicker with ghostly blue flame."
#
# environment mechanics:
#   - Low visibility: ranged attacks suffer a small accuracy penalty unless player has Ghost Lantern
#   - Ghostly whispers: small chance each turn to cause 'confusion' status that swaps player's action order
#
# items:
#   - "Ghost Lantern"
#       description: "A lantern that reveals hidden spirits. Grants +15% accuracy for ranged attacks while lit."
#       effect: reusable item; passive when in inventory and 'lit' flag set
#   - "Ectoplasm Vial"
#       description: "A sticky vial that heals 30 HP when used in combat. Also cancels 'burn' or 'shock' on use."
#       effect: consumable healing item
#
# friend/helper:
#   - "Friendly Ghost"
#       dialogue lines:
#           1) "I used to cheer for kings. I will stand with you one time."
#           2) "Follow the blue flame and you will find a hidden passage."
#       reward:
#           - Grants 'Spectral Ally' ability: a temporary companion that deals 12 damage for two rounds
#           - Shows a secret path to Rascal's Hideout if player listens
#       friend flag: friends_met["Friendly Ghost"] = True after interaction
#
# enemies:
#   - "Phantom Horde" (groups)
#       stats example: each phantom: health 12, strength 5, defense 1, speed 6, type "ranged"
#       special: they ignore 50% of low defense if the player is "unlit"
#   - "Haunted Knight"
#       stats example: health 40, strength 12, defense 6, speed 3, type "melee"
#       special: resists stun very slightly
#
# boss: None at this arena
#
# paths:
#   - Electro Valley
#   - Rascal's Hideout
#   - Serenity Peak
#
# interactions:
# def arena_spooky_town():
#     # Print spooky description and fog effects
#     # If Ghost Lantern not taken:
#     #     Offer to pick up the Ghost Lantern
#     # If Friendly Ghost not met:
#     #     friend_interaction("Friendly Ghost") -> grant Spectral Ally ability
#     # If Phantom groups appear:
#     #     Offer combat or avoidance (flee mechanics)
#     # If Haunted Knight present and not defeated:
#     #     Offer combat (stronger fight)
#     # Remember low visibility rules: apply ranged accuracy penalty unless Ghost Lantern in inventory
#     # Show exits and prompt for movement choice
#     # Return chosen next arena


# sample combat turn vs Phantom Horde where Ghost Lantern not used:
#   - Player attacks with Archer card (ranged), accuracy reduced by 15%
#   - If miss, no damage done; otherwise proceed normally
#   - Phantoms have high speed so they often strike first next round

# Arena 13 
# description:
#   "A maze of crooked alleys and rooftop shacks. Rascals dart between shadows
#    and set traps for the unwary. The air smells of grease and mischief."
#
# environment mechanics:
#   - Traps: stepping on certain tiles triggers a trap dealing 5-8 damage unless player has 'Trap Disarm' skill or item
#   - Pickpocket attempts: small chance to lose a few coins in long interactions unless player has high speed
#
# items:
#   - "Rascal's Dagger"
#       description: "A light, wicked dagger that adds a chance to deal critical damage.
#                     Grants +10% crit chance when equipped."
#       effect: equippable; permanent crit chance increase
#   - "Smoke Bomb"
#       description: "A consumable that ensures escape success when used in combat."
#       effect: consumable; guarantee flee this combat
#
# friend/helper:
#   - "Sneaky Rascal"
#       dialogue lines:
#           1) "You got guts, skeleton. Here, learn to move like me."
#           2) "I won't ask for anything... much."
#       reward:
#           - Grants 'Dodge' passive: +8% dodge chance
#           - Gives one Smoke Bomb
#       friend flag: friends_met["Sneaky Rascal"] = True after interaction
#
# enemies:
#   - "Rascal Gang" (small groups)
#       stats example: health 16 each, strength 6, defense 2, speed 7
#       special: use hit-and-run tactics (first round attack then attempt to flee)
#   - "Trapmaster"
#       stats example: health 26, strength 8, defense 3, speed 4
#       special: sets traps that persist in arena until disarmed
#
# boss: None here
#
# paths:
#   - Spooky Town
#   - Serenity Peak
#   - Electro Valley
#
# interactions 
# def arena_rascals_hideout():
#     # Print hideout description and watch for traps
#     # If Rascal's Dagger not taken:
#     #     Offer pickup; equip if accepted and add crit chance
#     # If Sneaky Rascal not met:
#     #     friend_interaction("Sneaky Rascal") -> grant dodge passive and Smoke Bomb
#     # If Trapmaster or Rascals present:
#     #     Combat sequence or attempt to avoid
#     # Trap mechanics:
#     #     If player steps on trap tile and has no disarm skill:
#     #         Apply trap damage and mark tile as sprung
#     # Show exits and prompt movement choice
#     # Return chosen next arena


# sample combat turn vs Rascal Gang (hit-and-run):
#   - Round 1: Rascal attacks and attempts to flee
#       If flee succeeds: Rascal leaves the fight (no XP drop)
#       If fails: continues fight; player must adapt using abilities or Smoke Bomb to escape


# Arena 14 Serenity Peak
# description:
#   "A calm plateau with warm breezes, shallow pools, and soft chimes.
#    The place restores a weary warrior's resolve. Monks practice in silent circles."
#
# environment mechanics:
#   - Resting Pools: restore a small portion of HP or energy once per visit
#   - Meditation: temporary buff to XP gains for a limited time after meditating
#
# items:
#   - "Serenity Water"
#       description: "A vial of sacred water that restores 30 HP and 5 energy when used."
#       effect: consumable healing item
#   - "Meditation Bead"
#       description: "When used, increases XP gain by 20 percent for the next 3 battles."
#       effect: consumable buff item
#
# friend/helper:
#   - "Monk"
#       dialogue lines:
#           1) "Balance your strikes and mind, skeleton."
#           2) "Spend a moment here and you will find clarity."
#       rewards:
#           - Free heal at the fountain (one-time)
#           - Gives Meditation Bead or teaches a passive regeneration (small HP per round)
#       friend flag: friends_met["Monk"] = True after interaction
#
# enemies:
#   - "Peaceful Sentinels"
#       stats example: health 20, strength 6, defense 4, speed 3
#       note: more for training than for harm; low aggression
#
# boss: None here
#
# paths:
#   - Spooky Town
#   - Rascal's Hideout
#   - Miner's Mine (Arena 15)
#
# interactions
# def arena_serenity_peak():
#     # Print calm area description
#     # Offer to meditate:
#     #     If player meditates:
#     #         Apply XP buff for next 3 battles (increase xp by 20%)
#     #         Possibly restore a small amount of HP
#     # If Monk not met:
#     #     friend_interaction("Monk") -> free heal or Meditation Bead
#     # If Peaceful Sentinels present:
#     #     Combat or training options
#     # Show exits and prompt movement choice
#     # Return chosen next arena


# sample use case: player meditates then fights enemy in next arena:
#   - Player meditates at Serenity Peak, gains XP buff
#   - During next combat, when awarding base XP, multiply by 1.2 and add to player_stats["xp"]


# Arena 15 Miners Mine Boss number 3
# description:
#   "A winding mine with cavernous chambers. Sparks fly from charged rails.
#    Miners once lashed to the ore now haunt the halls. The Electro Giant pounds
#    through the ground with each movement, sending arcs of light and debris."
#
# items in arena:
#   - "Miner's Pick"
#       description: "A heavy pick used by miners, now enchanted. Can be used as a weapon or to break specific barriers."
#       effect: can unlock Executioner's Kitchen shortcut or be crafted into a weapon
#   - "Giant Battery" (drops from boss)
#       description: "A large, humming battery. Required for crafting and unlocking late-game devices."
#       effect: boss drop, key item
#
# helper/helper NPC:
#   - "Old Miner"
#       dialogue lines:
#           1) "We dug too deep for coin. But we kept tools. Take this pick, you'll need it."
#           2) "Watch the plates underfoot — the Giant's charge can shatter them."
#       reward:
#           - Gives Miner's Pick and +20 coins
#       friend flag: friends_met["Old Miner"] = True after interaction
#
# enemies:
#   - "Underground Miners" (groups)
#       stats example: health 24, strength 7, defense 3, speed 3
#       special: sometimes drop small coin pouches
#   - "Spark Beetle"
#       stats example: health 16, strength 5, defense 1, speed 6
#       special: small electrical damage on contact
#
# boss: ELECTRO GIANT
#   boss_stats:
#       total_health: 220
#       base_strength: 22
#       base_defense: 10
#       speed: 4
#       type: "melee" primarily, second phase uses "ranged electrical shock"
#   boss_specials:
#       - "Charge Slam": heavy area attack that deals 25-35 damage and can stagger player for one round
#       - "Electro Burst": ranged shock that ignores 25% of player's defense and applies 'shock' status for 2 rounds
#       - "Armor Plates": boss has armor segments that must be broken; until enough segments are broken, boss defense is higher
#   phases:
#       - Phase 1 (220 -> 151): heavy melee attacks, summons miner minions occasionally
#       - Phase 2 (150 -> 71): Electromagnetic field activates, reduces player defense effectiveness, boss does Electro Burst more often
#       - Phase 3 (70 -> 0): Armor plates cracked, boss enrages, attack speed and damage increase; may cause floor collapse hazards
#
# rewards on defeat:
#   - XP reward: 400
#   - coins: 300
#   - item drop: "Giant Battery"
#   - unlocks: Executioner's Kitchen and other advanced paths, and grants materials for later craft
#
# entry requirements:
#   - Might require "Golem Core" from Hog Mountain or can be accessed by default depending on player's path
#
# boss battle:
# def boss_electro_giant_battle():
#     # Pre-battle:
#     #     If Old Miner not met: offer his help; gain Miner's Pick and coins
#     #     Give player a chance to use items or retreat before battle
#
#     # Boss combat loop:
#     # while electro_giant_health > 0 and player_health > 0:
#     #     show_stats() and display boss HP and current phase
#     #     player chooses: Attack, Defend, Use Item, Use Ability, or Attempt Flee (flee not allowed vs bosses)
#     #
#     #     If player Attack:
#     #         If using weapon with armor-piercing property or high damage:
#     #             reduce armor plates count appropriately
#     #         Apply compute_damage(player_strength + weapon_modifier, card_damage, boss_defense)
#     #
#     #     If player Defend:
#     #         apply increased defense for this round
#     #
#     #     If player Use Item:
#     #         consume potion or Shock Grenade etc.
#     #
#     #     After player action:
#     #         if boss_hp <= phase_threshold_trigger:
#     #             transition phase and print cinematic text
#     #
#     #     Boss turn:
#     #         Decide between Charge Slam, Electro Burst, or summon minions based on phase and cooldowns
#     #         Apply Range/Type conditional for Electro Burst (ranged)
#     #         compute and subtract damage from player
#     #
#     #     End round: update temporary buffs, statuses, and check for player death
#
#     # On boss defeat:
#     #     Append "Electro Giant" to defeated_bosses
#     #     Give XP, coins, and drop "Giant Battery"
#     #     Unlock Executioner's Kitchen and other paths by setting arena_map[arena]["locked"] = False
#     #     Print major victory scene and possibly auto-level the player or give a large XP boost
#
# sample boss-combat snippet (numbers):
#   - Player strength = 18, defense = 8, health = 120
#   - Boss Phase 1: boss_strength = 22, boss_defense = 10, boss_hp = 220
#   - Player uses Strength Elixir (+6) and attacks with card_damage 12:
#       compute raw = 18 + 12 = 30
#       defense_effective = boss_defense * 0.5 = 5
#       damage = 30 - 5 = 25 -> damage_category = "high" (>= HIGH_DAMAGE_THRESHOLD)
#       boss_hp = 220 - 25 = 195
#   - Boss chooses Charge Slam:
#       compute boss_raw = 22
#       player_defense_effective = player_defense * 0.5 = 4
#       boss_damage = 22 - 4 = 18
#       player_health = 120 - 18 = 102
#   - Continue rounds until boss phases or dies
#
# design notes:
#   - Breaking armor plates should be tactical: some weapons or cards reduce plate count faster
#   - Summoned minions create distraction; use area attacks or abilities to clear them
#   - Electro Burst forces use of potions or defend actions to survive
#
# post-boss world changes:
#   - Executioner's Kitchen unlocked
#   - New crafting recipes become available that require Giant Battery
#   - Optional side-quests referencing Giant Battery appear in later arenas

# Arena 16 Exexutioners Kitchen
# description:
#   "A massive kitchen with gigantic cooking utensils, boiling cauldrons, and swinging meat cleavers.
#    Shadows move strangely across the walls. Steam clouds make visibility difficult."
#
# environment mechanics:
#   - Hot steam: deals 3-6 damage if player stays too long in one spot
#   - Swinging cleavers: occasional timed hazards that must be dodged (Dexterity check)
#
# items:
#   - "Chef's Cleaver"
#       description: "A heavy blade once used to butcher giants. Grants +12 attack damage when equipped."
#       effect: equippable weapon
#   - "Hot Sauce Vial"
#       description: "Can be thrown on enemy to increase their burn damage taken by 15% for 3 rounds."
#       effect: consumable buff item
#
# friend/helper:
#   - "Kitchen Golem"
#       dialogue lines:
#           1) "I only serve those who fight for the right cause. Here, take my cleaver."
#           2) "Careful not to slip on spilled oil."
#       reward:
#           - Gives Chef's Cleaver immediately
#           - Warns about hazards in Boot Camp arena
#       friend flag: friends_met["Kitchen Golem"] = True after interaction
#
# enemies:
#   - "Angry Sous Chef"
#       stats example: health 35, strength 10, defense 4, speed 4, type "melee"
#       special: can throw pots causing splash damage
#   - "Rolling Pin Minion"
#       stats example: health 20, strength 6, defense 2, speed 6, type "melee"
#       special: high chance to knockback player (delay next action)
#
# boss: None here
#
# paths:
#   - Miner's Mine
#   - Royal Crypt
#
# interactions:
# def arena_executioners_kitchen():
#     # Print kitchen description and hazards
#     # If Chef's Cleaver not taken:
#     #     Offer pickup
#     # If Kitchen Golem not met:
#     #     friend_interaction("Kitchen Golem") -> give weapon and hazard warning
#     # Combat sequences with minions or avoid using environment tactics
#     # Steam or swinging cleaver hazards trigger on timer/turn count
#     # Show exits and prompt movement choice

# Arena 17 Royal Crypt
# description:
#   "Ancient stone corridors filled with sarcophagi and royal tombs.
#    Candles flicker on the walls. Shadows of the past seem to whisper secrets."
#
# environment mechanics:
#   - Low light: reduces accuracy unless player has torch or Ghost Lantern
#   - Undead hands occasionally reach from coffins: chance of small damage or status 'grabbed'
#
# items:
#   - "Royal Key"
#       description: "Opens locked chests and passages; necessary for certain side quests."
#       effect: key item
#   - "Ancient Coin Pouch"
#       description: "A pouch of coins (50) hidden in sarcophagi."
#       effect: instant coin gain
#
# friend/helper:
#   - "Crypt Guardian"
#       dialogue lines:
#           1) "Few dare enter these halls. I will guide those worthy."
#           2) "Keep your steps quiet, or the dead may rise."
#       reward:
#           - Grants hint for hidden treasure and safe path
#           - Adds minor boost: +5 defense for next battle
#       friend flag: friends_met["Crypt Guardian"] = True after interaction
#
# enemies:
#   - "Skeleton Warrior"
#       stats example: health 25, strength 8, defense 5, speed 4, type "melee"
#   - "Crypt Wraith"
#       stats example: health 30, strength 12, defense 3, speed 6, type "ranged"
#       special: ignores half defense of player, deals 'fear' status reducing next attack by 50%
#
# boss: None
#
# paths:
#   - Executioner's Kitchen
#   - Silent Sanctuary
#   - Dragon Spa
#
# interactions:
# def arena_royal_crypt():
#     # Print eerie crypt description
#     # If Royal Key not taken:
#     #     Offer pickup
#     # If Ancient Coin Pouch not found:
#     #     Offer pickup, add coins to player
#     # If Crypt Guardian not met:
#     #     friend_interaction("Crypt Guardian") -> add defense bonus
#     # Combat encounters: Skeletons and Wraiths appear in sequence
#     # Apply low light rules: accuracy penalties if torch/lantern not equipped
#     # Show exits and prompt movement choice

# Arena 18 silent Sanctuary
# description:
#   "A serene but ominous temple with high ceilings, echoing footsteps, and frozen air.
#    Silence is almost tangible; even whispers can be heard."
#
# environment mechanics:
#   - Silence aura: reduces magic or ranged attack efficiency by 10%
#   - Sacred runes: stepping on them may heal or damage depending on the rune type
#
# items:
#   - "Rune Stone"
#       description: "Mystical stone that boosts magical attacks by +10 damage for next 3 battles."
#       effect: consumable buff
#   - "Healing Herb"
#       description: "Restores 40 HP when used; can be used in combat or out of combat."
#       effect: consumable healing item
#
# friend/helper:
#   - "Silent Monk"
#       dialogue lines:
#           1) "In silence, your heart beats louder. Take this stone."
#           2) "The shadows teach patience, the light teaches timing."
#       reward:
#           - Gives Rune Stone
#           - Provides insight on optimal attack sequence in next arena
#       friend flag: friends_met["Silent Monk"] = True after interaction
#
# enemies:
#   - "Silent Sentinels"
#       stats example: health 28, strength 9, defense 4, speed 4, type "melee"
#   - "Phantom Shadows"
#       stats example: health 20, strength 8, defense 2, speed 7, type "ranged"
#       special: chance to dodge first attack each turn
#
# boss: None
#
# paths:
#   - Royal Crypt
#   - Dragon Spa
#   - Boot Camp
#
# interactions:
# 
# def arena_silent_sanctuary():
#     # Print temple description and silence effects
#     # If Rune Stone not taken:
#     #     Offer pickup
#     # If Healing Herb not taken:
#     #     Offer pickup
#     # If Silent Monk not met:
#     #     friend_interaction("Silent Monk") -> Rune Stone + battle advice
#     # Combat: Silent Sentinels and Phantom Shadows; apply silence penalty
#     # Show exits and prompt movement choice

# Arena 19 Dragon Spa
# description:
#   "A tropical arena with warm waters, mist, and stone dragon statues.
#    The smell of herbs fills the air. Pools provide healing effects if rested in."
#
# environment mechanics:
#   - Hot spring pools: restore 20 HP once per visit
#   - Mist reduces ranged attack accuracy by 10%
#
# items:
#   - "Dragon Scale"
#       description: "Hard, iridescent scale from a dragon statue; adds +10 defense if equipped."
#       effect: equippable defense item
#   - "Healing Crystal"
#       description: "Consumable that restores 50 HP instantly."
#       effect: consumable healing item
#
# friend/helper:
#   - "Dragon Spirit"
#       dialogue lines:
#           1) "I guard the waters. Respect them and I will aid you."
#           2) "Rest well here; the next challenge will test all you learned."
#       reward:
#           - Restores 40 HP
#           - Gives Dragon Scale
#       friend flag: friends_met["Dragon Spirit"] = True after interaction
#
# enemies:
#   - "Aqua Serpents"
#       stats example: health 22, strength 8, defense 3, speed 5, type "ranged"
#   - "Steam Golem"
#       stats example: health 40, strength 12, defense 6, speed 3, type "melee"
#
# boss: None
#
# paths:
#   - Silent Sanctuary
#   - Boot Camp
#   - Optional: side path to Clash Fest / PANCAKES!
#
# Interactions:
# def arena_dragon_spa():
#     # Print spa description
#     # If Dragon Scale not taken:
#     #     Offer pickup and equip (+10 defense)
#     # If Healing Crystal not taken:
#     #     Offer pickup
#     # If Dragon Spirit not met:
#     #     friend_interaction("Dragon Spirit") -> heal + Dragon Scale
#     # Combat encounters: Aqua Serpents, Steam Golem; apply mist effect to ranged attacks
#     # Hot spring pools can be used once per visit to restore HP
#     # Show exits and prompt movement choice

#Arena 20 boot camp boss battle 4
# description:
#   "A rugged training camp filled with obstacle courses, swinging logs, and towering mining equipment.
#    The Mighty Miner tests all who enter with brute strength and cunning traps."
#
# items:
#   - "Boot Camp Armor"
#       description: "Reinforced armor for heavy defense; grants +15 defense when equipped."
#       effect: equippable item
#   - "Energy Drink"
#       description: "Restores 30 HP and grants +5 temporary strength for next battle."
#       effect: consumable buff item
#
# friend/helper:
#   - "Trainer Miner"
#       dialogue lines:
#           1) "You've come far, skeleton. Take this armor to survive the next trial."
#           2) "Observe the logs; timing is everything."
#       reward:
#           - Gives Boot Camp Armor
#           - Provides advice on Mighty Miner's attack pattern
#       friend flag: friends_met["Trainer Miner"] = True after interaction
#
# enemies:
#   - "Miner Cadets"
#       stats example: health 20, strength 6, defense 3, speed 5, type "melee"
#   - "Rock Crushers"
#       stats example: health 28, strength 10, defense 5, speed 3, type "melee"
#
# boss: MIGHTY MINER
#   boss_stats:
#       total_health: 250
#       base_strength: 25
#       base_defense: 12
#       speed: 4
#       type: "melee"
#   boss_specials:
#       - "Ground Slam": 30-40 damage to player; chance to stagger
#       - "Pick Throw": 15-25 ranged attack ignoring 20% defense
#       - "Reinforced Armor": reduces damage from low-tier attacks by 50%
#
# boss battle:
# def boss_mighty_miner_battle():
#     # Pre-battle: ensure player has Boot Camp Armor or Energy Drink if desired
#     # While boss HP > 0 and player HP > 0:
#     #     Display boss and player stats
#     #     Player turn: Attack, Defend, Use Item, Ability
#     #         Apply armor bonuses if equipped
#     #     Boss turn: choose Ground Slam or Pick Throw based on cooldown
#     #     Compute damage and update HP
#     # End loop when either HP <= 0
#     # On victory:
#     #     Append "Mighty Miner" to defeated_bosses
#     #     Award XP: 450, coins: 350
#     #     Unlock next arenas (Clash Fest, PANCAKES!, Valkalla)
#     #     Print cinematic victory text
#
# sample combat turn snippet:
#   - Player HP: 130, strength: 22 (+5 temporary from Energy Drink)
#   - Boss uses Ground Slam: 35 damage
#       Armor reduces 50%: 17 damage taken
#       Player HP = 130 - 17 = 113
#   - Player attacks with card + weapon bonus = 30
#       Mighty Miner armor reduces 50%: 15 damage
#       Boss HP = 250 - 15 = 235
# Arena 21 Clash Fest 
# description:
#   "A grand coliseum decorated with banners and fireworks.
#    The sound of cheering echoes as automated arena traps spring periodically."
#
# environment mechanics:
#   - Firework traps: occasional AoE damage 5-10
#   - Random coin drops appear on floor: 10–20 coins per trigger
#
# items:
#   - "Festival Shield"
#       description: "Shield adorned with colorful banners; +10 defense against ranged attacks."
#       effect: equippable item
#   - "Spark Bomb"
#       description: "Throws a small explosive that deals 20–25 damage to all enemies in arena."
#       effect: consumable offensive item
#
# friend/helper:
#   - "Festival Trickster"
#       dialogue lines:
#           1) "Catch these sparks! They'll help you in tight fights."
#           2) "The more you dodge, the stronger you appear."
#       reward:
#           - Gives Spark Bomb
#           - Adds temporary agility +5 for one arena traversal
#       friend flag: friends_met["Festival Trickster"] = True after interaction
#
# enemies:
#   - "Arena Fighters"
#       stats example: health 30, strength 10, defense 5, speed 5, type "melee"
#   - "Firework Elementals"
#       stats example: health 20, strength 8, defense 2, speed 7, type "ranged"
#       special: AoE explosion on every 2nd turn
#
# boss: None
#
# paths:
#   - PANCAKES!
#   - Valkalla
#
# interactions:
# def arena_clash_fest():
#     # Print arena description and traps
#     # If Festival Shield not taken:
#     #     Offer pickup
#     # If Spark Bomb not taken and Festival Trickster not met:
#     #     friend_interaction("Festival Trickster") -> give Spark Bomb + agility boost
#     # Combat sequences with Arena Fighters and Firework Elementals
#     # Firework traps randomly trigger each turn
#     # Collect random coins if player steps on coin drop zones
#     # Show exits and prompt movement choice

# Arena 22 Pancakes!
# description:
#   "A whimsical arena filled with giant syrup rivers and floating pancakes.
#    The sticky surfaces slow movement, making timing important."
#
# environment mechanics:
#   - Syrup: reduces speed by 2 each turn standing on it
#   - Flipping pancakes: chance to knock player down (stun for 1 turn)
#
# items:
#   - "Butter Blade"
#       description: "A slippery sword that increases attack by +15 when used on melee enemies."
#       effect: equippable weapon
#   - "Maple Syrup Vial"
#       description: "Sticky liquid that slows enemy for 2 turns, reducing speed by 3."
#       effect: consumable debuff item
#
# friend/helper:
#   - "Fluffy Pancake Spirit"
#       dialogue lines:
#           1) "I am the guardian of syrup and fluff. Take my blade."
#           2) "Use the sticky surfaces wisely to trap your foes."
#       reward:
#           - Gives Butter Blade
#           - Explains sticky surfaces mechanics
#       friend flag: friends_met["Fluffy Pancake Spirit"] = True after interaction
#
# enemies:
#   - "Syrup Slimes"
#       stats example: health 25, strength 7, defense 3, speed 4, type "ranged"
#   - "Flying Pancake Beasts"
#       stats example: health 30, strength 9, defense 4, speed 6, type "melee"
#
# boss: None
#
# paths:
#   - Clash Fest
#   - Valkalla
#
# interactions:
# -------------------------------------------------------
# def arena_pancakes():
#     # Print arena description and hazards
#     # If Butter Blade not taken and Pancake Spirit not met:
#     #     friend_interaction("Fluffy Pancake Spirit") -> give Butter Blade
#     # Combat: Syrup Slimes and Flying Pancake Beasts
#     # Syrup slows player; pancake flips may cause stun
#     # Maple Syrup Vial can be used strategically to debuff enemies
#     # Show exits and prompt movement choice

# Arena 23 Valkalla
# description:
#   "A cold, mountainous arena with icy peaks, howling winds, and jagged cliffs.
#    The treacherous terrain tests agility and endurance."
#
# environment mechanics:
#   - Slippery ice: chance to fall, lose turn or take 5-10 damage
#   - Strong winds: reduce ranged accuracy by 15%
#
# items:
#   - "Valkallian Ice Shield"
#       description: "Grants +15 defense against ranged attacks."
#       effect: equippable item
#   - "Frost Potion"
#       description: "Deals 25 damage to melee enemy and reduces their speed by 2 for 2 turns."
#       effect: consumable offensive item
#
# friend/helper:
#   - "Frost Giant"
#       dialogue lines:
#           1) "The wind bites, but so can you. Take this shield."
#           2) "Step carefully on ice, or the cliffs will be your grave."
#       reward:
#           - Gives Valkallian Ice Shield
#           - Advice on ranged attack penalties
#       friend flag: friends_met["Frost Giant"] = True after interaction
#
# enemies:
#   - "Ice Wolves"
#       stats example: health 25, strength 8, defense 4, speed 6, type "melee"
#   - "Frost Archers"
#       stats example: health 20, strength 10, defense 3, speed 5, type "ranged"
#
# boss: None
#
# paths:
#   - Clash Fest
#   - PANCAKES!
#   - Legendary Arena
#
# interactions:
# def arena_valkalla():
#     # Print icy mountain description
#     # If Valkallian Ice Shield not taken:
#     #     Offer pickup
#     # If Frost Giant not met:
#     #     friend_interaction("Frost Giant") -> give Ice Shield + advice
#     # Combat: Ice Wolves and Frost Archers
#     # Apply ice slip and wind mechanics
#     # Show exits and prompt movement choice


# Arena 24 Final
# description:
#   "The grandest arena, shimmering with golden light.
#    Mega Knight awaits, ready to test every skill you have gained."
#
# environment mechanics:
#   - No hazards
#   - High visibility, all attacks normal
#
# items:
#   - "Legendary Banner"
#       description: "Boosts all stats by +5 temporarily during the final boss fight."
#       effect: consumable buff
#
# friend/helper:
#   - All previously met friends may give advice or minor buffs
#       e.g., Dragon Spirit +20 HP, Frost Giant +5 defense, Festival Trickster +5 speed
#
# enemies:
#   - None prior to boss
#
# boss: MEGA KNIGHT
#   boss_stats:
#       total_health: 500
#       base_strength: 35
#       base_defense: 20
#       speed: 6
#       type: "melee"
#   boss_specials:
#       - "Mega Jump": 50 damage, ignores defense 50%
#       - "Shockwave Slam": 30-40 damage to all adjacent allies
#       - "Armor Plate": reduces damage from weak attacks by 50%
#
# boss battle:
# def boss_mega_knight_battle():
#     # Pre-battle: check if Legendary Banner or other buffs exist
#     # While boss HP > 0 and player HP > 0:
#     #     Display boss and player stats
#     #     Player turn: Attack, Defend, Use Item, Use Ally Ability
#     #     Apply buffs from previous friends/items
#     #     Compute damage and update HP for boss and allies
#     #     Boss turn: choose Mega Jump or Shockwave Slam based on cooldown
#     # End loop when either HP <= 0
#     # On victory:
#     #     Append "Mega Knight" to defeated_bosses
#     #     Award XP: 1000, coins: 1000
#     #     Print cinematic victory text
#     #     Break main game loop — player wins

# Arena 25 final loop
# description:
#   "After defeating Mega Knight, Larry can explore Legendary Arena freely or restart the adventure."
#
# options:
#   - Restart game:
#       - Reset all player stats, inventory, coins
#       - Reset defeated bosses and friend flags
#       - Main game loop starts over
#   - Explore Legendary Arena:
#       - Interact with all friends
#       - Collect leftover items
#       - Optional side quests for coins and XP
#
# main loop break logic:
#   - Use break statement to exit game loop when Mega Knight is defeated
#   - Optionally prompt for restart after end
#
# def post_final_replay():
# Print celebration text
#  Offer restart or free exploration
# If restart selected:
#     Reset all variables
# Break to main game loop start


#ts is too long 