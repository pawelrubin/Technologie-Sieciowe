package csma

class Transmission(
  var direction : Int,
  var id : Char
) {
  override fun toString(): String {
    return id.toString()
  }
}