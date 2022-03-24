from jinja2 import Environment, FileSystemLoader
from model import load_model, weekdays
import os

jinja_environment = Environment(
    loader=FileSystemLoader(
        os.path.abspath(
            os.path.dirname(__file__)) + '/templates', encoding='utf8'))
template = jinja_environment.get_template('index.html')     

output = template.render({"days": load_model(), "weekdays": weekdays()})

os.makedirs('docs', exist_ok=True)
with open(os.path.join('docs','index.html'), 'w') as f:
    f.write(output)

from pathlib import Path

from shutil import copyfile

pathlist = Path('static').glob('*')
for path in pathlist:
    path_in_str = path.name
    copyfile(os.path.join('static', path_in_str), os.path.join('docs', path_in_str))
