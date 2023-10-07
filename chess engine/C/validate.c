#include "defs.h"
#include "stdio.h"
#include "string.h"

int SqOnBoard(const int sq)
{
    return FilesBrd[sq] == OFFBOARD ? 0 : 1;
}