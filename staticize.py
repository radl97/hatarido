template = jinja_environment.get_template('CommentCreate.html')     
output = template.render(template_values)) 

with open('docs/index.html', 'w') as f:
    f.write(output)

render_template("index.html", days=load_model(), weekdays=weekdays())
