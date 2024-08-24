//TECNOLOGICO CAMPUS SAN JUAN DEL RIO
//Lindero Leyva Zaira Yumelli
//Version 1.1

//A una n cantidad de alumnos pedir al usuario el nombre y 3 calificaciones de 0-100
//de n cantidad de alumnos, calcular promedio si la calificacion es menor a 70 Escribir REPROBADO
// determinar el alumno con mayor y meno calificacion.

//ALGORITMO 
//1. Inicio 
//2. Definir las variables: n <- 0, a <- 0, Cal1 <- 0, Cal2 <- 0, Cal3, <- 0, may <- 0, men <- 0, prom <- 0.0, ma <- 0.0, me <- 0.0
//3. Escribir "Ingrese la cantidad de alumnos: ", n
//4. may <- -1
//5. men <- 101
//6. Para a <- 1 hasta n
//	6.1 Escribir "Ingrese el nombre del alumno ",a," : ",nom
//	6.2 Escribir "Ingrese la 1° calificación: ",Cal1
//	6.3 Escribir "Ingrese la 2° calificación: ", Cal2
//	6.4 Escribir "Ingrese la 3° calificación: ", Cal3
//7. Calcular: prom <- (a + b + c) / 3
//8. Si prom < 70 Entonces
//	8.1 Escribir "REPROBADO"
//9. SiNo
//	9.1 Escribir "APROBADO"
//10. FinSi
//11. Si prom > mayor Entonces
//	11.1 mayor <- prom
//	11.2 ma <- nom
//12. FinSi
//11. Si prom > menor Entonces
//	11.1 menor <- prom
//	11.2 me <- nom
//12. FinSi
//13. FinPara
//14. Escribir "El alumno con el mayor promedio es ",ma," con promedio de: ",may
//14. Escribir "El alumno con el menor promedio es ",me," con promedio de: ",men
//15.FinAlgoritmo

Algoritmo Calificaciones
	
	Definir n, a Como Entero
	Definir nom, ma, me Como Caracter
	Definir Cal1, Cal2, Cal3, may, men Como Real
	
	Imprimir  "Ingrese la cantidad de alumnos: "
	leer n
	
	may <- -1
	men <- 101
	
	Para a <- 1 hasta n
		Imprimir  "Ingrese el nombre del alumno ",a," : "
		leer nom
	
	
		Imprimir  "Ingrese la 1° calificación: "
		leer Cal1
		Imprimir  "Ingrese la 2° calificación: "
		leer Cal2
		Imprimir  "Ingrese la 3° calificación: "
		leer Cal3
	
		prom <- (Cal1 + Cal2 + Cal3) / 3
	
		Si prom < 70 Entonces
			Escribir "REPROBADO"
		SiNo
			Escribir "APROBADO"
		FinSi
	
		Si prom > may Entonces
			may <- prom
			ma <- nom
		FinSi
	
		Si prom > men Entonces
			men <- prom
			me <- nom
		FinSi
	FinPara
	
	Escribir "El alumno con el mayor promedio es ",ma," con promedio de: ",may
	Escribir "El alumno con el menor promedio es ",me," con promedio de: ",men
	
FinAlgoritmo
