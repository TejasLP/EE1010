#include <stdio.h>
#include <math.h>

double f(double x) {
    return exp(x)-2;
}

double df(double x) {
    return exp(x);
}

int main() {
    double x = 1.0;
    double tol = 1e-6;
    int max_iter = 100;

    for (int i = 0; i < max_iter; i++) {
        double x_next = x - f(x) / df(x);
        if (fabs(x_next - x) < tol) {
            x = x_next;
            break;
        }
        x = x_next;
    }

    printf("Approximate root: %.5f\n", x);
    return 0;                                                                                                                                            }
