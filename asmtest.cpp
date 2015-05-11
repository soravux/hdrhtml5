#include <stdio.h>
#include <math.h>

extern "C" {
inline float clipF(float n, float min, float max){
    return fmax(min, fmin(n, max));
}

// No restrict? :-(
int C_linear(float* src, float* dst, int length, float min, float max){
    float range = max - min;
    for(int i=0; i<length; i+=4){
        dst[i] = clipF((src[i] - min) / range * 255., 0., 255.);
        dst[i+1] = clipF((src[i+1] - min) / range * 255., 0., 255.);
        dst[i+2] = clipF((src[i+2] - min) / range * 255., 0., 255.);
        dst[i+3] = clipF((src[i+3] - min) / range * 255., 0., 255.);
    }
    return 0;
}
}

int main(){

    return 0;
}
