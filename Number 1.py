lang  = {
    'Go' : 'A statically typed, compiled programming language designed at Google', 
    'C++':'C++ is a general-purpose programming language created by Bjarne Stroustrup as an extension of the C programming language, or C with Classes',
    'C':'C is a general-purpose, procedural computer programming language supporting structured programming, lexical variable scope, and recursion, with a static type system', 
    'Java': 'A high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible',  
    'Swift': 'Swift is a general-purpose, multi-paradigm, compiled programming language developed by Apple Inc. and the open-source community'
}


for key,value in sorted (lang.items()):
    print(key, end = "\n") 
    print(value, end = "\n ")
    print()