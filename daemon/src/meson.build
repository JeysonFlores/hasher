daemon_conf = configuration_data()
daemon_conf.set('PYTHON', py_installation.path())
daemon_conf.set('VERSION', meson.project_version())

configure_file(
    input: 'hasher_service.py',
    output: meson.project_name(),
    install: true,
    install_dir: get_option('bindir'),
    configuration: daemon_conf
)