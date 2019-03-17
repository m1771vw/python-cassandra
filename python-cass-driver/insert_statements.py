import random 

def insert_dog(session, name, breed, size, avg_weight):
    session.execute(
    """
    INSERT INTO dogs (name, breed, size, avg_weight)
    VALUES (%(name)s, %(breed)s, %(size)s, %(avg_weight)s)
    """,
    {
     'name': name,
     'breed': breed,
     'size': size,
     'avg_weight': avg_weight
    }
)

def generate_name():
    first_name = ["Miki", "Nobu", "Spot", "Charlie", "Barkley",
                  "Diane", "Bojack", "Sebastian", "Snow", "Kinko",
                  "Todd", "Princess", "Miko", "Max", "Charlie",
                  "Cooper", "Buddy","Jack","Rocky","Duke",
                  "Bear","Tucker", "Oliver","Bella", "Lucy",  
                  "Luna", "Daisy","Lola","Sadie","Molly",
                  "Bailey","Maggie","Stella"]
    second_name = ["Miki", "Nobu", "Spot", "Charlie", "Barkley",
                  "Diane", "Bojack", "Sebastian", "Snow", "Kinko",
                  "Todd", "Princess", "Miko", "Max", "Charlie",
                  "Cooper", "Buddy","Jack","Rocky","Duke",
                  "Bear","Tucker", "Oliver","Bella", "Lucy",  
                  "Luna", "Daisy","Lola","Sadie","Molly",
                  "Bailey","Maggie","Stella"]
    return first_name[random.randint(0, len(first_name)-1)] + " " + second_name[random.randint(0, len(second_name)-1)]
    
def generate_breed():
    breed = [
        "affenpinscher", "Afghan hound", "Airedale terrier", "Akita", 
        "Alaskan Malamute", "American Staffordshire terrier", 
        "American water spaniel", "Australian cattle dog", 
        "Australian shepherd", "Australian terrier", "basenji", 
        "basset hound", "beagle", "bearded collie", "Bedlington terrier", 
        "Bernese mountain dog", "bichon frise", "black and tan coonhound", 
        "bloodhound", "border collie", "border terrier", "borzoi", 
        "Boston terrier", "bouvier des Flandres", "boxer", "briard", 
        "Brittany", "Brussels griffon", "bull terrier", "bulldog", 
        "bullmastiff", "cairn terrier", "Canaan dog", "Chesapeake Bay retriever", 
        "Chihuahua", "Chinese crested", "Chinese shar-pei", "chow chow", 
        "Clumber spaniel", "cocker spaniel", "collie", "curly-coated retriever", 
        "dachshund", "Dalmatian", "Doberman pinscher", "English cocker spaniel", 
        "English setter", "English springer spaniel", "English toy spaniel", "Eskimo dog", 
        "Finnish spitz", "flat-coated retriever", "fox terrier", "foxhound", 
        "French bulldog", "German shepherd", "German shorthaired pointer", 
        "German wirehaired pointer", "golden retriever", "Gordon setter", 
        "Great Dane", "greyhound", "Irish setter", "Irish water spaniel", 
        "Irish wolfhound", "Jack Russell terrier", "Japanese spaniel", 
        "keeshond", "Kerry blue terrier", "komondor", "kuvasz", 
        "Labrador retriever", "Lakeland terrier", "Lhasa apso", 
        "Maltese", "Manchester terrier", "mastiff", "Mexican hairless", 
        "Newfoundland", "Norwegian elkhound", "Norwich terrier", "otterhound", 
        "papillon", "Pekingese", "pointer", "Pomeranian", "poodle", "pug", 
        "puli", "Rhodesian ridgeback", "Rottweiler", "Saint Bernard", "saluki", 
        "Samoyed", "schipperke", "schnauzer", "Scottish deerhound", 
        "Scottish terrier", "Sealyham terrier", "Shetland sheepdog", "shih tzu", 
        "Siberian husky", "silky terrier", "Skye terrier", 
        "Staffordshire bull terrier", "soft-coated wheaten terrier", 
        "Sussex spaniel", "spitz", "Tibetan terrier", "vizsla", "Weimaraner", 
        "Welsh terrier", "West Highland white terrier", "whippet", "Yorkshire terrier"
    ]
    return breed[random.randint(0, len(breed)-1)]

def generate_size():
    size = ["Extra Small", "Small", "Medium", "Large", "Extra Large"]
    return size[random.randint(0, len(size)-1)]

def generate_avg_weight():
    return random.randint(20, 251)

