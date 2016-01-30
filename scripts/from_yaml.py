from __future__ import print_function
from sdfbuilder.math import Vector3
from sdfbuilder.structure import Collision
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../')

# from revolve.build import util
# util.size_scale_factor = 10

from revolve.convert.yaml import yaml_to_robot
from tol.spec import get_body_spec, get_brain_spec
from tol.config import parser
from tol.build import get_builder, get_simulation_robot

bot_yaml = '''
---
body:
  id          : Core
  type        : Core
  children:
    0:
      id: Brick1
      type: FixedBrick
      orientation: 90
      children:
        2:
          id: Sensor
          type: TouchSensor
    1:
      id: Hinge
      type: Hinge
      orientation: 90
    2:
      id: Tc1
      type: TouchSensor

'''
# bot_yaml = '''
# ---
# body:
#   id          : Core
#   type        : TouchSensor
# '''
conf = parser.parse_args()
body_spec = get_body_spec(conf)
brain_spec = get_brain_spec(conf)
bot = yaml_to_robot(body_spec, brain_spec, bot_yaml)
builder = get_builder(conf)
sdf = get_simulation_robot(bot, "test_bot", builder, conf)
sdf.elements[0].set_position(Vector3(0, 0, 0.05))

with open("/home/elte/.gazebo/models/test_bot/model.sdf", "w") as f:
    f.write(str(sdf))

