#! Python 3
# Traffic light simulation representing the stoplights at an intersection

market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stopLight):
    for key in stopLight.keys():
        if stopLight[key] == 'green':
            stopLight[key] = 'yellow'
        elif stopLight[key] == 'yellow':
            stopLight[key] = 'red'
        elif stopLight[key] == 'red':
            stopLight[key] = 'green'
    assert 'red' in stopLight.values(), 'Neither light is red! ' + str(stopLight)

switchLights(market_2nd)
print(market_2nd)