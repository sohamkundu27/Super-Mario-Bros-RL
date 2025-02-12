import gym_super_mario_bros
from gym_super_mario_bros.actions import RIGHT_ONLY
from nes_py.wrappers import JoypadSpace

ENV_NAME = 'SuperMarioBros-1-1-v3'
env = gym_super_mario_bros.make(ENV_NAME)
env = JoypadSpace(env, RIGHT_ONLY)

state = env.reset()
done = False

while not done:
    action = RIGHT_ONLY.index(['right'])
    state, action, done, nstate = env.step(action)
    env.render()

env.close()