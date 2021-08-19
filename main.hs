type Volt = Float
type Amp = Float
type Ohm = Float
type Node = Int
type Branch = ((Node, Node), Component)
type Circuit = [Branch]

data Component = 
 V Volt | R Ohm | I Amp deriving(Show)

cir :: Circuit
cir = [ 
 ((0, 1), R 2), 
 ((1, 2), V 32), 
 ((0, 2), R 8), 
 ((2, 3), R 4),
 ((0, 3), V 20)
 ]
