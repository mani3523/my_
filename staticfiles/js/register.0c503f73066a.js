{% extends "main.html" %}
{% load static %}
{% load crispy_forms_tags %}

{% block title %}
<title>User register</title>

{% endblock title %}
</br>
<h2>Welcome to Registration Page</h2>
{% block content %}
</br>
{% for message in messages  %}
    <div class = "alert alert-success alert-dismissible fade show" role="alert">
        New user registration successful, login through your username and password
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>
    </div>
{% endfor %}
<div class='container'>
    <form method='POST' class="loginfrm mt-5 col-6">
        {% csrf_token %}
        {{register_form|crispy}}
        <div class="d-grid gap-2 d-md-flex justify-content-md">
            <button class="button_slide slide_diagonal" type="submit" style="background-color: transparent;">Register</button>
        </div>
    </form>
</div>
<form class='mt-5 col-6'>
    {% csrf_token %}
    <p>Already have an account?</p>
    {{form|crispy}}
    <div class="d-grid gap-2 d-md-flex justify-content-md">
        <button><a href="{% url "login" %}" data-title="Login"></a></button>
    </div>
</form>
<script src="{% static'js/register.js'%}"></script>
{% endblock content %}