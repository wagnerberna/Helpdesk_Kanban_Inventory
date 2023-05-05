from django.contrib.auth.models import User
from django.db import models


class Status(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "kanban_status"

    def __str__(self):
        return self.name


# auto_now_add (atualiza apenas quando é inserido)
# auto_now (atualiza toda vez q é alterado)
# on_delete set_null (quando uma categoria for apagada o campo se torna nulo)
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70, null=False, unique=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "kanban_project"

    def __str__(self):
        return self.name
        # return "Projeto: %s / Status: %s" % (self.name, self.status)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70, null=False, unique=True)
    description = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "kanban_category"

    def __str__(self):
        return self.name


# usa tabela de usuários do Django
class Team(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "kanban_team"

    def __str__(self):
        return "%s" % self.user_name

        # return "%s / Time: %s" % (self.user_name, self.user_name)


class Priority(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1, null=True, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "kanban_priority"

    def __str__(self):
        return "%s" % self.name


# task_owner (pode ficar em branco(no formulário para salvar), e o valor padrão é None)
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=70, null=False)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )
    task_owner = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    priority = models.ForeignKey(
        Priority, on_delete=models.SET_NULL, null=True, blank=True
    )
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "kanban_task"

    def __str__(self):
        return self.title
        # return "Tarefa: %s / Projeto: %s, Responsável: %s, Status: %s" % (
        #     self.name,
        #     self.project,
        #     self.task_owner,
        #     self.status,
        # )
