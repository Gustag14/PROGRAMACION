#include <stdio.h>
#include <time.h>

/*
    Programa de práctica en C
    Simula un pequeño entrenamiento de un robot
*/

// Función que calcula el doble de la energia
int calcularDobleEnergia(int energia){
    int doble = energia * 2;
    return doble;
}

int main(){

    // Mensaje inicial
    printf("Inicio del entrenamiento del robot\n");
    printf("----------------------------------\n");

    // Variables básicas
    int energia = 47;
    int puntos = 4 + 3;
    float velocidad = 1.0000000432;
    int dia;

    // Operación matemática
    printf("Puntos iniciales del robot: %i\n", puntos);

    // Comparadores
    int menorque = energia < 30;
    int mayorque = energia > 30;
    int igualdad = energia == 47;
    int desigualdad = energia != 10;

    printf("Energia menor que 30: %i\n", menorque);
    printf("Energia mayor que 30: %i\n", mayorque);
    printf("Energia igual a 47: %i\n", igualdad);
    printf("Energia distinta de 10: %i\n", desigualdad);

    // Operadores lógicos
    int robotPreparado = energia > 20 && puntos >= 7;
    int robotPuedeEntrenar = energia > 80 || puntos >= 7;

    printf("Robot preparado con AND: %i\n", robotPreparado);
    printf("Robot puede entrenar con OR: %i\n", robotPuedeEntrenar);

    // Condicionales
    if(energia < 10){
        printf("El robot tiene muy poca energia\n");
    }else if(energia < 30 && energia >= 10){
        printf("El robot tiene energia baja\n");
    }else if(energia < 60 && energia >= 30){
        printf("El robot tiene energia media\n");
    }else if(energia >= 60){
        printf("El robot tiene energia alta\n");
    }else{
        printf("El valor de energia no es correcto\n");
    }

    // Uso de una función
    int energiaDoble = calcularDobleEnergia(energia);
    printf("El doble de energia del robot es: %i\n", energiaDoble);

    // Bucle for
    printf("\nPlan de entrenamiento semanal:\n");

    for(dia = 1; dia <= 7; dia++){
        printf("Dia %i: entrenamiento completado\n", dia);
    }

    // Medición de tiempo
    clock_t inicio, fin;
    double tiempo;

    inicio = clock();

    int contador;

    for(contador = 0; contador <= 50000000; contador++){
        velocidad = velocidad * 1.00000000645;
    }

    fin = clock();

    tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;

    printf("\nVelocidad final del robot: %f\n", velocidad);
    printf("Tiempo de ejecucion: %f segundos\n", tiempo);

    return 0;
}