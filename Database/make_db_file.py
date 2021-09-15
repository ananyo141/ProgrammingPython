# Save the in-memory database to a file

dbfilename = 'people-file.auto'
ENDDB  = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

def storeDbase(db, dbfilename = dbfilename) -> None:
    "formatted dump of database to flat file"

    with open(dbfilename, 'w') as dbfile:
        for key in db:
            print(key, file = dbfile)               # write the individual keys: name(str)
            for (name, value) in db[key].items():   
                print(name + RECSEP + repr(value), file = dbfile)  # write the data in dict formatted as python datatype
            print(ENDREC, file = dbfile)            # end marker for one individual record
        print(ENDDB, file = dbfile)                 # end marker for the database

def loadDbase(dbfilename = dbfilename) -> dict:
    "parse the data to reconstruct database"
    
    import sys
    reconstructedDatabase = {}  # a dict of dict
    with open(dbfilename, 'r') as dbfile:
        sys.stdin = dbfile      # redirect input from dbfile
        
        key = input()                               # read first key or name(str) input,
        while (key != ENDDB):                       # and continue until reach END OF DATABASE
            rec = {}
            field = input()                         # read data fields until END OF RECORD
            while field != ENDREC:                  
                (name, value) = field.split(RECSEP) # and separate with field separator
                rec[name] = eval(value)             # read the pythonic-value
                field = input()    

            reconstructedDatabase[key] = rec        # insert the dictionary into the database
            key = input()

    return reconstructedDatabase


if __name__ == '__main__':
    from initdata import db
    storeDbase(db)
