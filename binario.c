
/*ESERCIZIO 7: CONVERTITORE BINARIO*/

// PROCEDIMENTO RICORSIVO

#include <stdio.h>

void binario(int);

int main(void)
{
	int n;
	printf("Inserisci un numero intero: ");
	scanf("%d", &n);

	binario(n);
	return 0;	
}


void binario(int n)
{
	if (n == 1){
		printf("%d", 1);

	}else{
		binario(n/2); 
		int resto = n % 2;
		printf("%d", resto);
	}
}
