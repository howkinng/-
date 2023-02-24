import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    private ArrayList<String> notes;

    public Main() {
        notes = new ArrayList<String>();
    }

    public void addNote() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your note: ");
        String note = scanner.nextLine();
        notes.add(note);
    }

    public void editNote() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the index of the note to edit: ");
        int index = scanner.nextInt();
        scanner.nextLine();
        System.out.print("Enter the updated note: ");
        String note = scanner.nextLine();
        notes.set(index, note);
    }

    public void deleteNote() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the index of the note to delete: ");
        int index = scanner.nextInt();
        notes.remove(index);
    }

    public void displayNotes() {
        System.out.println("Notes:");
        for (int i = 0; i < notes.size(); i++) {
            System.out.println(i + ": " + notes.get(i));
        }
    }

    public static void main(String[] args) {
        Notebook notebook = new Notebook();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Menu:");
            System.out.println("1. Add a new note");
            System.out.println("2. Edit an existing note");
            System.out.println("3. Delete a note");
            System.out.println("4. Display all notes");
            System.out.println("5. Quit");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    notebook.addNote();
                    break;
                case 2:
                    notebook.editNote();
                    break;
                case 3:
                    notebook.deleteNote();
                    break;
                case 4:
                    notebook.displayNotes();
                    break;
                case 5:
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice. Try again.");
                    break;
            }
        }
    }
}
