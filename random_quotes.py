#import random
from random import choice
from verse_of_day import get_bible_quote_of_day

philosophical_quotes = [
    "The only true wisdom is in knowing you know nothing. - Socrates"
    , "The unexamined life is not worth living. - Socrates"
    , "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson"
    , "I think, therefore I am. - René Descartes"
    , "Life is what happens when you're busy making other plans. - John Lennon"
    , 'Hardship often prepares an ordinary person for an extraordinary destiny. - Christopher Markus'
    , 'There is no easy way from the earth to the stars. - Seneca'
    , 'Well, I must endure the presence of a few caterpillars if I wish to become acquainted with the butterflies. - Antoine de Saint-Exupéry'
    , 'You have power over your mind - not outside events. Realize this, and you will find strength. - Marcus Aurelius'
    , 'The flame that burns Twice as bright burns half as long - Lao Tzu'
    , 'The price good men pay for indifference to public affairs is to be ruled by evil men - Plato'
    , 'The only thing I know is that I know nothing. - Socrates'
    , 'Freedom is secured not by the fulfilling of one\'s desires, but by the removal of desire. - Epictetus'
    , 'Everything we hear is an opinion, not a fact. Everything we see is a perspective, not the truth. - Marcus Aurelius'
    , 'The greater the difficulty, the more glory in surmounting it. - Epicurus'
    , 'The function of prayer is not to influence God, but rather to change the nature of the one who prays. - Søren Kierkegaard'
    , "Even the finest sword plunged into salt water will eventually rust. - Sun Tzu"
    , 'Doing nothing is better than being busy doing nothing. - Lao Tzu'
    , 'Man is born free, but is everywhere in chains. - Jean-Jacques Rousseau'
    , "Even while they teach, men learn. - Seneca the Younger"
    , "Science is what you know. Philosophy is what you don't know. - Bertrand Russell"
    , "If you would be a real seeker after truth, it is necessary that at least once in your life you doubt, as far as possible, all things. - René Descartes"
    , "A little philosophy inclineth man's mind to atheism; but depth in philosophy bringeth men's minds about to religion. - Sir Francis Bacon"
    , "The brave man is he who overcomes not only his enemies but his pleasures. - Democritus"
    , "History is Philosophy teaching by examples. - Thucydides"
    , "We are what we repeatedly do. Excellence, then, is not an act, but a habit. - Aristotle"
    # Add more quotes as needed
    ]

inspirational_quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can, and you're halfway there. - Theodore Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "In the middle of every difficulty lies opportunity. - Albert Einstein",
    "The secret of getting ahead is getting started. - Mark Twain"
    , "The bad news is time flies. The good news is you're the pilot. — Michael Altshuler"
    ,  "Keep your face always toward the sunshine, and shadows will fall behind you. - Walt Whitman"
    # Add more inspirational quotes as needed
]

