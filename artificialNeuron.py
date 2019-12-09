
#Single Artificial Neuron.
#created by Isaí vargas Chávez-Age 19 All rigths reserved /Users/Isai/eclipse-workspace/Perceptron/src/NeuronalNetworks/ArtificialNeuron.java@
# Compilador Clang 6.0 (clang-600.0.57)] on darwin.
# version 1.0.
# 03/02/2018 in Mexico City.
import random 

class Neuron :
       #Atributes
        bias  =  0
        y  =  0    #Output
        v =  0
        inputsignal = 0
        inputweight = 0
        inputsVector  = [  ]
        weightsVector = [  ]
        trainingVector = [  ]
        learningRate = 0
        iterathion = 0 
     
   
        def __init__( self ) :
             self.bias = 1
             self.inputweight = float(self.inputweight)
             self.learningRate = 0.5
             self.inputsVector  =   [ 1  ]
             self.weightsVector =  [ ]
             self.trainingVector =  [  ]
        
        def add_inputVector(self,inputsVector) :
                self.inputsVector.append ( inputsVector )

        def add_trainingVector(self,inputTrainSet) :
              self.trainingVector.append (inputTrainSet)
                                                   

        def  add_weightsVector (self,numberinputs):
                   self.num =numberinputs
                   start = -1.0
                   end   =  1.0
                   for j in range(self.num):
                        self.weightsVector.append( random.uniform(start, end) )

                     

        def  Synapsis( self,iterathion,numberinputs,inputsVector): #where the function spect a variable number of arguments.
                 v = 0
                 self.inputsVector
                 self.weightsVector
                 for  k in range (iterathion) :
                       self.numberinputs = numberinputs +1  
                       for  j  in  range(self.numberinputs) :    
                            v = v + ( (self.inputsVector [ j ]*[ iterathion ]) *(self.weightsVector[ j ]*[ iterathion ] ) )

                 print (' V : ' ,v)
                 return v
               

        def   Signum( self ):#Activation FUNCTION.
                  if  self.v > 0:  # Signum Function!
                      self.y = 1
                  else :
                      self.y = 0
                      
                  print ('Out put:',self.y)
                  return self.y

        def Learn( self,y,iterathion,inputsVector,weightsVector,trainOutput,k) : # Learning function
               k = 1
               if self.y == self.trainOutput:
                    self.weightsVector = self.inputweight*(iterathion )
                    
               elif self.y > 0:
                     self.inputweight  = self.inputweight +  self.learningRate *(self. trainOutput*self.iterathion) -  (self.y *self.iterathion) *(self.inputsVector*self.iterathion)
               else:
                     self.weightsVector = self.weightsVector -  self.learningRate *(self. trainOutput*self.iterathion) -  (self.y *self.iterathion) *(self.inputsVector*self.iterathion)

               return self.weightsVector

                      
              
           
                      
         

                        

