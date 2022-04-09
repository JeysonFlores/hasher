project('com.github.jeysonflores.hasher.Service',
          version: '0.0.0',
    meson_version: '>= 0.50.0',
  default_options: [ 'warning_level=2',
                   ],
)

prefix = get_option('prefix')
datadir = get_option('datadir')
libexecdir = join_paths(prefix, get_option('libexecdir'))
etcdir = get_option('sysconfdir')
dbus_service_dir = dependency(
    'dbus-1'
).get_pkgconfig_variable(
    'session_bus_services_dir',
    define_variable: ['datadir', join_paths(prefix, datadir)]
)
python = import('python')
py_installation = python.find_installation('python3')

subdir('src')
subdir('data')