# EG 2nd Crew Shares


print("The crew earned a whole bunch of money on the last outing, but the captain didn't have time to divvy it all up before release everyone to port.He gave each member of the crew 500 dollars for the evening and then sat down with his first mate to properly divide the shares.")

money_earned = float(input("How much money was made in the outing.(number has to be a whole number without decimals): "))
crew_num = int(input("How many crew members were there not including the captain and the first mate."))

equal_share = money_earned/(crew_num+10)
captains_share = round(equal_share*7,2)
first_mate_share = round(equal_share*3,2)
last_share = money_earned-(captains_share+first_mate_share)
crew_share = round (equal_share-500, 2)

print(f"The captain gets, ${captains_share:.2f}")
print(f"The First mate gets, ${first_mate_share:.2f}")
print(f"The crew members each need, ${crew_share:.2f} more.")