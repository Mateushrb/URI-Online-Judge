package Iniciante;

import java.util.Locale;
import java.util.Scanner;

class Main_1005 {
    public static void main(String args[]) {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);

        float A = input.nextFloat();
        float B = input.nextFloat();

        double MEDIA = ((A*3.5) + (B*7.5)) / 11;

        System.out.printf("MEDIA = %.5f\n", MEDIA);
        input.close();
    }
}
