# Product categories with tags for matching
PRODUCT_CATEGORIES = {
    # SNACKS
    "Chips": [
        # Major International Brands
        "Lay's", "Ruffles", "Doritos", "Pringles", "Cheetos", "Tostitos", "Sun Chips", "Kettle Brand", 
        "Cape Cod", "Utz", "Wise", "Popchips", "Terra Chips", "Miss Vickie's", "Takis", "Fritos", 
        "Bugles", "Stacy's Pita Chips", "Garden Fresh Gourmet", "Boulder Canyon", "Route 11", 
        "Deep River Snacks", "Late July", "Simply", "Snyder's of Hanover", "Quest Chips", "Rap Snacks",
        "Zapp's", "Golden Flake", "Better Made", "Tim's Cascade", "Hawaiian", "Dirty", "El Sabroso",
        # Store Brands
        "Great Value", "Kirkland Signature", "Trader Joe's", "Whole Foods 365", "Simple Truth",
        # Tags
        "Bag", "Crunchy", "Salty", "Snack", "Potato", "Tortilla", "Corn", "Ridged", "Flavored"
    ],

    "Crackers": [
        # Major Brands
        "Ritz", "Triscuit", "Wheat Thins", "Cheez-It", "Goldfish", "Premium", "Club", "Carr's",
        "Keebler", "Lance", "Annie's", "Back to Nature", "Late July", "Mary's Gone Crackers",
        "Milton's", "Crunchmaster", "Nabisco", "Pepperidge Farm", "Blue Diamond", "Simple Mills",
        "Nut Thins", "Kavli", "Wasa", "RyKrisp", "Water Crackers", "Sailor Boy Pilot Bread",
        # Specialty/Health
        "Doctor Kracker", "Finn Crisp", "GG Scandinavian", "Edward & Sons", "Partners",
        # Store Brands
        "Great Value", "Kirkland", "365", "Simple Truth", "Good & Gather",
        # Tags
        "Box", "Package", "Salty", "Crispy", "Whole Grain", "Gluten-Free", "Organic"
    ],

    # BEVERAGES
    "Soft Drinks": [
        # Cola Brands
        "Coca-Cola", "Pepsi", "RC Cola", "Fentimans Cola", "Fritz-Cola", "Jolt Cola", "Virgin Cola",
        "Afri Cola", "Mecca Cola", "OpenCola", "Inca Kola", "China Cola", "Double Cola", "Thums Up",
        # Lemon-Lime
        "Sprite", "7 Up", "Sierra Mist", "Mountain Dew", "Bubble Up", "Teem", "DNL",
        # Orange Sodas
        "Fanta", "Crush", "Sunkist", "Slice", "Mirinda", "Orangina", "Stewart's Orange 'n Cream",
        # Root Beer
        "A&W", "Barq's", "Mug", "Dad's", "IBC", "Stewart's", "Virgil's", "Sprecher",
        # Other Flavors
        "Dr Pepper", "Big Red", "Squirt", "Fresca", "Tab", "Surge", "Mello Yello", "Sun Drop",
        # Tags
        "Bottle", "Can", "Carbonated", "Sweet", "Diet", "Zero Sugar", "Caffeine Free"
    ],

    "Sports Drinks": [
        # Major Brands
        "Gatorade", "Powerade", "Body Armor", "Vitamin Water", "Propel", "Sqwincher", 
        "All Sport", "BioSteel", "Electrolit", "Lucozade Sport", "Pocari Sweat",
        # Natural/Organic
        "Nuun", "LMNT", "Liquid I.V.", "Hydrant", "DripDrop", "NOOMA", "Ultima Replenisher",
        # Recovery Drinks
        "Pedialyte Sport", "O.R.S.", "Normalyte", "Hydralyte",
        # Tags
        "Bottle", "Powder", "Tablets", "Electrolytes", "Zero Sugar", "Recovery", "Hydration"
    ],

    "Energy Drinks": [
        # Major Brands
        "Red Bull", "Monster", "Rockstar", "NOS", "Full Throttle", "Bang", "Reign",
        "5-Hour Energy", "Amp", "Xyience", "Celsius", "GURU", "Uptime", "Venom",
        "Redline", "G Fuel", "SPIKE", "Rip It", "Rowdy Energy", "Adrenaline Shoc",
        # Natural/Organic
        "Hiball", "Zevia Energy", "Runa", "Sambazon", "Clean Energy",
        # Store Brands
        "Kirkland Signature", "Great Value",
        # Tags
        "Can", "Bottle", "Shot", "Carbonated", "Sugar-Free", "Caffeine", "Taurine"
    ],

    "Juices": [
        # Major Brands
        "Tropicana", "Minute Maid", "Ocean Spray", "Welch's", "Simply", "Florida's Natural",
        "V8", "Mott's", "Apple & Eve", "Juicy Juice", "Capri Sun", "Sunny D", "Dole",
        "Del Monte", "Langers", "Old Orchard", "R.W. Knudsen", "Santa Cruz Organic",
        # Premium/Cold Pressed
        "Naked", "Bolthouse Farms", "Evolution Fresh", "Suja", "Blueprint", "Pressed Juicery",
        # Store Brands
        "Great Value", "Kirkland", "Simple Truth", "365",
        # Tags
        "Bottle", "Carton", "Box", "Concentrate", "Not From Concentrate", "Cold Pressed"
    ],

    # BREAKFAST & CEREAL
    "Breakfast Cereal": [
        # Kellogg's Brands
        "Frosted Flakes", "Rice Krispies", "Special K", "Froot Loops", "Corn Flakes", 
        "Apple Jacks", "Corn Pops", "All-Bran", "Smart Start", "Cracklin' Oat Bran",
        # General Mills
        "Cheerios", "Lucky Charms", "Cinnamon Toast Crunch", "Trix", "Chex", "Cocoa Puffs",
        "Count Chocula", "Fiber One", "Golden Grahams", "Kix", "Monster Cereals",
        # Post
        "Honey Bunches of Oats", "Grape-Nuts", "Pebbles", "Honeycomb", "Alpha-Bits",
        # Health Focused
        "Barbara's", "Bob's Red Mill", "Cascadian Farm", "Kashi", "Annie's",
        # Tags
        "Box", "Bag", "Breakfast", "Grain", "Ready-to-eat", "Whole Grain", "Organic"
    ],

    # HEALTH & BEAUTY
    "Shampoo": [
        # Mass Market
        "Pantene", "Head & Shoulders", "Dove", "TRESemmé", "Garnier", "L'Oreal",
        "Herbal Essences", "Aussie", "Suave", "VO5", "OGX", "John Frieda",
        # Professional
        "Matrix", "Redken", "Paul Mitchell", "Kerastase", "Aveda", "Living Proof",
        "Oribe", "Bumble and Bumble", "Moroccanoil", "Joico", "Sebastian",
        # Natural/Organic
        "Love Beauty & Planet", "Shea Moisture", "Burt's Bees", "Alba Botanica",
        # Tags
        "Bottle", "Hair Care", "Liquid", "Sulfate-Free", "Color-Safe", "Natural"
    ],

    "Toothpaste": [
        # Major Brands
        "Colgate", "Crest", "Sensodyne", "Aquafresh", "Arm & Hammer", "Tom's of Maine",
        "Closeup", "Pepsodent", "Mentadent", "Rembrandt", "Biotene",
        # Natural/Specialty
        "Hello", "Native", "Schmidt's", "Dr. Bronner's", "TheraBreath", "Desert Essence",
        # Professional
        "Prevident", "Clinpro", "Enamelon", "MI Paste",
        # Tags
        "Tube", "Oral Care", "Fluoride", "Whitening", "Sensitive", "Natural"
    ],

    # CLEANING PRODUCTS
    "Laundry Detergent": [
        # Major Brands
        "Tide", "Gain", "Persil", "All", "Arm & Hammer", "Purex", "Sun", "Era",
        "Method", "Mrs. Meyer's", "Seventh Generation", "OxiClean", "Woolite",
        # Natural/Eco-Friendly
        "Ecover", "Common Good", "Dropps", "Earth Breeze", "ECOS", "Nellie's",
        # Store Brands
        "Great Value", "Kirkland Signature", "Up&Up", "365",
        # Tags
        "Liquid", "Pods", "Powder", "HE", "Natural", "Free & Clear"
    ],

    "All-Purpose Cleaners": [
        # Major Brands
        "Lysol", "Clorox", "Mr. Clean", "Fabuloso", "Pine-Sol", "Formula 409",
        "Spic and Span", "Fantastik", "Easy-Off", "Scrubbing Bubbles",
        # Natural/Eco-Friendly
        "Method", "Mrs. Meyer's", "Seventh Generation", "Green Works", "Better Life",
        # Store Brands
        "Great Value", "Up&Up", "365", "Simple Truth",
        # Tags
        "Spray", "Liquid", "Wipes", "Disinfectant", "Natural", "Multi-Surface"
    ],

    "Paper Towels": [
        # Major Brands
        "Bounty", "Brawny", "Viva", "Scott", "Sparkle", "Marcal", "Pacific Blue",
        # Natural/Recycled
        "Seventh Generation", "Green Forest", "365 Everyday Value", "Natural Value",
        # Store Brands
        "Great Value", "Kirkland Signature", "Up&Up", "Member's Mark",
        # Tags
        "Roll", "Sheet", "Select-A-Size", "Recycled", "Multi-Purpose", "Kitchen"
    ],

    "Toilet Paper": [
        # Major Brands
        "Charmin", "Angel Soft", "Quilted Northern", "Cottonelle", "Scott", "Who Gives A Crap",
        # Natural/Recycled
        "Seventh Generation", "Green Forest", "365 Everyday Value", "Natural Value",
        # Store Brands
        "Great Value", "Kirkland Signature", "Up&Up", "Member's Mark",
        # Tags
        "Roll", "2-Ply", "3-Ply", "Soft", "Strong", "Recycled", "Bathroom"
    ],

    "Dog Food": [
        # Premium Brands
        "Royal Canin", "Hill's Science Diet", "Blue Buffalo", "Purina Pro Plan",
        "Orijen", "Acana", "Merrick", "Wellness", "Taste of the Wild",
        # Mainstream Brands
        "Purina Dog Chow", "Pedigree", "Iams", "Eukanuba", "Nutro", "Nature's Recipe",
        # Natural/Organic
        "Natural Balance", "Nature's Variety", "Castor & Pollux", "Organix",
        # Tags
        "Dry", "Wet", "Puppy", "Adult", "Senior", "Grain-Free", "Natural"
    ],

    "Cat Food": [
        # Premium Brands
        "Royal Canin", "Hill's Science Diet", "Blue Buffalo", "Purina Pro Plan",
        "Orijen", "Acana", "Merrick", "Wellness", "Taste of the Wild",
        # Mainstream Brands
        "Friskies", "Fancy Feast", "Meow Mix", "9Lives", "Iams", "Whiskas",
        # Natural/Organic
        "Natural Balance", "Nature's Variety", "Castor & Pollux", "Organix",
        # Tags
        "Dry", "Wet", "Kitten", "Adult", "Senior", "Indoor", "Grain-Free"
    ],

    "Frozen Food": [
        # Meals
        "Stouffer's", "Lean Cuisine", "Marie Callender's", "Healthy Choice",
        "Amy's Kitchen", "Evol", "Smart Ones", "Banquet", "Kid Cuisine",
        # Pizza
        "DiGiorno", "Red Baron", "Tombstone", "Tony's", "California Pizza Kitchen",
        # Vegetables
        "Birds Eye", "Green Giant", "Cascadian Farm", "Pictsweet", "Season's Choice",
        # Ice Cream
        "Ben & Jerry's", "Häagen-Dazs", "Breyers", "Blue Bell", "Turkey Hill",
        # Tags
        "Frozen", "Ready-to-Heat", "Meal", "Convenience", "Single Serve"
    ],

    "Canned Vegetables": [
        # Major Brands
        "Del Monte", "Green Giant", "Libby's", "S&W", "Le Sueur", "Progresso",
        # Store Brands
        "Great Value", "Kirkland", "365", "Simple Truth",
        # Organic
        "Muir Glen", "Field Day", "Eden Organic",
        # Tags
        "Can", "Preserved", "Ready-to-Eat", "Vegetables", "Shelf-Stable"
    ],

    "Canned Fruits": [
        # Major Brands
        "Del Monte", "Dole", "Libby's", "S&W", "Sun-Maid", "Musselman's",
        # Store Brands
        "Great Value", "Kirkland", "365", "Simple Truth",
        # Tags
        "Can", "Preserved", "In Syrup", "In Juice", "Fruit", "Shelf-Stable"
    ],

    "Canned Soups": [
        # Major Brands
        "Campbell's", "Progresso", "Amy's", "Wolfgang Puck", "Pacific Foods",
        "Healthy Valley", "Imagine", "Annie's", "Chunky", "Well Yes!",
        # Store Brands
        "Great Value", "Kirkland", "365", "Simple Truth",
        # Tags
        "Can", "Ready-to-Eat", "Condensed", "Organic", "Low-Sodium"
    ],
    
    "Candy": [
        # Major Brands
        "Mars", "Hershey's", "Nestlé", "Cadbury", "Ferrero", "Mondelez",
        "Skittles", "Starburst", "Twizzlers", "Jolly Rancher", "Life Savers",
        "Haribo", "Trolli", "Sour Patch Kids", "Swedish Fish", "Mike and Ike",
        # Specialty/Gourmet
        "Sugarfina", "See's Candies", "Ghirardelli", "Lindt", "Godiva",
        # Store Brands
        "Great Value", "Kirkland Signature", "365",
        # Tags
        "Sweet", "Sour", "Chewy", "Hard", "Gummy", "Chocolate-covered"
    ],

    "Chocolate": [
        # Major International Brands
        "Hershey's", "Cadbury", "Lindt", "Ghirardelli", "Godiva", "Ferrero Rocher",
        "Mars", "Nestlé", "Toblerone", "Ritter Sport", "Milka", "Dove", "Russell Stover",
        # Premium/Artisanal
        "Valrhona", "Scharffen Berger", "Green & Black's", "Tony's Chocolonely",
        "Endangered Species", "Divine", "Theo Chocolate", "Lake Champlain",
        # Store Brands
        "Trader Joe's", "Kirkland Signature", "365",
        # Tags
        "Dark", "Milk", "White", "Premium", "Fair Trade", "Organic", "Bean-to-Bar"
    ],

    "Popcorn": [
        # Ready-to-Eat Brands
        "Smartfood", "Skinny Pop", "Boom Chicka Pop", "Popcornopolis", "Pipcorn",
        "Lesser Evil", "G.H. Cretors", "Trader Joe's", "Cracker Jack",
        # Microwave Brands
        "Orville Redenbacher's", "Pop Secret", "Act II", "Jolly Time", "Newman's Own",
        # Gourmet/Specialty
        "Garrett Popcorn", "Doc Popcorn", "Poppy Handcrafted", "Joe & Seph's",
        # Store Brands
        "Great Value", "Kirkland Signature", "365", "Simple Truth",
        # Tags
        "Ready-to-Eat", "Microwave", "Kettle Corn", "Caramel", "Cheese", "Natural"
    ],

    "Trail Mix": [
        # Major Brands
        "Planters", "Kar's", "Nature's Garden", "Trader Joe's", "Second Nature",
        "Back to Nature", "Bear Naked", "Kind", "Sahale Snacks", "Emerald",
        # Store Brands
        "Great Value", "Kirkland Signature", "365", "Simple Truth",
        # Types
        "Traditional", "Tropical", "Energy", "Omega", "Student", "Mountain",
        # Tags
        "Mixed", "Raw", "Roasted", "Sweet & Salty", "Organic", "Natural"
    ],

    "Granola Bars": [
        # Major Brands
        "Nature Valley", "Quaker", "KIND", "Clif Bar", "Luna Bar", "Larabar",
        "RXBar", "Fiber One", "Special K", "Kashi", "Annie's", "Think!",
        # Premium/Natural
        "Perfect Bar", "GoMacro", "This Saves Lives", "88 Acres", "Bobo's",
        # Store Brands
        "Great Value", "Kirkland Signature", "365", "Simple Truth",
        # Tags
        "Protein", "Granola", "Nut", "Fruit", "Energy", "Organic", "Gluten-Free"
    ],

    "Dried Fruits": [
        # Major Brands
        "Sun-Maid", "Ocean Spray", "Mariani", "Dole", "Sunsweet", "Made in Nature",
        "Trader Joe's", "That's it", "Peeled Snacks", "Bare Snacks",
        # Store Brands
        "Great Value", "Kirkland Signature", "365", "Simple Truth",
        # Types
        "Raisins", "Cranberries", "Apricots", "Dates", "Figs", "Mango", "Pineapple",
        # Tags
        "No Added Sugar", "Organic", "Sulfite-Free", "Natural", "Unsweetened"
    ],

    "Cheese Snacks": [
        # Major Brands
        "Cheetos", "Cheez-It", "Goldfish", "Combos", "Cheese Nips", "Moon Cheese",
        "Whisps", "Pirate's Booty", "Annie's", "Planters Cheez Balls",
        # Specialty/Health
        "From the Ground Up", "ParmCrisps", "Just the Cheese", "Keto Wise",
        # Store Brands
        "Great Value", "Kirkland Signature", "365", "Simple Truth",
        # Tags
        "Crunchy", "Puffed", "Baked", "Keto", "Gluten-Free", "Natural"
    ],

    "Rice Snacks": [
        # Major Brands
        "Quaker", "Rice Krispies", "Lundberg", "Annie's", "Trader Joe's",
        # Asian Brands
        "Nongshim", "Sanko", "Want Want", "Bin Bin", "One One",
        # Types
        "Rice Cakes", "Rice Crackers", "Rice Crisps", "Senbei", "Rice Rolls",
        # Store Brands
        "Great Value", "Kirkland Signature", "365", "Simple Truth",
        # Tags
        "Gluten-Free", "Low-Calorie", "Whole Grain", "Organic", "Asian-Style"
    ],

    "Fruit Snacks": [
        # Major Brands
        "Welch's", "Mott's", "Annie's", "Black Forest", "Kellogg's", "Betty Crocker",
        "Sun-Maid", "That's it", "BEAR", "Stretch Island",
        # Natural/Organic
        "YumEarth", "Surf Sweets", "Clif Kid", "GoGo squeeZ",
        # Store Brands
        "Great Value", "Kirkland Signature", "365", "Simple Truth",
        # Tags
        "Natural", "Organic", "No Added Sugar", "Real Fruit", "Kids", "School Safe"
    ]
}

