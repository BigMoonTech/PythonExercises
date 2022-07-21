class GrumpyDict(dict):
    def __repr__(self):
        print("WTF? WHY DO YOU EVEN CARE?")
        return super().__repr__()

    def __missing__(self, key):
        print(f"YOU WANT {key}? YEAH RIGHT.")

    def __setitem__(self, key, value):
        print(f"UGH. I GUESS I'LL ADD {value.upper()}!!! FML.")
        super().__setitem__(key, value)

grump = GrumpyDict({"first": "Tom", "last": "Jones"})

print(grump)
grump["city"] = "Denver"
print(grump)