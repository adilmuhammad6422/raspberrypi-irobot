#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "create" for configuration ""
set_property(TARGET create APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(create PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libcreate.so"
  IMPORTED_SONAME_NOCONFIG "libcreate.so"
  )

list(APPEND _cmake_import_check_targets create )
list(APPEND _cmake_import_check_files_for_create "${_IMPORT_PREFIX}/lib/libcreate.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
