#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "RAPLCap::raplcap-msr" for configuration ""
set_property(TARGET RAPLCap::raplcap-msr APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(RAPLCap::raplcap-msr PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libraplcap-msr.so.0.9.0"
  IMPORTED_SONAME_NOCONFIG "libraplcap-msr.so.0"
  )

list(APPEND _IMPORT_CHECK_TARGETS RAPLCap::raplcap-msr )
list(APPEND _IMPORT_CHECK_FILES_FOR_RAPLCap::raplcap-msr "${_IMPORT_PREFIX}/lib/libraplcap-msr.so.0.9.0" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
