import random
import math
import json

class Blockchain:
    class _Block:
        def __init__(self, donnee, hash_precedent, hash_value=None):

            if hash_value:
                self.hash = hash_value
            else:
                self.hash = int(math.pow(10, 6) + random.randint(0, int(math.pow(10, 7) - math.pow(10, 6))))
            self.hash_precedent = hash_precedent
            self.donnee = donnee

        def to_dict(self):
            return {
                'hash': self.hash,
                'hash_precedent': self.hash_precedent,
                'donnee': self.donnee
            }

        @classmethod
        def from_dict(cls, data):
            return cls(data['donnee'], data['hash_precedent'], data['hash'])

        def get_hash(self):
            return self.hash

        def get_hash_precedent(self):
            return self.hash_precedent

        def get_donnee(self):
            return self.donnee

    def __init__(self):
        self.chaine = []

    def ajouter_block(self, donnee):
        hash_precedent = 0
        if len(self.chaine) > 0:
            hash_precedent = self.chaine[-1].get_hash()
        self.chaine.append(self._Block(donnee, hash_precedent))

    def afficher_blockchain(self):
        for i, block in enumerate(self.chaine):
            print(f"Block {i + 1}")
            print(f"Donnee: {block.get_donnee()}")
            print(f"Hash: {block.get_hash()}")
            print(f"Hash precedent: {block.get_hash_precedent()}")
            print("----------------------------")

    def est_dans_la_blockchain(self, hash_value):
        for block in self.chaine:
            if block.get_hash() == hash_value:
                return True
        return False

    def sauvegarder(self, filename):
        with open(filename, 'w') as file:
            chaine_data = [block.to_dict() for block in self.chaine]
            json.dump(chaine_data, file, indent=4)

    def recuperer(self, filename):
        with open(filename, 'r') as file:
            chaine_data = json.load(file)
            self.chaine = [self._Block.from_dict(block_data) for block_data in chaine_data]
        print(f"Blockchain loaded from {filename}.")
