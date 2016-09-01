tutorial_link:
https://docs.python.org/2/tutorial/index.html
  command line link:
https://docs.python.org/2/using/cmdline.html#using-on-general


summarize:
- statement grouping is done by indentation
- no variable or argument declarations are necessary, no $,@,my,var,int, ...
- python, cmd z (mac), ctrl z (window)
- indentation is Python’s way of grouping statements, no comma, no parathesis
- a loop’s else clause runs when no break occurs.
- call python function by keyword arguments. Like perl with a hash argument. default argument like php, tuples args with *arg, dictionary arg with **dict

todo: personal web, about, my book, my favourite,...
todo: sublime my setting, favourite plugin
todo:
##uyenhoangnguyenhoangnguyenhoangnguyenhoangnguyenhoangnguyenhoangnguyenhoangnguyenhoang
todo:
get Takaaki's slide
todo: change first character of each line to capital letters.



#todo: problem with string.punctuation.
#If I stand at home directory, then it's ok
#something related to module import, namespace here.
#DONE, sublime, .pyc file

#todo:
#1. change file name to this_format DONE
#2. make do.py ...
#3. make todo list: enter, display, mark progress
#1. Change all password.
#2. change $ for ubuntu
#3. Make shortcut


The art of readable code ideas:
Part I: Surface Level
    chapter 1. Code should be easy to understand
    chapter 2. Pack information in your names:
        Use specific word: fetch instead of get
            Finding  more colorful words
        Avoid generic names like tmp or retval
            Have a good reason to use generic names like tmp, i, retval,...
            Loop iterator
            Prefer concrete names over abstract names
        Attaching extra information to a Name (names like a tiny comment):
            Values with units (size -> size_mb, start -> start_ms)
            Shorter names are ok for shorter scope (varialbes that less used)
            Acronyms and Abbreviations: think for new project member
            Throwing out unneeded words: ConvertToString -> ToString
        Use name formatting to convey meaning:
            _ for private member,
            var $img  $("#img") for jQuery object
            id="use_unsderscore" class="use-dashes"
    chapter 3. Name that can't be miscontrued
        What other meaning could someone interpret from this name:
            select(), exclude() instead of filter
            truncate(text, max_chars) instead of clip(text, length)
        Use Min and Max instead of Limit
        Use First and Last for Inclusive Ranges
        Use Begin, End for Inclusive/Exclusive Ranges
        Naming boolean:
            need_password instead of read_password
            HasSpaceLeft() instead of SpaceLeft()
            bool use_ssl = true instead of bool disable_ssl = false
        Matching Expectations of Users: users may expect get() or size() to be lightweight methods
            computeMean instead of getMean
            countElements instead of size
        Evaluating multiple name candidates
    chapter 4: Aesthetics
        Rearrange line break to be consistent and compact
            Use methods to clean up irregularity
            Use column alignment when helpful: just stop if it takes much effort
            Pick a meaningful order and use it consistently
        Break code into paragraphs, like text
        Personal style versus consistency: choose consistency
    chapter 5: Knowing what to comment
        What not to comment:
            The purpose of commenting is to help reader know as much as writer did
            Don't comment on facts that can be quickly derived from code itself
            Don't comment just for sake of commenting
            Don't comment bad name, fix the names instead:
            self-documenting names
            good code > bad code + good comments
        Recording your thought:
            Include "Director comentary"
            Comment the flaws in your code
            Comment on your constant
            Put yourself int the reader's shoes
            Anticipating likely questions
            Advertising likely pitfalls
            Big picture comments
            Summary comments
            Final thoughts - getting over writer's block
    Chapter 6: Making comment precise and Compact
        Keep comments compact: comments should have a high information-to-space ratio
        Avoid ambiguous pronounces:
            //Insert data to cache, if it's small -> //if data is small, insert it to the cache
        Polish sloppy sentences:
            #Depending on whether we've already crawled this url before, give it a different priority
            #Give higher priority for never ever crawled url
        Use input/output example that illustrate corner cases
        State the Intent of your code:
            //Iterate through the list in  reverse order ->
            //Display each price, from highest to lowest
        Use Named function parameter as comment, thanks to Python, Perl
        Use information-dense words to compact comment
