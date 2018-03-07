import os

os.environ['JUPYTER_CONFIG_DIR'] = '/home/jovyan/jupyter-config'
c.Spawner.env_keep.append('JUPYTER_CONFIG_DIR')
c.NotebookApp.default_url = '/scriptedforms/detailed.md'

