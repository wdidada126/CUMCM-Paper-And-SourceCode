cmake_minimum_required(VERSION 3.10)
project(Gemini_ICPC_2025)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Enable warnings
if(MSVC)
    add_compile_options(/W4)
else()
    add_compile_options(-Wall -Wextra -pedantic)
endif()

# Problem A executable
add_executable(problem_a a.cpp)
target_include_directories(problem_a PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})

# Problem C executable
add_executable(problem_c c.cpp)
target_include_directories(problem_c PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})

# Problem D executable
add_executable(problem_d d.cpp)
target_include_directories(problem_d PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})

# Problem E executable
add_executable(problem_e e.cpp)
target_include_directories(problem_e PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})

# Problem F executable
add_executable(problem_f f.cpp)
target_include_directories(problem_f PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})

# Problem H executable
add_executable(problem_h h.cpp)
target_include_directories(problem_h PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})

# Problem I executable
add_executable(problem_i i.cpp)
target_include_directories(problem_i PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})

# Problem J executable
add_executable(problem_j j.cpp)
target_include_directories(problem_j PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})

# Problem K executable
add_executable(problem_k k.cpp)
target_include_directories(problem_k PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})

# Problem L executable
add_executable(problem_l l.cpp)
target_include_directories(problem_l PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})

message(STATUS "Build configuration complete.")
message(STATUS "Available executables:")
message(STATUS "  problem_a - Problem A solution")
message(STATUS "  problem_c - Problem C solution")
message(STATUS "  problem_d - Problem D solution")
message(STATUS "  problem_e - Problem E solution")
message(STATUS "  problem_f - Problem F solution")
message(STATUS "  problem_h - Problem H solution")
message(STATUS "  problem_i - Problem I solution")
message(STATUS "  problem_j - Problem J solution")
message(STATUS "  problem_k - Problem K solution")
message(STATUS "  problem_l - Problem L solution")
message(STATUS "Use 'make' to build all projects.")
message(STATUS "Use './problem_X' to run specific problem solution.")