# Canadian alternatives mapped by category
CATEGORY_ALTERNATIVES = {
    # Snacks
    "Chips": [
        "Covered Bridge", "Hardbite", "Miss Vickie's Canada", "Humpty Dumpty",
        "Yum Yum", "President's Choice", "Compliments", "Selection"
    ],
    
    "Crackers": [
        "Dare", "Christie", "President's Choice", "Compliments", "Selection",
        "Neal Brothers", "Mary Macleod's Shortbread"
    ],

    # Beverages
    "Soft Drinks": [
        "Canada Dry", "Crush Canada", "President's Choice", "Compliments Cola",
        "Selection Cola", "Big 8", "Cott Beverages"
    ],

    "Sports Drinks": [
        "BioSteel", "Guru", "FLOW Hydration", "Sapsucker", "Hydrator", "Viveau",
        "Canadian Mineral Water Co.", "Eska Sport"
    ],

    "Energy Drinks": [
        "Guru", "RISE Kombucha", "Flow Energy", "Beaver Buzz", "Rockstar Canada",
        "Red Bull Canada"
    ],

    "Juices": [
        "Sun-Rype", "Oasis", "Lassonde", "President's Choice", "Allen's",
        "Graves", "McCain Fruit Juices"
    ],

    # Breakfast & Cereal
    "Breakfast Cereal": [
        "Nature's Path", "President's Choice", "Compliments", "Selection",
        "Holy Crap Cereals", "One Degree Organic Foods"
    ],

    # Health & Beauty
    "Shampoo": [
        "AG Hair", "Live Clean", "Attitude", "The Green Beaver Company",
        "Cake Beauty", "Province Apothecary"
    ],

    "Toothpaste": [
        "Green Beaver", "Nelson Naturals", "Attitude", "President's Choice",
        "Life Brand", "Compliments"
    ],

    # Cleaning Products
    "Laundry Detergent": [
        "Nature Clean", "Bio-Vert", "Attitude", "The Soap Works",
        "President's Choice", "Compliments"
    ],

    "All-Purpose Cleaners": [
        "Nature Clean", "Bio-Vert", "Attitude", "Sapadilla",
        "President's Choice", "Compliments"
    ],

    # Paper Products
    "Paper Towels": [
        "Cascades", "Irving", "Kruger Products", "President's Choice",
        "Selection", "Compliments"
    ],

    "Toilet Paper": [
        "Cascades", "Irving", "Kruger Products", "President's Choice",
        "Selection", "Compliments"
    ],

    # Pet Products
    "Dog Food": [
        "Open Farm", "Canadian Naturals", "FirstMate", "Petcurean",
        "President's Choice Nutrition First", "Orijen"
    ],

    "Cat Food": [
        "Open Farm", "Canadian Naturals", "FirstMate", "Petcurean",
        "President's Choice Nutrition First", "Orijen"
    ],

    # Frozen Food
    "Frozen Food": [
        "President's Choice", "McCain Foods", "Arctic Gardens",
        "Pinty's", "Yves Veggie Cuisine", "Cedar"
    ],

    # Canned Goods
    "Canned Vegetables": [
        "President's Choice", "Compliments", "Selection",
        "Arctic Gardens", "Green Giant Canada"
    ],

    "Canned Fruits": [
        "President's Choice", "Compliments", "Selection",
        "Del Monte Canada"
    ],

    "Canned Soups": [
        "Habitant", "President's Choice", "Compliments",
        "Selection", "Campbell's Canada"
    ],

    # Candy
    "Candy": [
        "Dare", "Allan Candy Company", "Kerr's", "Ganong", "Laura Secord",
        "Pot of Gold", "Coffee Crisp", "Caramilk", "Mr. Big", "Wunderbar"
    ],

    # Chocolate
    "Chocolate": [
        "Laura Secord", "Purdy's", "Rogers' Chocolates", "Ganong",
        "Bernard Callebaut", "Chocolats Favoris", "Peace by Chocolate"
    ],

    # Popcorn
    "Popcorn": [
        "President's Choice", "Kernels Popcorn", "Bad Monkey Popcorn",
        "Canadian Popcorn Company", "Orville Redenbacher Canada"
    ],

    # Trail Mix
    "Trail Mix": [
        "President's Choice", "Prana", "Canadian Pure", "Selection",
        "Compliments", "Made Good"
    ],

    # Granola Bars
    "Granola Bars": [
        "Made Good", "President's Choice", "Vector", "Canadian Pure",
        "Nature Valley Canada", "Quaker Canada"
    ],

    # Dried Fruits
    "Dried Fruits": [
        "Patience Fruit & Co", "Fruit d'Or", "Canadian Berry Dryers",
        "Forbes Wild Foods", "Organic Traditions"
    ],

    # Cheese Snacks
    "Cheese Snacks": [
        "Hawkins Cheezies", "President's Choice", "Compliments",
        "Selection", "Great Value Canada"
    ],

    # Rice Snacks
    "Rice Snacks": [
        "President's Choice", "Compliments", "Selection",
        "Made Good", "Nature's Path Canada"
    ],

    # Fruit Snacks
    "Fruit Snacks": [
        "Made Good", "President's Choice", "Dare Real Fruit",
        "Sun-Rype", "Bear Paws", "Selection"
    ]
}