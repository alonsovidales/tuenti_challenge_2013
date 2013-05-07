import encript.SimpleCrypto;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Ok, this is what I did to solve this problem:
 *  - I downloaded the Android SDK (for Mac)
 *  - I runned the signal.apk on the emulator
 *  - I extracted the classes.dex from the signal.apk, this is the file who contains all the classes
 *  - I used the dex2jar application to extract the .class files:
 *       https://code.google.com/p/dex2jar/
 *  - With the .class files, I used this Java decompiler to get .java code:
 *       http://java.decompiler.free.fr/
 *  - Checking the code of ContestProvider.java, I discovered that it uses a SQLlite database, you have the file in:
 *       src/ContestProvider.java
 *  - Then, I used the Eclipse of the SDK to extract the SQLLite database from the emulator
 *  - You have the database in:
 *       src/contest.db
 *  - Well, on the database I checked the table "contest" who contains some extrange strings on base 64 I supposed
 *  - Checking a little bit more the code, I discovered that is was encrypted using the SimpleCrypto class, you have
 *    this class on:
 *      encript/SimpleCrypto.java 
 *  - On the code, I discovered that the key used is: "test"
 *  - Well, I created this file who using the discovered strings and using the SimpleCrypto class gets the output XD
 *
 * And that's all, was too hard, but amazing :) I don't have any experience with android apps and I didn't use Java
 * in more than 6 years
 *
 * @author Alonso Vidales <alonso.vidales@tras2.es>
 */

public class Problem {
    public static void main(String[] args) throws IOException {
        SimpleCrypto localSimpleCrypto2 = new SimpleCrypto("test");

        String line;
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        line = reader.readLine();
        int number = Integer.valueOf(line.trim());

        switch (number) {
            case 0:
                System.out.println(localSimpleCrypto2.decrypt("BNCGuyEC70Q="));
                break;

            case 1:
                System.out.println(localSimpleCrypto2.decrypt("KUJKbD/UFDg="));
                break;

            case 2:
                System.out.println(localSimpleCrypto2.decrypt("boXiRXOEItw="));
                break;

            case 3:
                System.out.println(localSimpleCrypto2.decrypt("meKQj+Vj6Z8="));
                break;

            case 4:
                System.out.println(localSimpleCrypto2.decrypt("U0I2iKX+sa0="));
                break;
        }
    }
}
