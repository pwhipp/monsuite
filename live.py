"""
This is just for development. When in the venv run:
python live.py
to run the sphinx documentation on the specified local port.
Any changes to the sphinx files will be automatically rebuilt and updated in a browser pointed at 'localhost:5500'
"""
from livereload import Server, shell
server = Server()
server.watch('documentation/docs/*.rst', shell('make html', cwd='documentation'))
server.serve(port=5500, root='documentation/_build/html')
