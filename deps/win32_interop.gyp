{
  'targets': [
    {
      'target_name': 'win32_interop',
      'type': 'static_library',
      'direct_dependent_settings': {
        'include_dirs': [ '.' ],
      },
      'sources': [
        './win32_interop/win32fixes.c',
        './win32_interop/Win32_ANSI.c',
        './win32_interop/Win32_FDAPI.cpp',
        './win32_interop/Win32_fdapi_crt.cpp',
        './win32_interop/win32_rfdmap.cpp',
        './win32_interop/Win32_variadicFunctor.cpp',
      ],
    }
  ]
}