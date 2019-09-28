# bicubic-interpolation-pytorch-version-the-same-results-with-matlab-imresize
A version of matlab function 'imresize' using 'bicubic' interpolation, realized by pytorch and 
could acclearte by cuda. So it can be plug in nerual networks . While many interpolation methods 
in python like scipy.misc.imresize and torch.nn.function.Upsample(interpolation) and so on. 
They outputs different results with the results on matlab version. 
And I will update an python version 'bicubic' using numpy as soon as possible. 
And of course it can not acclerate by cuda, resulting slower results.
