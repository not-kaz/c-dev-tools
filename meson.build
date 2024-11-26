project(
  'project_name',
  'c',
  default_options : [
    'c_std=c99',
    'warning_level=3',
    'buildtype=debug',
    #'default_library=static'
    ]
)


# Pedantic warning C99 warning flags
warn_flags = [
  '-Wpedantic',
  #'-Wall',
  #'-Wextra',
  '-Wconversion',
  '-Wsign-conversion',
  '-Wpointer-arith',
  '-Wcast-qual',
  '-Wmissing-prototypes',
  '-Wstrict-prototypes',
  '-Wmissing-declarations',
  '-Wdeclaration-after-statement',
  '-Wimplicit-function-declaration',
  '-Wshadow',
  '-Wdouble-promotion',
  '-Wformat-signedness',
  '-Wvla'
]

add_project_arguments(
  warn_flags,
  language: 'c'
)

# If cppcheck found, add it as possible run target during compilation.
#   'meson compile -C builddir cppcheck'
cppcheck = find_program('cppcheck', required: false)
if cppcheck.found()
  run_target('cppcheck',
    command : [
      'cppcheck',
      '--enable=all',
      '--suppress=missingIncludeSystem', '--suppress=unusedFunction',
      '--project=' + join_paths(meson.build_root(), 'compile_commands.json'),
    ]
  )
endif

# 'meson setup builddir -Dfsan_enable=true', will show fsanitize when running binary.
# Make sure fsan is available, otherwise you might encounter linker errors.
fsan_enable = get_option('fsan_enable')
if (fsan_enable)
  fsan_args = [
    '-fsanitize=address',
    '-fsanitize=undefined',
    '-fsanitize=leak',
    '-g'
  ]
  message('Fsanitize flag is enabled.')
else
  fsan_args = []
endif

src = []

executable(
  'exe_name',
  src,
  c_args: fsan_enable ? [fsan_args, warn_flags] : warn_flags,
  link_args: fsan_enable ? fsan_args : []
)

