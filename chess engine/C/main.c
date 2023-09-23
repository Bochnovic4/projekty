#include "defs.h"
#include "stdio.h"
#include "stdlib.h"

#define FEN1 "2b5/p2NBp1p/1bp1nPPr/3P4/2pRnr1P/1k1B1Ppp/1P1P1pQP/Rq1N3K b - - 0 1"
#define FEN2 "r1bqkb1r/1ppnpppp/p4n2/3p4/8/1P3N1P/PBPPPPP1/RN1QKB1R w KQkq - 2 5"
#define FEN3 "rnbqk2r/ppppnppp/1b6/4p3/4P3/3P3P/PPP1BPP1/RNBQK1NR w KQkq - 3 5"

int main()
{
    AllInit();

    S_BOARD board[1];

    ParseFen(START_FEN, board);
    PrintBoard(board);

    ParseFen(FEN1, board);
    PrintBoard(board);

    ParseFen(FEN2, board);
    PrintBoard(board);

    ParseFen(FEN3, board);
    PrintBoard(board);
    return 0;
}