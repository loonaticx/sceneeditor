"""
SceneGlobals.py
Author: Loonatic
Date: 10/15/21
"""

configFile = "config/config.prc"

# some of these can be put in config.prc
controlType = 'Keyboard'

color = (30, 30, 30)
backgroundColor = (color[0]/255.0, color[1]/255.0, color[2]/255.0)

dummyModelPath = "models/misc/sphere"


# todo: integrate this (particle panel is broken rn)
ParticlePanelSpecs = {
    "appname": "Particle Panel",
    "framewidth": 375,
    "frameheight": 575,
    "usecommandarea": 0,
    "usestatusarea": 0,
    "balloonstate": "both"
}

sceneControls = {
    'mouse1-up'
    'mouse2-up'
    'mouse3-up'
    'shift'
    'control'
    'alt'
    'page_up'
    'page_down'
}