import time
from flask import Flask, request, Response
from flask import render_template
# import markdown

from app.agent import Agent

def setup_routes(app: Flask):
	@app.route('/')
	def home():
		agent = Agent()
		
		# agents = [dict(name=f'Agent {i+1}') for i in range(20)]
		models = agent.get_models()
		# agents = [i for i in range(len(agent.get_agents()))]
		agents = agent.get_agents()
		# response = 'Thinking...'
		response = ''
		
		return render_template('index.html',
			title		= 'Ask the llama',
			models		= models,
			agents		= agents,
			response	= response
		)
	
	# @app.route('/ask', methods=['POST'])
	# async def ask():
	# 	# agents = [dict(name=f'Agent {i+1}') for i in range(20)]
	# 	form_data = dict(request.form)
		
	# 	model = form_data['models']
	# 	role = agent.get_agents()[int(form_data['agent'])]
	# 	user_msg = form_data['prompt']
	# 	# stream = agent.get_agent_stream(model, role, user_msg)
	# 	# print(stream)
	# 	# response = ''
	# 	# for chunk in agent.get_agent_stream(model, role, user_msg):
	# 	# 	# print(chunk['message']['content'], end='', flush=True)
	# 	# 	response += chunk['message']['content']

	# 	response = 'Here is a complete CSS file that can be used to style Markdown content: ```css /* Global Styles */ * { box-sizing: border-box; margin: 0; padding: 0; } body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; background-color: #f9f9f9; } h1, h2, h3, h4, h5, h6 { font-weight: bold; color: #444; margin-bottom: 10px; } h1 { font-size: 28px; } h2 { font-size: 24px; } h3 { font-size: 20px; } h4, h5, h6 { font-size: 18px; } p { margin-bottom: 15px; } a { text-decoration: none; color: #337ab7; } a:hover { color: #23527c; } /* Markdown Styles */ .markdown-body { font-family: Consolas, Monaco, "Lucida Console", monospace; font-size: 14px; padding: 15px; border-radius: 3px; background-color: #f2f2f2; box-shadow: 0 1px 1px rgba(0, 0, 0, .05); } .markdown-body table { font-size: inherit; border-collapse: collapse; margin-bottom: 20px; } .markdown-body th { background-color: #444; color: #fff; padding: 10px; border: 1px solid #333; } .markdown-body td { border: 1px solid #333; padding: 10px; } .markdown-body code { font-family: Consolas, Monaco, "Lucida Console", monospace; font-size: inherit; background-color: #f0f0f0; border-radius: 3px; padding: 2px 4px; white-space: pre-wrap; } .markdown-body code:after { visibility: hidden; content: attr(data-url); } .markdown-body blockquote { margin-bottom: 15px; font-style: italic; } .markdown-body hr { border: none; border-top: 1px solid #aaa; margin: 30px auto; } .markdown-body ul, .markdown-body ol { list-style: none; padding: 0; margin-bottom: 15px; } (markdown-body li { margin-left: 20px; } .markdown-body img { max-width: 100%; height: auto; margin: 10px 0; border-radius: 3px; box-shadow: 0 1px 1px rgba(0, 0, 0, .05); } .markdown-body pre { font-family: Consolas, Monaco, "Lucida Console", monospace; font-size: inherit; background-color: #f2f2f2; border-radius: 3px; padding: 15px; box-shadow: 0 1px 1px rgba(0, 0, 0, .05); } .markdown-body pre code { font-family: Consolas, Monaco, "Lucida Console", monospace; font-size: inherit; background-color: #f0f0f0; border-radius: 3px; padding: 2px 4px; white-space: pre-wrap; } .markdown-body table th, .markdown-body table td { border: 1px solid #ddd; padding: 8px 16px; vertical-align: top; } ``` This CSS file includes styles for common Markdown elements like headings, paragraphs, lists, code blocks, images, and tables. It also includes some basic typography and layout styles to make the content look visually appealing. You can customize this CSS file as needed to fit your specific use case or branding requirements.'

	# 	return response
	@app.route('/ask', methods=['POST'])
	# @app.route('/ask')
	def ask():
		agent = Agent()

		form_data = dict(request.form)

		model = form_data['models']
		# role = agent.get_agents()[int(form_data['agent'])]
		role = agent.get_agents()[form_data['agent']]
		user_msg = form_data['prompt']
		if len(user_msg) < 1:
			return ''

		def gen():
			for chunk in agent.get_agent_stream(model, role, user_msg):
				# yield f"{chunk['message']['content']}".replace('\n','<br>')
				# res = f"{chunk['message']['content']}".replace('\n','<br>')
				# res = f"{chunk['message']['content']}".replace('\n','\\n')
				res = f"{chunk['message']['content']}"
				# print(res)
				# # res = markdown
				yield res

		return Response(gen(), mimetype='text/event-stream')