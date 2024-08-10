abstract class PaymentMethod {
    abstract void pay();
}

class CreditCard extends PaymentMethod {
    private String ccNo;
    private String expDate;
    private String cvv;

    public CreditCard(String ccNo, String expDate, String cvv) {
        this.ccNo = ccNo;
        this.expDate = expDate;
        this.cvv = cvv;
    }

    @Override
    void pay() {
        System.out.println("Payment successful using Credit Card. Details:");
        System.out.println("Card Number: " + ccNo);
        System.out.println("Expiration Date: " + expDate);
        System.out.println("CVV: " + cvv);
    }
}

class PayPal extends PaymentMethod {
    private String email;

    public PayPal(String email) {
        this.email = email;
    }

    @Override
    void pay() {
        System.out.println("Payment successful using PayPal. Email: " + email);
    }
}

class Bitcoin extends PaymentMethod {
    private String walletAddress;

    public Bitcoin(String walletAddress) {
        this.walletAddress = walletAddress;
    }

    @Override
    void pay() {
        System.out.println("Payment successful using Bitcoin. Wallet Address: " + walletAddress);
    }
}

public class Main {
    public static void main(String[] args) {
        PaymentMethod creditCard = new CreditCard("1234-5678-9876-5432", "12/25", "123");
        PaymentMethod payPal = new PayPal("user@example.com");
        PaymentMethod bitcoin = new Bitcoin("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa");

        creditCard.pay();
        payPal.pay();
        bitcoin.pay();
    }
}
