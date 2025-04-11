import java.util.Scanner;

class User {
    protected String username;
    protected String password;

    public void register(String name, String pw) {
        this.username = name;
        this.password = pw;
        System.out.println("Username: " + username);
        System.out.println("Password: " + password);
    }

    public void notification(){
        System.out.println("user created by User");
        System.out.println("----");
    }
}

class Admin extends User {
    private final String role = "Admin";

    @Override
    public void notification() {
        System.out.println("User created by " + role);
    }
}

public class App {
    public static void main(String[] args) throws Exception {
        try (Scanner input = new Scanner(System.in)) {
            System.out.println("Enter username: ");
            String name = input.nextLine();
            System.out.println("Enter password: ");
            String pw = input.nextLine();
            System.out.println("---");
            User user = new User();
            user.register(name, pw);
            user.notification();
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
