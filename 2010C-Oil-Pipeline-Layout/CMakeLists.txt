cmake_minimum_required(VERSION 3.10)
project(OilPipelineLayout_2010C)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Program 1: Company 3 evaluation - minimum total cost
add_executable(company3_eval_2_1
    "company3_eval_2_1.cpp"
)

# Program 2: Company 3 evaluation - total cost calculation
add_executable(company3_eval_3_1
    "company3_eval_3_1.cpp"
)

message(STATUS "Build configuration complete.")
message(STATUS "Run 'make' to build the projects.")
message(STATUS "Use './company3_eval_2_1' and './company3_eval_3_1' to run the programs.")
