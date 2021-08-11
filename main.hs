type Volt = Float
type Amp = Float
type Ohm = Float
type Node = Int
type Branch = ((Node, Node), Component)

data Component = 
 V Volt | R Ohm | I Amp deriving(Show)

cir :: [Branch]
cir = [((0, 1), V 4.4), ((1, 2), R 1), ((1, 2), R 2), ((1, 2), R 2), ((2, 3), R 3), ((3, 0), R 5)]
