gnome = import('gnome')

subdir('ui')

desktop_file = i18n.merge_file(
  input: 'com.github.DesktopCreatorTeam.DesktopCreator.desktop.in',
  output: 'com.github.DesktopCreatorTeam.DesktopCreator.desktop',
  type: 'desktop',
  po_dir: '../po',
  install: true,
  install_dir: join_paths(get_option('datadir'), 'applications')
)

desktop_utils = find_program('desktop-file-validate', required: false)
if desktop_utils.found()
  test('Validate desktop file', desktop_utils,
    args: [desktop_file]
  )
endif

gnome.compile_resources('desktopcreator',
  'desktopcreator.gresource.xml',
  gresource_bundle: true,
  source_dir: meson.current_build_dir(),
  install: true,
  install_dir: PKGDATA_DIR,
  dependencies: blueprints
)

appstream_file = i18n.merge_file(
  input: configure_file(
    input: '@0@.appdata.xml.in.in'.format(PROJECT_RDNN_NAME),
    output: '@BASENAME@',
    configuration: configuration_data({
      'APP_ID': APPLICATION_ID,
      'PROJECT_URL': PROJECT_URL,
      'BUGTRACKER_URL': BUGTRACKER_URL,
      'HELP_URL': HELP_URL,
      'TRANSLATE_URL': TRANSLATE_URL
    })
  ),
  output: '@0@.appdata.xml'.format(APPLICATION_ID),
  po_dir: '../po',
  install: true,
  install_dir: join_paths(get_option('datadir'), 'appdata')
)

appstream_util = find_program('appstream-util', required: false)
if appstream_util.found()
  test('Validate appstream file', appstream_util,
    args: ['validate', appstream_file]
  )
endif

install_data('com.github.DesktopCreatorTeam.DesktopCreator.gschema.xml',
  install_dir: join_paths(get_option('datadir'), 'glib-2.0/schemas')
)

compile_schemas = find_program('glib-compile-schemas', required: false)
if compile_schemas.found()
  test('Validate schema file', compile_schemas,
    args: ['--strict', '--dry-run', meson.current_source_dir()]
  )
endif

subdir('icons')
