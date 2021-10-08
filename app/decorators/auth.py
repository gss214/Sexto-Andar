from flask import  session, redirect, url_for
from functools import wraps

from flask.helpers import flash

# Decorator
def is_authenticated(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        # Verifica session['logado']
        # print('Antes session')
        if 'user_id' not in session:
            # Retorna para a URL de login caso o usuário não esteja logado
            # print('Dentro session')
            return redirect(url_for('login'))

        return f(*args, **kwargs)
    return wrapper

def has_permission(permission):
    def has_permission_f(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            # Verifica session['logado']
            #print('Antes session')
            if 'user_id' not in session:
                # Retorna para a URL de login caso o usuário não esteja logado
                #print('Dentro session')
                return redirect(url_for('index'))

            if session['user_permission'] not in permission:
                flash('Sem permissão de acesso!') 
                return redirect(url_for('index'))

            return f(*args, **kwargs)
        return wrapper
    return has_permission_f