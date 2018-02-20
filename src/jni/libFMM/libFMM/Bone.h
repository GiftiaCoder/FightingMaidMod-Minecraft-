#pragma once

#include "cuArray.h"

#include <string>
#include <vector>

class Bone
{
private:
	std::string name;
	std::vector<Bone *> childern;
};
