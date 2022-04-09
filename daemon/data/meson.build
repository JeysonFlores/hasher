data_conf = configuration_data()
data_conf.set('libexecdir', get_option('prefix') + '/' + get_option('bindir'))

configure_file(
    input: meson.project_name() + '.desktop.in',
    output: meson.project_name() + '.desktop',
    configuration: data_conf,
    install: true,
    install_dir: join_paths(etcdir, 'xdg', 'autostart')
)

configure_file(
    input: meson.project_name() + '.service.in',
    output: meson.project_name() + '.service',
    configuration: data_conf,
    install: true,
    install_dir: dbus_service_dir
)
