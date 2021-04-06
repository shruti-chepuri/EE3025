#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define PI 3.141592653589793


typedef struct Comp {
    double r, i;
} Comp;



void comp_print(Comp comp) {
    printf("%.6f + %.6f i\n", comp.r, comp.i);
}


void fft(const Comp *sig, Comp *f, int s, int n, int inv) {
    int i, hn = n >> 1;
    double theta = (inv ? PI : -PI) / (double)hn;
    Comp ep,ei;
    ep.r = cos(theta); ep.i = sin(theta);
    Comp *pi = &ei, *pp = &ep;
    if (!hn) *f = *sig;
    else
    {
        fft(sig, f, s << 1, hn, inv);
        fft(sig + s, f + hn, s << 1, hn, inv);
        pi->r = 1;
        pi->i = 0;
        for (i = 0; i < hn; i++)
        {
            Comp even = f[i], *pe = f + i, *po = pe + hn;
            double nr = po->r * pi->r - po->i * pi->i;
            double ni = po->i * pi->r + po->r * pi->i;
            po->r = nr;
            po->i = ni;
            pe->r += po->r;
            pe->i += po->i;
            po->r = even.r - po->r;
            po->i = even.i - po->i;
            nr = pi->r * pp->r - pi->i * pp->i;
            ni = pi->i * pp->r + pi->r * pp->i;
            pi->r = nr;
            pi->i = ni;
        }
    }
}


int main() {
    FILE *fout;
    int n, i, k;
    //k = 3;
    n = 8;
    Comp sig[n], sig0[n];
    double sigr[]= {1,2,3,4,4,3,2,1};
    for (i = 0; i < n; i++)
    {
        sig[i].r = sigr[i];
        sig[i].i = 0;
    }
    double realv[n];
    double imagv[n];
    fft(sig, sig0, 1, n, 0);
    fout  = fopen("fft_values.dat", "w");
     for (i = 0; i < n; i++){
        realv[i] = sig0[i].r;
        imagv[i] = sig0[i].i;
        comp_print(sig0[i]);
        
    }
    
    for(int i = 0; i < n; i++){
        fprintf(fout, "%lf \n", realv[i]);
        fprintf(fout, "%lf \n", imagv[i]);
        //printf("%lf", y[i]);
    }
    fclose(fout);
    return 0;
}

