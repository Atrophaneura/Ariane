blueprints = custom_target('blueprints',
  input: files(
    'window.blp',
    'welcome.blp',
    'help-overlay.blp',
    'show_row.blp',
  ),
  output: '.',
  command: [find_program('blueprint-compiler'), 'batch-compile', '@OUTPUT@', '@CURRENT_SOURCE_DIR@', '@INPUT@']
)
