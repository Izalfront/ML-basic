import java.util.Scanner;
import java.util.UUID;

// Abstract class Display
abstract class Display {
    abstract void notification();

    void token(UUID id) {
        System.out.println("Generated token ID: " + id);
    }
}

// User extends Display (implementasi abstract class)
class User extends Display {
    protected String username;
    protected String password;
    protected UUID id;

    public User() {
        this.id = UUID.randomUUID(); // Token dibuat saat objek dibuat
        System.out.println("User created with ID: " + id);
    }

    public void register(String name, String pw) {
        this.username = name;
        this.password = pw;
        System.out.println("Username: " + username);
        System.out.println("Password: " + password);
    }

    @Override
    public void notification() {
        System.out.println("User created by User");
        token(id); // panggil method dari abstract class
        System.out.println("----");
    }
}

// Admin extends User dan override notification()
class Admin extends User {
    private final String role = "Admin";

    @Override
    public void notification() {
        System.out.println("User created by " + role);
        token(id); // tetap bisa pakai token dari abstract class
        System.out.println("----");
    }
}

// Main class
public class App {
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            System.out.print("Enter username: ");
            String name = input.nextLine();
            System.out.print("Enter password: ");
            String pw = input.nextLine();
            System.out.println("---");

            // Bisa pilih User atau Admin Polymorphism
            User user = new User();
            user.register(name, pw);
            user.notification();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
