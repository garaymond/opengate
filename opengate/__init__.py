# for a unclear reason, ssl must be imported before to avoid error:
# "from http.client import HTTPConnection, HTTPSConnection
# ImportError: cannot import name 'HTTPSConnection' from 'http.client'"

# generic helpers
from .geometry.VolumeManager import __world_name__
from .helpers_log import *
from .helpers import *
from .helpers_image import *
from .helpers_tests import *
from .helpers_tests_root import *
from .helpers_transform import *

# main mechanism for the 'elements': source, actor, volume
from .UserInfo import *
from .UserElement import *
from .source.SourceBase import *
from .actor.ActorBase import *
from .geometry.VolumeBase import *

# main object
from .Simulation import *
from .EngineBase import *
from .SimulationEngine import *
from .SimulationOutput import *
from .helpers_run_timing import *

# helpers to list all possible types of elements
from .geometry.helpers_geometry import *
from .geometry.helpers_materials import *
from .source.helpers_source import *
from .source.helpers_gammas_from_ions_decay import *
from .actor.helpers_actor import *
from .actor.helpers_digitizer import *
from .actor.helpers_filter import *
from .SimulationUserInfo import *
from .helpers_element import *

# Volume specific
from .geometry.MaterialBuilder import *
from .geometry.ElementBuilder import *
from .geometry.MaterialDatabase import *
from .geometry.VolumeManager import *
from .geometry.VolumeEngine import *
from .geometry.SolidBuilderBase import *

# Source specific
from .source.SourceManager import *
from .source.SourceEngine import *
from .source.GANSourceConditionalGenerator import *
from .source.GANSourceConditionalPairsGenerator import *
from .source.VoxelizedSourceConditionGenerator import *
from .source.PencilBeamSource import *
from .physics.helpers_physics import *
from opengate.physics.helpers_physics import *

# Actor specific
from .actor.FilterManager import *
from .actor.ActorManager import *
from .actor.ActorEngine import *
from .actor.ActionEngine import *
from .UIsessionSilent import *
from .UIsessionVerbose import *
from .RunAction import *

# Physics
from .physics.PhysicsUserInfo import *
from .physics.PhysicsManager import *
from .physics.PhysicsEngine import *
