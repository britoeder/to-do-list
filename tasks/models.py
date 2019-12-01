from django.db import models
from django.contrib.auth import get_user_model
class Task(models.Model):
  # declaração da contante
  STATUS = (
    ('doing', 'Fazendo'),
    ('done', 'Feito'),
  )
  user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE) #quando excluido o usuario, o método models.CASCATE apaga todas as informações dele
  title = models.CharField(max_length=255)
  description = models.TextField()
  done = models.CharField(
    max_length=5,
    choices=STATUS, #constante, parecido com um select
  ) 
  # creat_at é usado para saber o momento exato de criação de conteudo no BD
  created_at = models.DateTimeField(auto_now_add=True)
  # update_at é usado para saber o momento exato de edição de conteudo no BD
  update_at = models.DateTimeField(auto_now=True)

# Essa função é utilizada para retornar o titulo da tarefa no admin do Django
  def __str__(self):
    return self.title
