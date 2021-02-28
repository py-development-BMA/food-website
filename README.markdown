## How to create page ##
  #### Part 1, reating html file in main/templates/main ####
  ```python
  {% extends "main/header.html" %}
  {% load static %}
  {% block content %}
  #content placed here
  {% endblock %}
  ```
  #### Part 2, connecting page to server ####
  ```python
  path('name_of_link/', views.name_of_function, name="name_to_use_as_link"),
  ```
  ##### Part 2.1, creating function in views.py #####
  ```python
  def name_of_function(request):
    context = {
    'something_to_html':'Hello world',
    }
    return render(request, 'main/name_of_file_html.html', context)
  ```
  #### Part 3, checking if working ####
 Open browser and write there
 ```
 localhost:8000/name_of_your_link
 ```
 
## How to paste images in html using django ##
example
```python
<img src="{% static 'img/image_name.png' %}">
```
