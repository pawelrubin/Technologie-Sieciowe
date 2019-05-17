package csma

class Node (
  var id : Char,
  var position : Int,
  var emits : Boolean,
  var collision : Boolean,
  var timeout : Int,
  var probability : Double,
  var mult : Int
)