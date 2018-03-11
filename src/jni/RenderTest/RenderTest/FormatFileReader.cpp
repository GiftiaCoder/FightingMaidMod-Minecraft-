#include "FormatFileReader.h"

FormatFileReader::FormatFileReader(const char *path) : in(path, std::ios::binary)
{
	// do nothing
}

void FormatFileReader::ReadStr(std::string &str)
{
	const static int MAX_STR_LEN = 1024;

	int len;
	char buff[MAX_STR_LEN];

	Read(&len);
	in.read(buff, len);
	buff[len] = 0;

	str = buff;
}
