#ifndef FOF_EXCEPTIONS_HPP
#define FOF_EXCEPTIONS_HPP

#include <stdexcept>
#include <string>

class BadArgumentExeception : public std::invalid_argument
{
public:
    BadArgumentExeception(const std::string& arg_name, const std::string& expected);
    BadArgumentExeception(const std::string& context,
            const std::string& arg_name, const std::string& expected);
    virtual ~BadArgumentExeception() throw(){}
    virtual const char* what() const throw();
protected:
    std::string message;

};

#endif
