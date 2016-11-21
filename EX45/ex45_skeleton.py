# * Map
#  - next_scene
#  - opening_scene
# * Engine
#  - play
# * Scene
#  - enter
    # * Death
    # * Saloon
    # * Plains
    # * Shaman Tent
    # * Snake Pit

class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()
