from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .models import *

User = get_user_model()

@login_required(login_url="/")
def recipes(request):
    if request.method == "POST":
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')

        Recipe.objects.create(
            recipe_image=recipe_image,
            recipe_name=recipe_name,
            recipe_description=recipe_description,
        )

        return redirect('/recipes/')

    queryset = Recipe.objects.all()

    search_query = request.GET.get('search')
    if search_query:
        queryset = queryset.filter(recipe_name__icontains=search_query)

    context = {'recipes': queryset, 'search_query': search_query}
    return render(request, 'recipes/recipes.html', context)

def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    return redirect('/recipes/')

def update_recipe(request, id):
    recipe = Recipe.objects.get(id=id)

    if request.method == "POST":
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')

        recipe.recipe_name = recipe_name
        recipe.recipe_description = recipe_description

        if recipe_image:
            recipe.recipe_image = recipe_image

        recipe.save()
        return redirect('/recipes/')

    context = {'recipe': recipe}
    return render(request, 'recipes/update_recipes.html', context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/recipes/')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('/')

    return render(request, 'recipes/login.html')

def logout_page(request):
    logout(request)
    return redirect('/')

def register_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('/register/')

        try:
            user = User.objects.create_user(username=username, password=password)
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('/')
        except Exception as e:
            messages.error(request, f'Error occurred: {e}')
            return redirect('/register/')

    return render(request, 'recipes/register.html')
