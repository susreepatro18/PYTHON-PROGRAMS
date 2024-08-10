abstract class Employee {
    abstract double calculateSalary();
}

class Manager extends Employee {
    private double baseSalary;
    private double bonus;

    public Manager(double baseSalary, double bonus) {
        this.baseSalary = baseSalary;
        this.bonus = bonus;
    }

    @Override
    double calculateSalary() {
        return baseSalary + bonus;
    }
}

class Developer extends Employee {
    private double baseSalary;
    private int projectCount;
    private final double projectBonus = 500; // Fixed amount per project

    public Developer(double baseSalary, int projectCount) {
        this.baseSalary = baseSalary;
        this.projectCount = projectCount;
    }

    @Override
    double calculateSalary() {
        return baseSalary + (projectCount * projectBonus);
    }
}

class Intern extends Employee {
    private double stipend;

    public Intern(double stipend) {
        this.stipend = stipend;
    }

    @Override
    double calculateSalary() {
        return stipend;
    }
}

public class Main {
    public static void main(String[] args) {
        Employee manager = new Manager(80000, 20000);
        Employee developer = new Developer(60000, 3);
        Employee intern = new Intern(30000);

        System.out.println("Manager's Salary: " + manager.calculateSalary());
        System.out.println("Developer's Salary: " + developer.calculateSalary());
        System.out.println("Intern's Salary: " + intern.calculateSalary());
    }
}
