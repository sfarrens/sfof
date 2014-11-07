#ifndef FOF_EXCEPTIONS_HPP
#define FOF_EXCEPTIONS_HPP

#include <stdexcept>
#include <string>

//! Class for bad argument exceptions.
class BadArgumentException : public std::invalid_argument
{
public:
    BadArgumentException(const std::string& arg_name, const std::string& expected);
    BadArgumentException(const std::string& context,
            const std::string& arg_name, const std::string& expected);
    virtual ~BadArgumentException() throw(){}
    virtual const char* what() const throw();
protected:
    std::string message;

};

//! Class for domain exceptions.
class DomainException : public std::domain_error
{
public:
    DomainException(const std::string& context, const std::string& report);
    virtual ~DomainException() throw(){}
    virtual const char* what() const throw();
protected:
    std::string message;

};

//! Class for runtime exceptions.
class RuntimeException : public std::runtime_error
{
public:
    RuntimeException(const std::string& context, const std::string& member_name, 
		      const std::string& expected);
    virtual ~RuntimeException() throw(){}
    virtual const char* what() const throw();
protected:
    std::string message;

};

#endif
