from charms.reactive import when, when_not, set_flag

@when('apt.installed.nginx')
@when_not('simple-nginx.installed')
def install_simple_nginx():
    set_flag('simple-nginx.installed')