# format = [ [text, speech_version] ]
bible_quotes =[  
                 ['Romans 15:13 - May the God of hope fill you with all joy and peace as you trust in him, so that you may overflow with hope by the power of the Holy Spirit.', 'Romans Chapter 15, Verse 13... May the God of hope fill you with all joy, and peace as you trust in him, so that you may overflow with hope, by the power of the Holy Spirit.']
               , ['Romans 8:38-39 - For I am convinced that neither death nor life, neither angels nor demons, neither the present nor the future, nor any powers, neither height nor depth, nor anything else in all creation, will be able to separate us from the love of God that is in Christ Jesus our Lord.', 'Romans Chapter 8, Verses 38-39... For I am convinced that neither death nor life, neither angels nor demons, neither the present nor the future, nor any powers, neither height nor depth, nor anything else in all creation, will be able to separate us from the love of God that is in Christ Jesus our Lord.']
               , ['Lamentations 3:22-23 - The steadfast love of the Lord never ceases; his mercies never come to an end; they are new every morning; great is your faithfulness.', 'Lamentations Chapter 3, Verses 22-23... The steadfast love of the Lord never ceases; his mercies never come to an end; they are new every morning; great is your faithfulness.']
               , ['Romans 8:31 - What, then, shall we say in response to these things? If God is for us, who can be against us?', 'Romans Chapter 8, Verse 31... What then, shall we say in response to these things? If God is for us, who can be against us?']
               , ['Psalm 27:1 - The Lord is my light and my salvation; whom shall I fear? The Lord is the stronghold of my life; of whom shall I be afraid?', 'Psalm Chapter 27, Verse 1... The Lord is my light and my salvation; whom shall I fear? The Lord is the stronghold of my life; of whom shall I be afraid?']
               , ['Isaiah 40:31 - But they who wait for the Lord shall renew their strength; they shall mount up with wings like eagles; they shall run and not be weary; they shall walk and not faint.', 'I zay ah Chapter 40, Verse 31... But they who wait for the Lord shall renew their strength; they shall mount up with wings like eagles; they shall run and not be weary; they shall walk and not faint.']
               , ['Philippians 4:13 - I can do all things through him who strengthens me.','Philippians Chapter 4, Verse 13... I can do all things through him who strengthens me.' ]
               , ['Proverbs 3:5-6 - Trust in the Lord with all your heart, and do not lean on your own understanding. In all your ways acknowledge him, and he will make straight your paths.', 'Proverbs Chapter 3, Verses 5-6... Trust in the Lord with all your heart, and do not lean on your own understanding. In all your ways acknowledge him, and he will make straight your paths.']
               , ['Matthew 17:20 - Our faith can move mountains.', 'Matthew Chapter 17, Verse 20... Our faith can move mountains.']
               , ['Psalm 107:1 - Give thanks to the Lord, for He is good; his love endures forever.', 'Psalm Chapter 1 o 7, Verse 1... Give thanks to the Lord, for He is good; his love endures forever.']
               , ['Jeremiah 29:11 - "For I know the plans I have for you," declares the Lord, "plans to prosper you and not to harm you, plans to give you hope and a future."', 'Jeremiah Chapter 29, Verse 11... "For I know the plans I have for you." declares the Lord, "plans to prosper you and not to harm you, plans to give you hope and a future."']
               , ['Psalm 34:8 - Taste and see that the Lord is good; blessed is the one who takes refuge in him.','Psalm Chapter 34, Verse 8... Taste and see that the Lord is good; blessed is the one who takes refuge in him.' ]
               , ['Matthew 11:8 - Come to Me, all you who are weary and burdened, and I will give you rest.', 'Matthew Chapter 11, Verse 8... Come to Me, all you who are weary and burdened, and I will give you rest.']
               , ['John 3:16 - For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life.', 'John Chapter 3, Verse 16... For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life.']
               , ['Psalm 91:11 - For he will command his angels concerning you to guard you in all your ways.', 'Psalm Chapter 91, Verse 11... For he will command his angels concerning you to guard you in all your ways.']
               , ['Ephesians 2:8-10 - For by grace you have been saved through faith. And this is not your own doing; it is the gift of God, not a result of works, so that no one may boast. For we are his workmanship, created in Christ Jesus for good works, which God prepared beforehand, that we should walk in them.', 'Ephesians Chapter 2, Verses 8-10... For by grace you have been saved through faith. And this is not your own doing; it is the gift of God, not a result of works, so that no one may boast. For we are his workmanship, created in Christ Jesus for good works, which God prepared beforehand, that we should walk in them.']
               , ['Philippians 4:7 - And the peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus.', 'Philippians Chapter 4, Verse 7... And the peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus.']
               , ['Psalm 118:14 - The LORD is my strength and my defence; he has become my salvation', 'Psalm Chapter 1 18, Verse 14... The LORD is my strength and my defence; he has become my salvation']
               , ["2 Corinthians 12:10 - That is why, for Christ's sake, I delight in weaknesses, in insults, in hardships, in persecutions, in difficulties. For when I am weak, then I am strong.", "Second Corinthians Chapter 12, Verse 10... That is why, for Christ's sake, I delight in weaknesses, in insults, in hardships, in persecutions, in difficulties. For when I am weak, then I am strong."]
               , ["James 1:17 - Every good and perfect gift is from above, coming down from the Father of the heavenly lights, who does not change like shifting shadows.", "James Chapter 1, Verse 17... Every good and perfect gift is from above, coming down from the Father of the heavenly lights, who does not change like shifting shadows."]
               , ["Psalm 121:2 - My help comes from the Lord, the Maker of heaven and earth.", "Psalm Chapter 1 21, Verse 2... My help comes from the Lord, the Maker of heaven and earth." ]
               , ["John 15:13 - Greater love has no one than this: to lay down one's life for one's friends.", "John Chapter 15, Verse 13... Greater love has no one than this: to lay down one's life for one's friends."]
               , ["Romans 8:28 - And we know that in all things God works for the good of those who love him, who have been called according to his purpose.", "Romans Chapter 8, Verse 28... And we know that in all things God works for the good of those who love him, who have been called according to his purpose."]
               , ["Philippians 4:6 - Do not be anxious about anything, but in everything, by prayer and petition, with thanksgiving, present your requests to God.", "Philippians Chapter 4, Verse 6... Do not be anxious about anything, but in everything, by prayer and petition, with thanksgiving, present your requests to God."]
               , ["Matthew 5:14 - You are the light of the world. A city that is set on a hill cannot be hidden", "Matthew Chapter 5, Verse 14... You are the light of the world. A city that is set on a hill cannot be hidden"]
               , ["Psalm 23:1-2 - The LORD is my shepherd; I shall not want. He maketh me to lie down in green pastures: he leadeth me beside the still waters.","Psalm Chapter 23, Verses 1-2... The LORD is my shepherd; I shall not want. He maketh me to lie down in green pastures: he leadeth me beside the still waters." ]
               , ["Romans 6:23 - For the wages of sin is death, but the gift of God is eternal life in Christ Jesus our Lord.", "Romans Chapter 6, Verse 23... For the wages of sin is death, but the gift of God is eternal life in Christ Jesus our Lord."]
               ]


def get_random_quote(quote_type):
    if quote_type == 'inspirational':
        random_quote = choice(inspirational_quotes)
        quote_list = [random_quote, random_quote]
    elif quote_type == 'philosophical':
        random_quote = choice(philosophical_quotes)
        quote_list = [random_quote, random_quote]
    elif quote_type == 'bible':
        quote_list = get_bible_quote_of_day() #random.choice(bible_quotes)
    else:
        quote_list =['Unknown Quote Type', 'Unknown Quote Type']

    return quote_list


