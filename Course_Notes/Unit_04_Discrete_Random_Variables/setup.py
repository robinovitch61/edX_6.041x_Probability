from IPython.display import HTML

def center():
	CSS = """
	.output {
	    align-items: center;
	}
	"""

	return(HTML('<style>{}</style>'.format(CSS)))
