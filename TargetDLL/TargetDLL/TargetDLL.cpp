// TargetDLL.cpp : Defines the exported functions for the DLL application.
//

#include "stdafx.h"
#include <stdio.h>
#include <iostream>

#define API_FUNCTION extern "C" __declspec(dllexport)


API_FUNCTION float DllFunction(int a, int b, int c, float* pArray, int N)
{

	for (int idx = 0; idx < N; ++idx)
	{
		pArray[idx] = (float)idx;

		//std::cout << pArray[idx];

		//printf("%f\n", pArray[idx]);
	}

	return (float)(a+b+c);
}




API_FUNCTION int VectorSum(float* c, float* a, float* b, int N)
{

	for (int idx = 0; idx < N; ++idx)
	{
		c[idx] = a[idx] + b[idx];
	}


	return 0;
}




struct AStruct
{
	int a;
	int b;
	int c;
	float z;
};

API_FUNCTION int GiveMyStructAsPointer(AStruct* pStruct)
{
	printf("Contents of the struct param: %d %d %d %f\n", pStruct->a, pStruct->b, pStruct->c, pStruct->z);


	return 0;
}