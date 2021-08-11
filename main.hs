type Volt = Float
type Amp = Float
type Ohm = Float
type Node = Int

data Component = 
 V Float | R Float | I Float deriving(Show)


data Circuit = Circuit { nodes :: (Node, Node),
                         components :: [Component]
                       } deriving(Show)
