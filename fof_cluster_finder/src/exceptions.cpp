#include "exceptions.hpp"

BadArgumentException::BadArgumentException(const std::string& arg_name,
        const std::string& expected):
std::invalid_argument(arg_name){
    message.append("BadArgumentException, \"").append(arg_name).append("\" value. Input value must be ")
            .append(expected).append(".");
}

BadArgumentException::BadArgumentException(const std::string& context,
        const std::string& arg_name, const std::string& expected):
std::invalid_argument(arg_name){
    message.append("BadArgumentException in ").append(context).append(", \"").append(arg_name).
            append("\" value. Input value must be ").append(expected).append(".");
}
const char* BadArgumentException::what() const throw(){
    return message.c_str();
}

DomainException::DomainException(const std::string& context, const std::string& report):
std::domain_error(report){
  message.append("DomainException in ").append(context).append(". ").append(report).append(".");
}
const char* DomainException::what() const throw(){
    return message.c_str();
}

RuntimeException::RuntimeException(const std::string& context,
        const std::string& member_name, const std::string& expected):
std::runtime_error(member_name){
    message.append("RuntimeException in ").append(context).append(", \"").append(member_name).
            append("\" value. Member value must be ").append(expected).append(".");
}
const char* RuntimeException::what() const throw(){
    return message.c_str();
}
