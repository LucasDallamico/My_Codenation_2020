from api.models import User, Agent, Event, Group
from django.db.models import Q
from datetime import datetime


def get_active_users() -> User:
    """
    Traga todos os usuarios ativos, seu último login deve ser 
    menor que 10 dias 
    Teste 1
    """
    #Obtem a data atual
    today = datetime.today()
    # Para descontar 10 dias da data de hj
    lim_of_seach = datetime.fromordinal(today.toordinal()-10) 
    # Retorna uma lista de objetos
    usuarios_ativos = User.objects.filter(last_login__gte=lim_of_seach)
    return usuarios_ativos


def get_amount_users() -> User:
    """
    Retorne a quantidade total de usuarios do sistema
    Teste 2
    """
    #Obtem o total de usuarios da estrutura de dados
    total_usuarios = User.objects.all().count()
    return total_usuarios


def get_admin_users() -> User:
    """
    Traga todos os usuarios com grupo = 'admin'
    Teste 3
    """
    total_usuarios_admin = User.objects.filter(group__name='admin')
    return total_usuarios_admin


def get_all_debug_events() -> Event:
    """
    Traga todos os eventos com tipo debug
    Teste 4
    """
    users_com_bug = Event.objects.filter(level='debug')
    return users_com_bug


def get_all_critical_events_by_user(agent) -> Event:
    """
    Traga todos os eventos do tipo critico de um 
    usuário específico
    Teste 5
    """
    critical_events = Event.objects.filter(
        Q(level='critical') & Q(agent=agent)
    )
    return critical_events


def get_all_agents_by_user(username) -> Agent:
    """
    Traga todos os agentes de associados a um 
    usuário pelo nome do usuário
    Teste 6
    """
    co_relacao = Agent.objects.filter(user__name=username)
    return co_relacao


def get_all_events_by_group() -> Group:
    """
    Traga todos os grupos que contenham alguem que possua 
    um agente que possuem eventos do tipo information
    Teste 7
    """
    agent_with_type_information = Group.objects.filter(
        user__agent__event__level='information'
        )
    return agent_with_type_information