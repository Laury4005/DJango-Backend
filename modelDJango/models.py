from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    
    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    

# En la shell de Django
# python manage.py shell

# Crear un nuevo autor
# >>> from mi_aplicacion.models import Author
# >>> author = Author.objects.create(name='Nombre del autor', bio='Biografía del autor')

# Crear un nuevo post asociado al autor
# >>> from mi_aplicacion.models import Post
# >>> post = Post.objects.create(title='Título del post', content='Contenido del post', author=author)

# Leer los posts
# >>> posts = Post.objects.all()
# >>> for post in posts:
# >>>     print(post.title)

# Leer autores
# authors = Author.objects.all()
# for author in authors:
# print(author.name)

# Actualizar un post
# >>> post = Post.objects.get(id=1)
# >>> post.title = 'Nuevo título del post'
# >>> post.save()

# Eliminar un post
# >>> post = Post.objects.get(id=1)
# >>> post.delete()
