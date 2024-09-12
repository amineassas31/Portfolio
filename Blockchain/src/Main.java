
public class Main {
    public static void main(String[] args) {
        Blockchain blockchain = new Blockchain();
        blockchain.ajouterBlock("3000");
        blockchain.ajouterBlock("NPU");
        blockchain.ajouterBlock("@");
        blockchain.afficherBlockchain();

    }


}