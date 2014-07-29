#include "exceptions.hpp"

BadArgumentExeception::BadArgumentExeception(const std::string& arg_name,
        const std::string& expected):
std::invalid_argument(arg_name){
    message.append("BadArgumentExeception ").append(arg_name).append(" value. It must be ")
            .append(expected);
}

BadArgumentExeception::BadArgumentExeception(const std::string& context,
        const std::string& arg_name, const std::string& expected):
std::invalid_argument(arg_name){
    message.append("BadArgumentExeception in ").append(context).append(", \"").append(arg_name).
            append("\" value. Input value must be ").append(expected).append(".");
}
const char* BadArgumentExeception::what() const throw(){
    return message.c_str();
}
