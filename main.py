# nom, prix, ingrédients, végétariènne
class Pizza:
    def __init__(self, nom, prix, ingredients, vegetarienne=False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne

    def Affichez(self):
        veg_str = ""
        if self.vegetarienne:
            veg_str = " - VEGETARIENNE"
            print(f"PIZZA {self.nom}: {self.prix}€ {veg_str}")
        else:
            print(f"PIZZA {self.nom}: {self.prix}€")
        print(", ".join(self.ingredients))
        print()


class PizzaPersonnalisee(Pizza):
    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENT = 1.2
    dernier_numero = 0

    def __init__(self):
        PizzaPersonnalisee.dernier_numero += 1
        self.numero = PizzaPersonnalisee.dernier_numero
        super().__init__(f"Personnalisée {self.numero}", 0, [])
        self.demander_ingredients_utilisateur()
        self.calculer_le_prix()

    def demander_ingredients_utilisateur(self):
        print()
        print(f"Ingredients pour la pizza personnalisée {self.numero}:")
        while True:
            ingredient = input(
                "Ajoutez un ingrédient (où ENTER pour terminer): ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(
                f"Vous avez {len(self.ingredients)} ingrédient(s): {', '.join(self.ingredients)}")

    def calculer_le_prix(self):
        self.prix = self.PRIX_DE_BASE + \
            self.PRIX_PAR_INGREDIENT*len(self.ingredients)
        return self.prix


pizzas = [Pizza("4 fromages", 8.5, ("brie", "emmental", "compté", "parmesan"), True),
          Pizza("bobolaise", 45.5, ("chitoumou", "pimant")),
          Pizza("Calzone", 5.5, ("emmental", "sardine", "parmesan")),
          Pizza("végétarienne", 11, ("tomate", "ail"), True),
          PizzaPersonnalisee(),
          PizzaPersonnalisee()]


def tri(e):
    return len(e.ingredients)


# pizzas.sort(key=tri)

for i in pizzas:
    i.Affichez()
