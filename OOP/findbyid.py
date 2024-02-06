def planet(id):
    planets = {1:"Mercury",
               2:"Venus",
               3:"earth",4:"Mars",5:"Jupiter",6:"Saturn",7:"Uranaus",
               8:"Neptune",9:"Pluto"}
    if id in planets:
        return planets[id]

print(planet(3))



