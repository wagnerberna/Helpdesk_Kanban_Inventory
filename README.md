# Sistema de HelpDesk em Django

## 💡 Objetivo:
Através do Django criar um sistema de help desk, gerência de projetos com quadro Kanban e inventário de TI, fornecendo dashboards interativos dos dados com o JavaScript.

## ⚙️ Serviço WEB:
O sistema está setado para acesso on premise, pois é acessado apenas dentro da rede local, sendo configurado em uma máquina virtual rodando o SO Linux Ubuntu, o acesso WEB é provido utilizando o Gunicorn e Nginx.

## 🎲 Banco de Dados:
O banco de dados escolhido é o PostgreSQL, caso a URL do mesmo não esteja configurada nas variáveis de ambiente, o sistema irá usar como padrão o SQLite na raiz do projeto.
### Diagrama de Entidade e Relacionamento do Banco:
![DER](readme/ti_db_der.png)

## ☑️ Menu Lateral:
Na lateral esquerda, através de um ícone de um quadrado azul com três traços, é possível acessar um menu com os atalhos mais utilizados, este menu foi feito em o JS com CSS.

## 📝 Paginação e Filtros:
Paginação e filtros foram inseridos em todas páginas que podem vir a conter uma grande quantidade de dados.
Os filtros em geral são por busca de palavras chaves ou categorias.

## 📋 Kanban:
No quadro Kanban as tarefas forma inseridas em formato de postits coloridos sendo divididas em quatro fileiras "TO DO", "DOING", "BLOCKED", "DONE" com as respectivas cores verde, amarelo, vermelho e azul.
Na lateral de cada postit existem três ícones, uma seta para passar a tarefa para o próximo status, uma pasta aberta para editar a tarefa e uma lixeira para excluir a mesma.
É possível Filtrar as tarefas pelo título, dono da tarefa e prioridade.
Novas Tarefas podem ser adicionadas pelo ícone de sinal positivo no canto superior esquerdo.

## 🤝 Help Desk:
O sistema de help desk pode ser utilizado tanto na área de infraestrutura como para área de desenvolvimento para suporte ao sistema, o usuário comum possui um acesso limitado, que só permite controlar, visualizar e abrir seus próprios chamados, os recursos mais avançados só são permitidos aos usuários inseridos na tabela de área restrita.
Na área do atendente é possível visualizar a fila geral de chamados, ou apenas os chamados que estão atribuídos ao atendente logado o qual pode inserir detalhes sobre o atendimento ou tentativas de contato na lateral direita, os status dos chamados são "Aguardando Atendimento", "Em Andamento", "Pendente" e "Concluído".
o envio de e-mails sobre aviso de abertura de chamado e atualizações no atendimento, pode ser ativado ou desativado por intermédio de uma varíavel de ambiente, que pode ser setada com True para Habilitar ou False para desabilitar.

## 📊 Dashboard:



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
### ⭐📌🚩⚠️👍👋 Gerais:
| Rota            | Descricao              |
|-----------------|------------------------|
| /admin          | Administração do Django|
| /login          | Login                  |
| /changepassword | Alteração da Senha     |
| /about          | Sobre o Sistema        |
| /logout         | logout                 |
| /               | Página Inicial         |

### 🙍‍♂️ Help Desk Usuários:
| Rota                            | Descricao                    |
|---------------------------------|------------------------------|
| /helpdesk/demand                | Chamados Abertos             |
| /helpdesk/new_demand            | Abertura de um Novo Chamados |
| /helpdesk/demand_done           | Chamados Finalizados         |
| /helpdesk/demand_details/{ID}   | Detalhes do Chamado pelo ID  |
| /helpdesk/delete/{ID}           | Excluir Chamado pelo ID      |

### 🧙 Help Desk Atendentes:
| Rota                            | Descricao                                 |
|---------------------------------|-------------------------------------------|
| /helpdesk/support               | Todos Chamados Aberto                     |
| /helpdesk/support_done          | Todos Chamados Finalizados                |
| /helpdesk/support_technical     | Chamados Atribuídos ao Técnico Logado     |
| /helpdesk/support/{ID}          | Detalhes e Atualização do Chamado pelo ID |

### 📋 Quadro Kanban:
| Rota                            | Descricao                                   |
|---------------------------------|---------------------------------------------|
| /kanban/kanban_manager          | Gerenciamento de Projetos e Tarefas         |
| /kanban/projects_open           | Acesso ao Quadro Kanban de cada Projeto     |
| /kanban/kanban_board/{ID}       | Quadro Kanban do Projeto pelo ID            |
| /kanban/kanban_task_add         | Criação de uma Nova Tarefa dentro do Kanban |
| /kanban/kanban_task_update/{ID} | Atualização da Tarefa pelo ID no Postit     |
| /kanban/kanban_task_delete/{ID} | Excluir Tarefa pelo ID no Postit            |

### ✅ Administração dos Projetos:
| Rota                            | Descricao                      |
|---------------------------------|--------------------------------|
| /kanban/projects_open           | Todos Projetos Abertos         |
| /kanban/project_add             | Criação de um Novo Projeto     |
| /kanban/projects_done           | Todos Projetos Finalizados     |
| /kanban/project_update/{ID}     | Atualização do Projeto pelo ID |
| /kanban/project_delete/{ID}     | Excluir Projeto pelo ID        |

### ✔️ Administração das Tarefas dos Projetos:
| Rota                            | Descricao                      |
|---------------------------------|--------------------------------|
| /kanban/task_open               | Todas Tarefas Abertas          |
| /kanban/task_add                | Criação de uma Nova Tarefa     |
| /kanban/task_done               | Todos Tarefas Finalizadas      |
| /kanban/task_update/{ID}        | Atualização da Tarefa pelo ID  |
| /kanban/task_delete/{ID}        | Excluir Tarefa pelo ID         |





### 📊 XXX:
| Rota                           | Descricao                             |
|--------------------------------|---------------------------------------|
| /report/xxx         | logout                 |
| /report_api/xxx         | logout                 |
report_interactive
| /inventory/xxx         | logout                 |


