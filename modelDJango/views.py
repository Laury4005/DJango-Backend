# En views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author, Post
from .serializers import AuthorSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.http import HttpResponseRedirect

# def login(request):
#     return render(request, 'login.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Accede a los datos del formulario POST
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirige al usuario a la página deseada después del inicio de sesión exitoso
                #return redirect('authors')
                return HttpResponseRedirect('/authors/') 
            else:
                # El usuario no existe o las credenciales son incorrectas
                # Aquí puedes mostrar un mensaje de error en el formulario
                pass
    else:
        form = LoginForm()  # Crea una instancia del formulario para mostrar en la página de inicio de sesión

    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    # Redirige al usuario a la página de login u otra página deseada después de cerrar sesión
    return redirect('user_login')

@login_required
def authors(request):
    if request.user.is_authenticated:
        return render(request, 'authors.html')
    else:
        return redirect('login')


@api_view(['GET', 'POST'])
def author_list(request):
    """
    List all users or create a new user.
    """
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def author_detail(request, pk):
    """
    Retrieve, update or delete a user instance.
    """
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)