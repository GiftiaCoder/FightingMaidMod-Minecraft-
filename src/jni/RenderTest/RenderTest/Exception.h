#pragma once

#include <iostream>
#include <string>

struct stException {
	char *msg;
	char *file;
	char *function;
	int line;
	std::string detail;
};

std::ostream& operator << (std::ostream &out, stException &exception);

#define CREATE_EXCEPTION(_msg_, _dtal_) stException{ \
	_msg_, \
	__FILE__, \
	__FUNCTION__, \
	__LINE__, \
	_dtal_}
#define NULL_STR "(NULL)"

#define MSG_FILE_CANT_ACCESS "File Not Exist !"

#define EXCEPTION_FILE_CANT_ACCESS(_dtal_) CREATE_EXCEPTION(MSG_FILE_CANT_ACCESS, _dtal_)

