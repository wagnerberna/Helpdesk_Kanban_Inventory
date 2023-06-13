# Sistema de HelpDesk em Django

## 💡 Objetivo:

Criar o backend e frontend de um sistema de helpdesk e gerenciamento do quadro kanban em Django.

## 🛠 Tecnologias:

- [Django](https://www.djangoproject.com/)
- [django Rest](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLite](https://www.sqlite.org/index.html)
- [Python-Decouple](https://pypi.org/project/python-decouple/)
- [Matplotlib](https://matplotlib.org)
- [Pandas](https://pandas.pydata.org)
- [Seaborn](https://seaborn.pydata.org)
- [OpenPyXL](https://openpyxl.readthedocs.io/en/stable/)
- [Bootstrap](https://getbootstrap.com)
- [Font Awesome](https://fontawesome.com)

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
| /helpdesk/demand               | Chamados Abertos             |
| /helpdesk/new_demand           | Abertura de um Novo Chamados |
| /helpdesk/demand_done          | Chamados Finalizados         |
| /helpdesk/demand_details/{ID}  | Detalhes do Chamado pelo ID  |
| /helpdesk/delete/{ID}          | Excluir Chamado pelo ID      |

### Help Desk Atendentes:
| /helpdesk/xxx         | logout                 |

| /kanban/xxx         | logout                 |
| /report/xxx         | logout                 |
| /report_api/xxx         | logout                 |
| /inventory/xxx         | logout                 |



| /candidate/{ID} | Buscar por ID         |
| /register       | Adicionar             |
| /candidate/{ID} | Atuaizar dados por ID |
| /candidate/{ID} | Deletar por ID        |




| Rota            | Descricao             |
|-----------------|-----------------------|
| /candidates     | Buscar todos          |
| /candidates     | Buscar todos          |
| /candidate/{ID} | Buscar por ID         |
| /register       | Adicionar             |
| /candidate/{ID} | Atuaizar dados por ID |
| /candidate/{ID} | Deletar por ID        |