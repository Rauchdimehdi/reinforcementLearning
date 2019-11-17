import argparse
import gym

def build_arg_parser():
	parser = argparse.ArgumentParser(description= ' run an enviroment')
	parser.add_argument('--input-env', dest='input_env',required=True, choices=['cartpole','mountaincar','pendulum'], help='Specify the enviroment name')
	return parser

if __name__ == '__main__':
	args= build_arg_parser().parse_args()
	input_env = args.input_env

	name_map = {'cartpole':'CartPole-v0',
				'mountaincar':'MountainCar-v0',
				'pendulum':'Pendulum-v0'}
	#our environment	
	env = gym.make(name_map[input_env])
	
	#Start iterating
	for _ in range(20):
		#reset the environment
		observation = env.reset()

		for i in range(100):
			#render the environment
			env.render()

			print(observation)
			#Take the action
			action = env.action_space.sample()
			#extraction some information of the action
			observation, reward, done, info = env.step(action)

			if done:
				print("Episode finished after {} timesteps", format(i+1))
				break



