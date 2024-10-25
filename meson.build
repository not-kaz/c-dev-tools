project(
  'example',
  'c',
  default_options : [
    'c_std=c11',
    'warning_level=3',
    'buildtype=debug',
    'default_library=static'
    ]
)

warn_flags = [
  '-Wpedantic',
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

system = host_machine.system()

if system == 'linux'
  # TODO: Implement Linux specific dependencies
elif system == 'windows'
  # TODO: Implement Windows specific dependencies
endif

add_project_arguments(
  warn_flags,
  language: 'c'
)

src = ['main.c']

executable(
  'exe',
  src,
  dependencies:
)
