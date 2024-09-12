import java.util.LinkedList;

import java.lang.Math;

public class Blockchain{
    private class Block{
        private int hash = (int) (Math.pow(10,6) + (int)(Math.random() * (Math.pow(10,7) - Math.pow(10,6) + 1)));
        private int hashPrecedent;
        private String donnee;
        public Block(String donnee, int hashPrecedent){
            this.hashPrecedent = hashPrecedent;
            this.donnee = donnee;
        }

        public int getHash(){
            return hash;
        }
        public int getHashPrecedent(){
            return hashPrecedent;
        }
        public String getDonnee(){
            return donnee;
        }

    }
    LinkedList<Block> chaine = new LinkedList<>();

    public void ajouterBlock(String donnee){
        int hashPrecedent = 0;
        if (!chaine.isEmpty()){
            hashPrecedent = chaine.getLast().getHash();
        }

        chaine.add(new Block(donnee,hashPrecedent));
    }
    public void afficherBlockchain() {
        for (int i = 0; i < chaine.size(); i++) {
            Block block = chaine.get(i);
            System.out.println("Block " + (i + 1));
            System.out.println("Donnee: " + block.getDonnee());
            System.out.println("Hash: " + block.getHash());
            System.out.println("Hash precedent: " + block.getHashPrecedent());
            System.out.println("----------------------------");
        }
    }
    public Boolean estDansLaBlockchain(int hash){
        for (Block block : chaine) {
            if (block.getHash() == hash) {
                return true;
            }
        }
        return false;
    }


}