
project(readthedocs_text)

cmake_minimum_required(VERSION 3.12)

# Path for local cmake modules
list(APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake)

#add_subdirectory(c++)
#add_subdirectory(pyfoobar)
add_subdirectory(doc)
