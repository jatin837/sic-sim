import Data.List
import Data.Matrix

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

getNodeFromBranch :: Branch -> [Node]
getNodeFromBranch b = [a1, a2] where 
 a1 = fst $ fst b 
 a2 = snd $ fst b 

getNodeList :: Circuit -> [Node]
getNodeList cir = tail 
 $ sort
 $ nub
 $ concatMap getNodeFromBranch cir

isNodeInBranch :: Node -> Branch -> Bool
isNodeInBranch n b = elem  n $ getNodeFromBranch b

getConnectedComponents :: Node -> Circuit -> [Component]
getConnectedComponents n circuit = map snd 
 $ filter (isNodeInBranch n) circuit

indexList :: Int -> Int -> [(Int, Int)]
indexList i j = [(i, j) | i <- [1..n], j <- [1..n]]

getComponentValue :: Component -> Float
getComponentValue (R val) = val
getComponentValue (V val) = val
getComponentValue (I val) = val

getTotalConductance :: (Node, Node) -> Circuit -> Double
getTotalConductance (i, j)
 | i == j = 5.0 -- TODO get resistors connected to i
 | otherwise = 6.6 -- TODO get resistors connected to i, j

n = length
 $ getNodeList cir

g = matrix n n (\(_, _) -> 0.0)
