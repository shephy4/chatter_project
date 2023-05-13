# Chatter_project

This is a Chatbot for Python Django including NLTK and Django-REST-framework. It is currently working without Machine learning algorithms because decisions are made by simple statistic evaluation. It is based on labeled data on your Django Database and the tool is supporting continuous labeling.

# Requirements
Except for the fact that you obviously require Django. Python (3.7, 3.8, 3.9)(these versions are specifically needed to install Chatbot library)

# Dependencies
Django REST-Framework - Awesome web-browsable Web APIs. NLTK - the Natural Language Toolkit

# Installation
pip install requirement.txt

# How run the application
py manage.py migrate
py manage.py runserver

# How to send a post request
Go the url the "/localhost/simple_chatbot"
Required Request type: POST
payload/data: {"message": "YOUR MESSAGE"}
response: {tag: 'TAG', message: 'RESPONSE'}

