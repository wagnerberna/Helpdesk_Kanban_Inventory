# Sistema de HelpDesk em Django

## 💡 Objetivo:

Através do Django criar um sistema de help desk, gerência de projetos e inventário de TI, fornecendo dashboards interativos dos dados com o JavaScript.
O sistema roda em uma máquina virtual Linux Ubuntu utilizando Gunicorn e Nginx, o banco de dados escolhido é o PostgreSQL.


## 🛠 Tecnologias:

- [Django](https://www.djangoproject.com/)
- [django Rest](https://www.django-rest-framework.org/)
- [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLite](https://www.sqlite.org/index.html)
- [Python-Decouple](https://pypi.org/project/python-decouple/)
- [Matplotlib](https://matplotlib.org)
- [Pandas](https://pandas.pydata.org)
- [Seaborn](https://seaborn.pydata.org)
- [OpenPyXL](https://openpyxl.readthedocs.io/en/stable/)
- [Bootstrap](https://getbootstrap.com)
- [Font Awesome](https://fontawesome.com)
- [Gunicorn](https://pypi.org/project/gunicorn/)
- [Nginx](https://nginx.org)


URL de Acesso: http://127.0.0.1:8000/

## 🔎 Rotas:
### Gerais:
| Rota            | Descricao              |
|-----------------|------------------------|
| /admin          | Administração do Django|
| /login          | Login                  |
| /changepassword | Alteração da Senha     |
| /about          | Sobre o Sistema        |
| /logout         | logout                 |
| /               | Página Inicial         |

### Help Desk Usuários:
| Rota                           | Descricao                    |
|--------------------------------|------------------------------|
| /helpdesk/demand               | Chamados Abertos             |
| /helpdesk/new_demand           | Abertura de um Novo Chamados |
| /helpdesk/demand_done          | Chamados Finalizados         |
| /helpdesk/demand_details/{ID}  | Detalhes do Chamado pelo ID  |
| /helpdesk/delete/{ID}          | Excluir Chamado pelo ID      |

### Help Desk Atendentes:
| Rota                           | Descricao                             |
|--------------------------------|---------------------------------------|
| /helpdesk/support              | Todos Chamados Aberto                 |
| /helpdesk/support_done         | Todos Chamados Finalizados            |
| /helpdesk/support_technical    | Chamados Atribuídos ao Técnico Logado |
| /helpdesk/support/{ID}         | Detalhes do Chamado pelo ID           |

### KANBAN Projetos:
| Rota                           | Descricao                    |
|--------------------------------|------------------------------|
| /kanban/projects_open          | Chamados Abertos             |
| /kanban/project_add            | Abertura de um Novo Chamados |
| /kanban/projects_done          | Chamados Finalizados         |
| /kanban/project_update/{ID}    | Detalhes do Chamado pelo ID  |
| /kanban/project_delete/{ID}    | Excluir Chamado pelo ID      |

### XXX:
| Rota                           | Descricao                             |
|--------------------------------|---------------------------------------|
| /kanban/xxx         | logout                 |
| /report/xxx         | logout                 |
| /report_api/xxx         | logout                 |
| /inventory/xxx         | logout                 |