Part II: Simplifying loops and logic
    Chapter 7: Making control flow easy to read
        The order of Arguments in Conditionals: more constant exp should be in the right hand:
            if (length >= 10) // if (byte_received <= byte_expected
        The order of if/else block:
            prefer positive case first
            prefer simpler case first
            prefer more interesting, conspicuous first
        The ternary operator: should use only when choosing between two simple values
        Avoid using do/while loop. It's just unnatural. Using while instead
        Minimize nesting:
            Avoid using if within if within if ...
            Look at the code from fresh perspective when youre making changes,do not
            sacrifies the readability for clean diff.
            Removing nesting by returning early
            Removing nesting inside loop: guard statements

    Chapter 8: Breaking down giant expression
        Explaining variables:
            if line.split(:)[0].strip == "root" -> user_name = line.split(":"), if (user_name == 'root')
        Summary variables:
            if(request.user_id == document.owner_id) -> bool user_owns_document = (request.user_id == document.owner_id)
        Using De Morgan's law
        Abusing short-circuit logic: Be aware of "clever" nuggets of code
        Wrestling with complicated logic: Finding another approach: opposite approach, nice example
        Breaking down giant statements: Dont Repeat Yourself :D
        Another Creative Way to Simplify Expressions: C++ macro, all for readability
    Chapter 9: Variables and readability
        Eliminating variables:
            Useless temporary variables
            Eliminating intermediate results
            Eliminating control flow variables
        Shrink the scope of varialbes: make vars visible by as few lines of code as possible
            If statement scope in C++ (if PaymentInfo* info = database.ReadPaymentInfo)
            Creating Private variables in javascript: use a closure (Javascript: the good part)
            Javascript global scope: Always use var for local variable
            No nested (block scope) in  Python, javascript and PHP save C++, Perl, Java
            Moving definition down (no need at the top)
            Prefer write-once variables: for(;true;)
Part III: Reorganizing your code
    Chapter 10: Extracting unrelated subproblems
        Pure Utility Code: I wish our library has an XYZ function
        Other general-purpose code: log
        Project-Specific Functionality
        Simplifying an existing interface
        Reshaping an interface to your needs
        Taking things too far: Until when some small functions called 2nd time, there is no need
    Chapter 11: One task at a time
        Task can be small: very nice example: vote_changed
        Extracting values from an object, applying "one task at a time", fragemented code, another nice example
        Another approach: Even greater solution
        A larger example and further improvement: one task at a time
        Summary: If you have code that’s difficult to read, try to list all of the tasks it’s doing.
    Chapter 12: Turning thought into Code
        Describing logic clearly: another nice approach: NOT
        Knowing your libraries helps: part of writting succint code is being aware of what your library has to offer
        An English description of the solution
        Applying the method recursively
        Summary: what is called "ubber ducking" techinique ?
    Chapter 13: Writting less code: the most readable code is not code at all
        Don't bother implementing that feature. You won't need it
        Question and break down your requirements: Store locator and adding a cache example
        Keeping your code base small: remove unused code
        Be familiar with the libraries around you: reading libs once in a while
        Why Reusing Libraries Is Such a Win
Part IV: Selected Topics
    Chapter 14: Testing and Readability
        Make Tests Easy to Read and Maintain
        Creating the minimal test statement: even one line of code
        Making error message readable: using better version of assert
        Choosing good test inputs: choose the simplest ones but completely excercise the code
        Multiple Tests of Functionality
        Test-Friendly Development: not too much setup, state (test driven development)
        Going too far
    Chapter 15: Designing and implementing a minute/hour counter: I'm so trivial. I'm a journey man, not a master.



q: InnoDB and MyISam ?
q: int(5), char(23), var_char(200) ? in sql mean 5 byte ?
q: where is my dot, marvel, ninja code ?
q: what is constrain in mysql ?
q: When not in transaction, if execute "mysql source mybook_database.sql but there is some syntax error query, then other queries are execute, no matter where are they ?
a: yes, they are executed, though they are above or below the wrong syntax query
