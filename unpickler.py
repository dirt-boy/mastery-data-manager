# Load the dictionary back from the pickle file.
import pickle
 
token  = pickle.load( open( "token.pickle", "rb" ) )
print token
