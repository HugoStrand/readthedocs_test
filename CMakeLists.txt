
# Path for local cmake modules
list(APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake)

add_subdirectory(c++)
add_subdirectory(pyfoobar)
add_subdirectory(doc)
