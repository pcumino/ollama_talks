#!/usr/bin/env python3

#===========================================================#
#File Name:			agent.py
#Author:			Pedro Cumino
#Email:				pedro.cumino@av.it.pt
#Creation Date:		Sat 22 Feb 14:59:30 2025
#Last Modified:		Sat 22 Feb 14:59:31 2025
#Description:
#Args:
#Usage:
#===========================================================#

import ollama
import yaml, json

class Agent(object):
	'''docstring for Agent'''
	def __init__(self):
		super(Agent, self).__init__()
		self.config = self.load_config()
		self.model = ''
		self.role = ''

	def load_config(self):
		config = ''
		with open('app/agents.yaml') as file:
			config = yaml.safe_load(file)
		return config

	def get_models(self):
		# return self.config['models']
		res = [i['model'].replace(':latest','') for i in ollama.list()['models']]
		return res

	def get_agents(self):
		return self.config['system-roles']

	def get_agent_stream(self, model, role, user_msg=''):
		assert len(user_msg) > 0, "Empty user message"
		assert model in self.get_models(), "This model does not exist"

		messages = [
			dict(role='system', content=role),
			dict(role='user', content=user_msg),
		]
		return ollama.chat(model=model, messages=messages, stream=True)
# config = load_config()
# print(get_models(config))
# print(get_agents(config))

# def main(argv):
# 	print(get_models())
# 	# the system prompt shall be executed only once
# 	# print(json.dumps(config, indent=4))
# 	pass
# 	# response = ollama.chat(model='llama2-uncensored', messages=[
# 	# response = ollama.chat(model='llama3', messages=[
# 	# {
# 	# 	'role': 'system',
# 	# 	'content': 'You are an AI assistant.',
# 	# },
# 	# {
# 	# 	'role': 'user',
# 	# 	'content': 'Why is the sky blue?',
# 	# },
# 	# ])
# 	# print(response['message']['content'])

# if __name__ == '__main__':
# 	import sys
# 	main(sys.argv[1:])


