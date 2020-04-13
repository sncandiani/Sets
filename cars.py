showroom = {"carModel1", "carModel2", "carModel3", "carModel4"}

print(len(showroom))

showroom.add("carModel1")



showroom.update({"carModel5", "carModel6"})

showroom.discard("carModel1")

junkyard = {"carModel4", "carModel900", "carModel500"}


newshowroom = showroom.union(junkyard)

newshowroom.discard("carModel4")

print(newshowroom)
