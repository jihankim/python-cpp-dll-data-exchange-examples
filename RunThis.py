import numpy as np
from ctypes import*

# Load DLL
mydll = cdll.LoadLibrary("./TargetDLL.dll")

# Define Resturn Type
mydll.DllFunction.restype = c_float;

# Run
N = 10;
ar =(c_float*N)()
a = mydll.DllFunction(1,2,3, ar, N)
zz = np.frombuffer(ar, dtype = c_float)
#print zz





# Numpy array to C++ DLL
N = 10;
A = np.arange(N).astype(c_float);
B = np.arange(N).astype(c_float);
C = np.zeros([N, 1]).astype(c_float);

cA = A.ctypes.data_as(POINTER(c_float*N));
cB = B.ctypes.data_as(POINTER(c_float*N));
cC = C.ctypes.data_as(POINTER(c_float*N));

mydll.VectorSum(cC, cA, cB, N);

npC = np.frombuffer(cC.contents, dtype = c_float);

#print cC


print 'A', A
print 'B', B
print 'C', npC.astype(float)




# Passing a struct to C++ DLL

# Define struct
class AStruct(Structure):
    _fields_ = [
        ("a", c_int),
        ("b", c_int),
        ("c", c_int),
        ("z", c_float),
        ]


paramStruct = AStruct();
paramStruct.a = 1;
paramStruct.b = 2;
paramStruct.c = 3;
paramStruct.z = 4.0;


mydll.GiveMyStructAsPointer.argtypes = [POINTER(AStruct)]
mydll.GiveMyStructAsPointer(byref(paramStruct))





del mydll;