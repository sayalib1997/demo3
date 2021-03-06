from fabric.api import *
from fabric.contrib.files import *
from path import path as ppath

app = env.app = {
    'seris_svn': 'https://svn.eionet.europa.eu/repositories/Python/seris',
    'reportdb_svn': 'https://svn.eionet.europa.eu/repositories/Naaya/trunk/eggs/reportdb',
    'localrepo': ppath(__file__).abspath().parent.parent,
}

try: from localcfg import *
except: pass

app.update({
    'instance_var_serisbeta': app['serisbeta_repo']/'instance',
    'sandbox_serisbeta': app['serisbeta_repo']/'sandbox',
    'instance_var_seris': app['seris_repo']/'instance',
    'sandbox_seris': app['seris_repo']/'sandbox',
    'user': 'edw',
})


@task
def ssh():
    open_shell("cd '%(seris_repo)s'" % app)


def _install_random_key(remote_path, key_length=20, mode=0600):
    import random
    import string
    from StringIO import StringIO
    vocabulary = string.ascii_letters + string.digits
    key = ''.join(random.choice(vocabulary) for c in xrange(key_length))
    put(StringIO(key), remote_path, mode=mode)


def _svn_repo(repo_path, origin_url, update=True):
    if not exists(repo_path/'.svn'):
        run("mkdir -p '%s'" % repo_path)
        with cd(repo_path):
            run("svn co '%s' ." % origin_url)

    elif update:
        with cd(repo_path):
            run("svn up")

@task
def install_serisbeta():
    _svn_repo(app['serisbeta_repo'], app['seris_svn'], update=True)

    if not exists(app['sandbox_serisbeta']):
        run("virtualenv "# -p python2.6 
            "--no-site-packages --distribute "
            "'%(sandbox_serisbeta)s'" % app)
    run("%(sandbox_serisbeta)s/bin/pip install -r %(serisbeta_repo)s/requirements.txt" % app)

    if not exists(app['instance_var_serisbeta']):
        run("mkdir -p '%(instance_var_serisbeta)s'" % app)

    secret_key_path = app['instance_var_serisbeta']/'secret_key.txt'
    if not exists(secret_key_path):
        _install_random_key(str(secret_key_path))

    put(app['localrepo']/'fabfile'/'production-settings_serisbeta.py',
        str(app['instance_var_serisbeta']/'settings.py'))

    upload_template(app['localrepo']/'fabfile'/'supervisord_serisbeta.conf',
                    str(app['sandbox_serisbeta']/'supervisord.conf'),
                    context=app, backup=False)

@task
def install_seris():
    _svn_repo(app['seris_repo'], app['seris_svn'], update=True)

    if not exists(app['sandbox_seris']):
        run("virtualenv "# -p python2.6 
            "--no-site-packages --distribute "
            "'%(sandbox_seris)s'" % app)
    run("%(sandbox_seris)s/bin/pip install -r %(seris_repo)s/requirements.txt" % app)

    if not exists(app['instance_var_seris']):
        run("mkdir -p '%(instance_var_seris)s'" % app)

    secret_key_path = app['instance_var_seris']/'secret_key.txt'
    if not exists(secret_key_path):
        _install_random_key(str(secret_key_path))

    put(app['localrepo']/'fabfile'/'production-settings_seris.py',
        str(app['instance_var_seris']/'settings.py'))

    upload_template(app['localrepo']/'fabfile'/'supervisord_seris.conf',
                    str(app['sandbox_seris']/'supervisord.conf'),
                    context=app, backup=False)


@task
def seris_supervisor():
    run("'%(sandbox)s/bin/supervisord'" % {
            'sandbox': app['sandbox_seris'],
        })

@task
def serisbeta_supervisor():
    run("'%(sandbox)s/bin/supervisord'" % {
            'sandbox': app['sandbox_serisbeta'],
        })

@task
def service_serisbeta(action):
    run("'%(sandbox)s/bin/supervisorctl' %(action)s %(name)s" % {
            'sandbox': app['sandbox_serisbeta'],
            'action': action,
            'name': 'serisbeta',
        })

@task
def service_seris(action):
    run("'%(sandbox)s/bin/supervisorctl' %(action)s %(name)s" % {
            'sandbox': app['sandbox_seris'],
            'action': action,
            'name': 'seris',
        })


@task
def deploy_serisbeta():
    execute('install_serisbeta')
    execute('serisbeta_supervisor')
    execute('service_serisbeta', 'restart')

@task
def update_serisbeta():
    execute('install_serisbeta')
    execute('service_serisbeta', 'restart')

@task
def deploy_seris():
    execute('install_seris')
    execute('seris_supervisor')
    execute('service_seris', 'restart')

@task
def update_seris():
    execute('install_seris')
    execute('service_seris', 'restart')

