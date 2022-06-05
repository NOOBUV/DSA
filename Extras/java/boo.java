public class boo {
    public boo(int i) {
        System.out.print(i + 1);
    }

    public boo(int i, String j) {
        System.out.print(j);
    }

    public class Main {
        static void myMethod() {
            boo baby = new SonOfBoo(1);
        }
    }
}

class SonOfBoo extends boo {
    public SonOfBoo(int i) {
        super(i);
    }
}
