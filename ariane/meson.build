configure_file(
  input: 'ariane.in',
  output: 'ariane',
  configuration: conf,
  install_dir: get_option('bindir')
)

configure_file(
  input: 'ariane.in',
  output: 'local-ariane',
  configuration: local_conf
)

configure_file(
  input: 'constants.py.in',
  output: 'constants.py',
  configuration: configuration_data({
    'APP_ID': APPLICATION_ID,
    'RELEASE_VER': meson.project_version(),
    'VERSION': meson.project_version() + VERSION_SUFFIX,
    'BUILD_TYPE': get_option('buildtype'),
    'PROJECT_URL': PROJECT_URL,
    'BUGTRACKER_URL': BUGTRACKER_URL,
    'HELP_URL': HELP_URL,
    'TRANSLATE_URL': TRANSLATE_URL
  }),
  install: true,
  install_dir: PY_INSTALLDIR.get_install_dir() / 'ariane',
)

launcher = join_paths(meson.project_build_root(), 'ariane', 'local-' + meson.project_name())

run_target('run',
  command: [launcher]
)

# Install sources
ariane_sources = [
  '__init__.py',
  'main.py',
  'window.py',
  'show_row.py',
  'welcome.py',
]

PY_INSTALLDIR.install_sources(ariane_sources, subdir: 'ariane')