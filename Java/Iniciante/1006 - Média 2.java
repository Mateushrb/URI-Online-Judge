package Iniciante;
import java.util.Locale;
import java.util.Scanner;
class Main_1006 {
    public static void main(String args[]) {
        Locale.setDefault(Locale.US);
        Scanner entrada_dados = new Scanner(System.in);

        double A = entrada_dados.nextDouble();
        double B = entrada_dados.nextDouble();
        double C = entrada_dados.nextDouble();

        double media = (A*2 + B*3 + C*5) / 10;

        System.out.printf("MEDIA = %.1f\n", media);

        entrada_dados.close();
    }
}