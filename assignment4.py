#import libraries
import aima.utils
import aima.logic

## The main entry point for this module
def main():
    # Create an array 
    Array=[]
    
    # Add first-order logic Array (rules and fact)
    Array.append(aima.utils.expr("Woman(jia)"))
    Array.append(aima.utils.expr("Man(john)"))
    Array.append(aima.utils.expr("Healthy(john)"))
    Array.append(aima.utils.expr("Healthy(jia)"))
    Array.append(aima.utils.expr("Wealthy(john)"))
    Array.append(aima.utils.expr("(Healthy(x) & Wealthy(x)) ==> Traveler(x)"))
    Array.append(aima.utils.expr("Traveler(x) ==> travel(x)"))
     
    # Create a first-order logic knowledge base (KB) with Array
    KB = aima.logic.FolKB(Array)
      
    # Get information from the knowledge base with ask
    travel=KB.ask(aima.utils.expr('Traveler(x)'))
    Wealthy=KB.ask(aima.utils.expr('Wealthy(x)'))
    Healthy=KB.ask(aima.utils.expr('Healthy(x)'))
      
    # Print answers
    print('Who can travel?')
    print(travel)
    print()
    print('who are Wealthy?')
    print(Wealthy)
    print()
    print('who are Healthy?')
    print(Healthy)
    print()
       
    # Tell python to run main method
    if __name__ == "__main__": main()